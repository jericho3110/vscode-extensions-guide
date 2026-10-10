# Security

## Contents

1. [Threat model: extensions are code with your rights](#1-threat-model-extensions-are-code-with-your-rights)
2. [What protects you, and what doesn't](#2-what-protects-you-and-what-doesnt)
3. [The .cmd batch-file trap](#3-the-cmd-batch-file-trap)
4. [RCE paths in this repo](#4-rce-paths-in-this-repo)
5. [Checklist before installing an extension](#5-checklist-before-installing-an-extension)
6. [Review table](#6-review-table)
7. [Accepted risks](#7-accepted-risks)
8. [References](#references)

---

## 1. Threat model: extensions are code with your rights

The official docs: *"The extension host has the same permissions as VS Code
itself"*. An extension can **read and write files, make network requests and
run external processes**.

| Threat | Example |
| --- | --- |
| a malicious extension | steals SSH keys, tokens, browser data |
| **typosquatting** | `ms-pyhton.python` instead of `ms-python.python` |
| a good extension turns bad | a hijacked publisher account ships a malicious update; auto-update installs it |
| a malicious *repository* | a cloned repo's `.vscode/tasks.json` or settings make an extension run its code |
| a malicious install list | `extensions.txt` with something sneaked in (§3) |

## 2. What protects you, and what doesn't

| Protection | What it does | Limit |
| --- | --- | --- |
| Marketplace malware scan | each published package is scanned | scanners miss new tricks |
| **Verified publisher** (blue check) | the publisher proved they own a domain | proves identity, not good intent |
| Name-squatting checks | blocks names copying official publishers | not perfect |
| Block list | known-malicious extensions are removed and **uninstalled automatically** | only after discovery |
| Signature check | VS Code checks the Marketplace signature at install | proves it came from the Marketplace unchanged, not that it's safe |
| Publisher trust prompt (1.97+) | asks before the first install from a new publisher | **not shown for `code --install-extension`** |
| **Workspace Trust** | in a folder you haven't trusted, tasks, debugging and many extension features are off | only if you don't click "Trust" by reflex |
| update delay (`extensions.autoUpdateDelay`, 12 h) | bad releases are often caught within hours | not a guarantee |

## 3. The .cmd batch-file trap

On Windows, `shutil.which("code")` finds
`...\Microsoft VS Code\bin\code.CMD`, which is a **batch file**. Windows can't
start a batch file directly, so it runs `cmd.exe`, and **`cmd.exe` re-parses
the arguments**. Python's list form (`subprocess.run([...])`) protects you
from a shell on Linux and macOS, but not here. An "id" such as

```text
ms-python.python & calc
```

would run `calc` after the install. This class of bug got CVEs across
several languages in 2024 ("BatBadBut").

**Fix:** every id is checked against a strict pattern before it can reach
`code`: letters, digits, hyphens, one dot and an optional `@1.2.3` version.
`& | % ^ " < >`, spaces and newlines can't pass.

```python
EXT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9][A-Za-z0-9-]*(@\d+(\.\d+){0,3})?$")
```

Test: `test_rejects_anything_cmd_exe_could_interpret` tries `&`, `|`, `%PATH%`,
`^`, a quote, a newline, `--force` and a path. Proven live:

```text
$ python main.py install bad.txt      # bad.txt contains: evil.x & calc
error: not a valid extension id: 'evil.x & calc' (expected publisher.name[@version])
```

## 4. RCE paths in this repo

| Path | Input | Defense |
| --- | --- | --- |
| `code --install-extension <id>` | ids from a list file | strict `EXT_ID` check (§3); argument list; confirm, default no |
| `code --list-extensions` output | VS Code's own output | parsed with the same `validate()` |
| `extensions.json` parsing | a repo's file (untrusted) | `json.loads` only (no `eval`); size limit 200 KB; must be a list of strings |
| `python main.py check` | fixed commands | no user input |

No `eval`, `exec`, `pickle` or `shell=True` anywhere; `devtools scan` checks
this in the gate.

## 5. Checklist before installing an extension

1. Is the **id exactly right**? Copy it from the Marketplace URL; watch for typosquats.
2. **Publisher:** verified? The language's own team? Lots of installs and a long history?
3. **Source:** is there a GitHub repo, and does the Marketplace page link to it?
4. **Recent changes:** a sudden new owner or a big unexplained update is a warning sign.
5. **Need:** is it built into VS Code already? Fewer extensions, less risk.
6. **Untrusted folders:** open unknown repos in **Restricted Mode** (don't trust the workspace).

## 6. Review table

| # | Finding | Fix | Test |
| --- | --- | --- | --- |
| 1 | `code` is a `.cmd` on Windows, so an id with `&` would run a command | strict id pattern before any call | `test_rejects_anything_cmd_exe_could_interpret` |
| 2 | a bad list printed a Python traceback | catch `ValueError`/`OSError` in `main.py`, print one line | manual run (§3) |
| 3 | a huge list file could use a lot of memory | 200 KB limit | `test_oversized_list_refused` |

## 7. Accepted risks

| Limit | Why accepted |
| --- | --- |
| the tool trusts that an id names the extension you meant | it can't know your intent; it shows the plan and asks |
| no check of the publisher's verified status | that needs the Marketplace API (network); use the checklist |
| the JSONC trailing-comma fix also edits `,]` inside strings | extension lists never contain that (noted in the code) |

## References

### Official

- VS Code: [Extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) ✔ (permissions, Marketplace protections, publisher trust, CLI note), [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)
- Python: [subprocess on Windows: batch files](https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
- Microsoft: [cmd.exe](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

### Other

- Flatt Security, [BatBadBut: You can't securely execute commands on Windows](https://flatt.tech/research/posts/batbadbut-you-cant-securely-execute-commands-on-windows/)
- [OWASP: Command injection](https://owasp.org/www-community/attacks/Command_Injection)

### Further learning

- [OWASP Top 10: Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
