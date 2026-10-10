# Installing extensions: every way

From clicking a button to installing from a list in a script. Each command
and flag is explained, and the examples are real output from this machine.

## Contents

1. [The extension id](#1-the-extension-id)
2. [In the editor](#2-in-the-editor)
3. [From the command line](#3-from-the-command-line)
4. [From a program: Python, PowerShell, bash, Node](#4-from-a-program-python-powershell-bash-node)
5. [Per project: recommendations](#5-per-project-recommendations)
6. [Per workflow: profiles](#6-per-workflow-profiles)
7. [Offline: VSIX files](#7-offline-vsix-files)
8. [Updating and removing](#8-updating-and-removing)
9. [Exercises](#9-exercises)
10. [References](#references)

---

## 1. The extension id

Every extension has an id, **`publisher.name`**: `rust-lang.rust-analyzer`
is the extension `rust-analyzer` by the publisher `rust-lang`. Ids are
case-insensitive. Add `@version` to pin one: `ms-python.python@2026.8.0`.

Find an id on the Marketplace page (the `itemName=` part of the URL), or in
the editor: right-click an extension and choose **Copy Extension ID**.

## 2. In the editor

| Way | How |
| --- | --- |
| Extensions view | `Ctrl+Shift+X`, search, **Install** |
| Pre-release | the dropdown next to **Install** → **Install Pre-Release Version** |
| Quick Open | `Ctrl+P`, type `ext install rust-lang.rust-analyzer`, Enter |
| Recommended for this repo | Extensions view → **Recommended** (from `.vscode/extensions.json`, §5) |

Since VS Code 1.97, installing from a publisher you haven't used before
asks you to confirm that you **trust the publisher**. See [SECURITY.md](SECURITY.md).

## 3. From the command line

The `code` command comes with VS Code. On Windows it's
`...\Microsoft VS Code\bin\code.cmd`; if it's missing, run **Shell Command:
Install 'code' command in PATH** from the Command Palette.

| Command | What it does |
| --- | --- |
| `code --list-extensions` | one id per line |
| `code --list-extensions --show-versions` | `id@version` per line |
| `code --list-extensions --category <cat>` | only one category (e.g. `"Programming Languages"`) |
| `code --install-extension <id>` | install, or update if already installed |
| `code --install-extension <id>@1.2.3` | install exactly that version |
| `code --install-extension <id> --pre-release` | install the pre-release channel |
| `code --install-extension <id> --force` | update to the latest without asking |
| `code --install-extension ./file.vsix` | install from a downloaded package (§7) |
| `code --uninstall-extension <id>` | remove |
| `code --update-extensions` | update everything installed |
| `code --disable-extensions` | start VS Code with every extension off (for troubleshooting) |
| `code --extensions-dir <dir>` | use a different extensions folder |
| `code --profile <name>` | open with a profile, which has its own extension set (§6) |

Real output when the 9 language extensions were added:

```text
$ code --install-extension rust-lang.rust-analyzer
Extension 'rust-lang.rust-analyzer' v0.3.3073 was successfully installed.
$ code --install-extension llvm-vs-code-extensions.vscode-clangd
Extension 'llvm-vs-code-extensions.vscode-clangd' v0.6.0 was successfully installed.
```

**Note:** installing from the command line doesn't show the publisher
trust prompt. You're trusting the publisher by typing the id, so check it first.

## 4. From a program: Python, PowerShell, bash, Node

Moving to a new computer? Save your list on the old one and install it on
the new one.

### Python (this repo's tool)

```bash
python main.py export my-extensions.txt          # save what's installed
python main.py install my-extensions.txt         # shows the plan, asks [y/N]
python main.py install .vscode/extensions.json   # a repo's recommendations work too
```

Real run:

```text
$ python main.py install examples/multi-language.txt
16 already installed, 0 to install:
```

What it does that a one-liner doesn't:

| Feature | Why |
| --- | --- |
| validates every id against `publisher.name[@version]` | on Windows `code` is a **batch file**, and `cmd.exe` would act on `&`, `\|` or `%` inside an argument (see [SECURITY.md](SECURITY.md#3-the-cmd-batch-file-trap)) |
| shows the plan, asks, defaults to **no** | extensions run with your rights; installing is a decision |
| skips what's installed (case-insensitive) | re-running is safe (**idempotent**) |
| reads `.txt` (with `#` comments) or `extensions.json` (with `//` comments) | your own list or a repo's recommendations |

The core is in [extensions.py](../extensions.py); the explanation is in
[CONCEPTS.md](CONCEPTS.md).

### PowerShell

```powershell
code --list-extensions > extensions.txt                        # export
Get-Content extensions.txt | ForEach-Object { code --install-extension $_ }   # install each line
```

`ForEach-Object` runs the block once per line, with the line in `$_`.

### bash (Linux, macOS, Git Bash)

```bash
code --list-extensions > extensions.txt
xargs -L 1 code --install-extension < extensions.txt
```

`xargs -L 1` runs the command once per input line, with the line added as
its argument.

### Node.js

```js
// install-list.mjs: node install-list.mjs extensions.txt
import { readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
const ID = /^[A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9][A-Za-z0-9-]*(@\d+(\.\d+){0,3})?$/;
for (const id of readFileSync(process.argv[2], "utf8").split(/\r?\n/).map(s => s.trim()).filter(Boolean)) {
  if (!ID.test(id)) throw new Error(`bad id: ${id}`);
  execFileSync("code", ["--install-extension", id], { stdio: "inherit", shell: process.platform === "win32" });
}
```

On Windows, Node needs `shell: true` to run a `.cmd` file at all. That's
exactly why the id check comes first.

**The one-liners trust the file.** Use them on lists you wrote yourself.

## 5. Per project: recommendations

A repo can suggest extensions to everyone who opens it.
`.vscode/extensions.json` (this repo has one):

```jsonc
{
  // VS Code suggests these when someone opens this repo.
  "recommendations": [
    "ms-python.python",
    "charliermarsh.ruff",
    "davidanson.vscode-markdownlint",
  ]
}
```

It's **JSONC** (JSON with comments and trailing commas), which is why
`extensions.py` strips those before parsing. Create one with the command
**Extensions: Configure Recommended Extensions (Workspace Folder)**. A
recommendation only *suggests*: nothing installs without you.

Dev containers can install extensions automatically, in
`.devcontainer/devcontainer.json` under `customizations.vscode.extensions`.

## 6. Per workflow: profiles

A **profile** is a named set of extensions and settings. For example: a
"Rust" profile with rust-analyzer and CodeLLDB only, and a "Docs" profile
with markdownlint only. Fewer active extensions means a faster editor and
less code running.

- Create: Settings (gear) → **Profiles** → **New Profile**
- Use from the CLI: `code --profile Rust .`
- Share: export a profile to a file or a GitHub gist, and import it elsewhere

## 7. Offline: VSIX files

A `.vsix` file is the extension package itself, a **zip** file holding
`extension/package.json` and the code. Install it with
`code --install-extension ./name.vsix` or **Extensions: Install from VSIX**.
**Auto-update is turned off** for extensions installed this way, so update
them by hand.

## 8. Updating and removing

- VS Code updates extensions automatically. `extensions.autoUpdateDelay` (default 12 hours) waits a while after a release first, which gives bad releases time to be caught. `extensions.autoCheckUpdates: false` stops the checks.
- `code --update-extensions` updates everything now.
- `code --uninstall-extension <id>` removes one. The folder under `~/.vscode/extensions/` is removed on the next start.

## 9. Exercises

1. `python main.py export mine.txt`, then open it. How many are helpers pulled in by other extensions (like the .NET runtime)?
2. Add `evil.ext & calc` to a copy of the list and run `python main.py install`. What stops it, and where in the code?
3. Make a "Docs" profile with only markdownlint and Even Better TOML. Open this repo with `code --profile Docs .`.
4. Download a `.vsix` from a Marketplace page (**Download Extension**), rename it to `.zip`, and read its `package.json`.

**Self-check:** why is `python main.py install` safe to run twice?

## References

### Official

- VS Code: [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) ✔ (CLI, VSIX, recommendations, auto-update), [Command line interface](https://code.visualstudio.com/docs/configure/command-line), [Profiles](https://code.visualstudio.com/docs/configure/profiles), [Dev Containers: extensions](https://code.visualstudio.com/docs/devcontainers/containers#_managing-extensions)
- `code --help` (VS Code 1.141, run locally) ✔
- Node.js: [`child_process.execFileSync`](https://nodejs.org/api/child_process.html#child_processexecfilesyncfile-args-options) ✔ (Windows `.cmd` files need a shell)
- PowerShell: [ForEach-Object](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/foreach-object); [xargs(1) manual](https://man7.org/linux/man-pages/man1/xargs.1.html)

### Other

- [JSON with Comments in VS Code](https://code.visualstudio.com/docs/languages/json#_json-with-comments)

### Further learning

- [VS Code: Settings Sync](https://code.visualstudio.com/docs/configure/settings-sync) (extensions follow you across machines)
