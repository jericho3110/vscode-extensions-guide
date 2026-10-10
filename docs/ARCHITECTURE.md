# Architecture

Mostly documentation, plus a small tool to install extensions from a list.

## Layout

```text
VSCode_Extensions_Guide/
├── main.py                 front door: list | export | install | check   (imperative shell: runs `code`)
├── extensions.py           functional core: validate, parse, plan        (no I/O, fully testable)
├── tests/                  11 unittest tests (no VS Code needed)
├── examples/               multi-language.txt: a starter list
├── .vscode/extensions.json this repo's own recommendations (a real example, also tested)
└── docs/                   the guide
```

## How `python main.py install FILE` flows

```text
main.install(path)
  ├─ parse_list(name, text)        .txt or JSONC → validated ids     (extensions.py)
  ├─ installed()                   code --list-extensions → validated ids
  ├─ plan(wanted, installed)       → to_install, already present      (extensions.py)
  ├─ print the plan, ask [y/N]     default no
  └─ for each id: code --install-extension <validated id>
```

## Design choices

| Choice | Alternatives | Why |
| --- | --- | --- |
| **functional core, imperative shell** | one script that parses and installs together | the risky part (validation) is pure and tested without VS Code |
| an allow-list regex for ids | escaping for `cmd.exe` | escaping batch-file arguments correctly is notoriously hard (BatBadBut); a strict allow-list is simple and provably safe |
| drive the `code` CLI | call the Marketplace API and unzip VSIX files ourselves | the CLI already verifies signatures and handles updates; reimplementing that would be less safe |
| a hand-written JSONC stripper | `json5` or `commentjson` packages | ~30 lines vs a dependency to vet; tested on real VS Code output |
| confirm before installing | install straight away | installing runs code with your rights: validate, show, confirm (default no) |
| `match` statement for the CLI | `argparse` | four tiny commands; `match` reads like the usage text. Switch to `argparse` when options grow |

## Principles used

- **Idempotency**: `install` skips what's present, so running it twice is safe (`plan`).
- **Fail closed**: one bad id stops the whole run before anything is installed.
- **YAGNI**: no uninstall-from-list, no sync, no Marketplace queries.

## References

### Official

- Python: [`match` statement tutorial (PEP 636)](https://peps.python.org/pep-0636/), [re](https://docs.python.org/3/library/re.html), [subprocess](https://docs.python.org/3/library/subprocess.html)

### Other

- Gary Bernhardt, [Functional Core, Imperative Shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell)

### Further learning

- [Exercism Python track](https://exercism.org/tracks/python)
