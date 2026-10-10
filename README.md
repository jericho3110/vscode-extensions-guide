# VS Code Extensions Guide

The VS Code extensions worth having in a multi-language workspace (Python,
Rust, C/C++, Go, Java, C#, TypeScript), how extensions work underneath, every
way to install them (editor, CLI, Python, PowerShell, bash, Node), and how to
stay safe. Each extension links to its Marketplace page and its source code
or docs.

## Contents
- [Quick start](#quick-start)
- [Layout](#layout)
- [Checks](#checks)
- [Documentation](#documentation)
- [References](#references)

## Quick start

```bash
python main.py list                                 # what you have, with versions
python main.py export my-extensions.txt             # save it (e.g. before a new PC)
python main.py install examples/multi-language.txt  # shows the plan, asks [y/N]
python main.py install .vscode/extensions.json      # a repo's recommendations work too
```

Real run on this machine:

```text
$ python main.py install examples/multi-language.txt
16 already installed, 0 to install:
```

Needs Python 3.10+ and the `code` command on `PATH`. No packages to install.

## Layout

```text
main.py                  front door: list | export | install | check
extensions.py            validate ids, parse lists (txt / JSONC), plan installs
tests/                   11 unittest tests (no VS Code needed)
examples/                multi-language.txt: a starter list
.vscode/extensions.json  this repo's own recommendations
docs/                    the guide
```

## Checks

`python main.py check` runs unittest, `ruff check`, `devtools scan` (secrets,
personal data, dangerous patterns) and `devtools links --offline`.

## Documentation

| Doc | What's in it |
| --- | --- |
| [docs/TOP_EXTENSIONS.md](docs/TOP_EXTENSIONS.md) | **start here**: the top 10, picks by language and by job, what's installed here, what to skip |
| [docs/INSTALLING.md](docs/INSTALLING.md) | every way to install: editor, every CLI flag, Python / PowerShell / bash / Node scripts, recommendations, profiles, VSIX, updates |
| [docs/HOW_EXTENSIONS_WORK.md](docs/HOW_EXTENSIONS_WORK.md) | manifest, activation events, the extension host, language servers (LSP), debug adapters, files on disk |
| [docs/SECURITY.md](docs/SECURITY.md) | threat model, what the Marketplace does and doesn't protect, the Windows `.cmd` trap, checklist |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONCEPTS.md](docs/CONCEPTS.md) | how the tool is built; every Python feature it uses |
| [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md) | a reading order in five stages |
| [docs/LIBRARIES_AND_BUILTINS.md](docs/LIBRARIES_AND_BUILTINS.md), [docs/CONVENTIONS.md](docs/CONVENTIONS.md), [docs/GLOSSARY.md](docs/GLOSSARY.md), [docs/FILE_TYPES.md](docs/FILE_TYPES.md) | modules, rules, terms, file types |
| [CHANGELOG.md](CHANGELOG.md) | versions |

## References

### Official

- VS Code: [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace), [Extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security), [Extension API](https://code.visualstudio.com/api)

### Further learning

- [Claude Code plugin guide](https://github.com/jericho3110/claude-code-plugin-guide) (the same questions for Claude Code)

## License

[MIT](LICENSE)
