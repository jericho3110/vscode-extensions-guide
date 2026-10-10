# Top VS Code extensions for a multi-language workspace

Picked for a workspace that mixes Python, Rust, C/C++, Go, Java, C#,
TypeScript and Markdown docs, like the side projects here. Every extension
has its Marketplace page and its source code or docs, for further research.

**How they were picked:** made by the language's own team or a well-known
publisher, open source where possible, and doing something the editor can't
do alone. Versions are the ones installed on this machine in October 2026
(VS Code 1.141).

## Contents

1. [The top 10](#1-the-top-10)
2. [By language](#2-by-language)
3. [By job](#3-by-job)
4. [Installed on this machine](#4-installed-on-this-machine)
5. [Ones to skip or replace](#5-ones-to-skip-or-replace)
6. [References](#references)

---

## 1. The top 10

| # | Extension (id) | What it does | Why it's in the top 10 | Links |
| --- | --- | --- | --- | --- |
| 1 | **Python** `ms-python.python` | running, debugging, testing and environments for Python | the base every other Python tool plugs into | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python) · [GitHub](https://github.com/microsoft/vscode-python) · [Docs](https://code.visualstudio.com/docs/python/python-tutorial) |
| 2 | **Pylance** `ms-python.vscode-pylance` | fast type checking, completions, go-to-definition for Python | catches type mistakes as you type | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) · [GitHub (issues)](https://github.com/microsoft/pylance-release) |
| 3 | **Ruff** `charliermarsh.ruff` | Python linting and formatting, very fast | the same `ruff check` the check gates run, shown inline | [Marketplace](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) · [GitHub](https://github.com/astral-sh/ruff-vscode) · [Docs](https://docs.astral.sh/ruff/editors/) |
| 4 | **rust-analyzer** `rust-lang.rust-analyzer` | the official Rust language server: types, errors, refactors, inlay hints | Rust is hard to read without the types it shows | [Marketplace](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) · [GitHub](https://github.com/rust-lang/rust-analyzer) · [Docs](https://rust-analyzer.github.io/) |
| 5 | **clangd** `llvm-vs-code-extensions.vscode-clangd` | C/C++ language server from the LLVM project | uses the same compiler (clang) the projects build with, so errors match | [Marketplace](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd) · [GitHub](https://github.com/clangd/vscode-clangd) · [Docs](https://clangd.llvm.org/) |
| 6 | **CodeLLDB** `vadimcn.vscode-lldb` | a debugger for Rust and C/C++ (LLDB) | breakpoints and variable views for native code | [Marketplace](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) · [GitHub](https://github.com/vadimcn/codelldb) |
| 7 | **Go** `golang.go` | Go support from the Go team, with `gopls` | one extension for formatting, testing and debugging Go | [Marketplace](https://marketplace.visualstudio.com/items?itemName=golang.go) · [GitHub](https://github.com/golang/vscode-go) · [Docs](https://go.dev/doc/editors) |
| 8 | **Error Lens** `usernamehw.errorlens` | shows each error's message on the line itself | you see problems without hovering or opening a panel | [Marketplace](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) · [GitHub](https://github.com/usernamehw/vscode-error-lens) |
| 9 | **GitLens** `eamodio.gitlens` | who changed each line and why (blame), history, comparisons | answers "why is this code like this?" from the commit messages | [Marketplace](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) · [GitHub](https://github.com/gitkraken/vscode-gitlens) |
| 10 | **markdownlint** `davidanson.vscode-markdownlint` | style checks for Markdown | the docs are half of every project here | [Marketplace](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) · [GitHub](https://github.com/DavidAnson/vscode-markdownlint) |

Install all ten (and a few more) in one go:
`python main.py install examples/multi-language.txt` (see [INSTALLING.md](INSTALLING.md)).

## 2. By language

| Language | Extension (id) | Notes | Links |
| --- | --- | --- | --- |
| Python | Python Debugger `ms-python.debugpy` | installed automatically with Python | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) · [GitHub](https://github.com/microsoft/vscode-python-debugger) |
| Python | Python Environments `ms-python.vscode-python-envs` | create and switch virtual environments | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-python-envs) · [GitHub](https://github.com/microsoft/vscode-python-environments) |
| Python | Jupyter `ms-toolsai.jupyter` | notebooks inside VS Code | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) · [GitHub](https://github.com/microsoft/vscode-jupyter) |
| Rust | rust-analyzer | see the top 10 | |
| Rust | Dependi `fill-labs.dependi` | shows outdated or vulnerable versions in `Cargo.toml`, `package.json`, `requirements.txt`, `go.mod` | [Marketplace](https://marketplace.visualstudio.com/items?itemName=fill-labs.dependi) · [GitHub](https://github.com/filllabs/dependi) |
| C/C++ | clangd + CodeLLDB | see the top 10. Don't also enable Microsoft's C/C++ IntelliSense: the two fight over the same files | |
| Go | Go | see the top 10 | |
| Java | Language Support for Java `redhat.java` | Java language server (Eclipse JDT) | [Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.java) · [GitHub](https://github.com/redhat-developer/vscode-java) |
| C# | C# `ms-dotnettools.csharp` | C# language server; also installs the .NET runtime helper | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) · [GitHub](https://github.com/dotnet/vscode-csharp) |
| TypeScript | built in | VS Code ships TypeScript support; no extension needed | [Docs](https://code.visualstudio.com/docs/languages/typescript) |
| Tauri apps | Tauri `tauri-apps.tauri-vscode` | completions for `tauri.conf.json`, Tauri commands | [Marketplace](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) · [GitHub](https://github.com/tauri-apps/tauri-vscode) |
| TOML | Even Better TOML `tamasfe.even-better-toml` | `Cargo.toml`, `pyproject.toml`: validation, formatting | [Marketplace](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) · [GitHub](https://github.com/tamasfe/taplo) |
| YAML | YAML `redhat.vscode-yaml` | schema checks for GitHub Actions, Kubernetes and more | [Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) · [GitHub](https://github.com/redhat-developer/vscode-yaml) |

## 3. By job

| Job | Extension (id) | Links |
| --- | --- | --- |
| CI | GitHub Actions `github.vscode-github-actions`: edit workflows with checks, watch runs | [Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) · [GitHub](https://github.com/github/vscode-github-actions) |
| Data files | Rainbow CSV `mechatroner.rainbow-csv`: colours each column, SQL-like queries | [Marketplace](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) · [GitHub](https://github.com/mechatroner/vscode_rainbow_csv) |
| Notes in code | Todo Tree `gruntfuggly.todo-tree`: lists every `TODO`/`FIXME` | [Marketplace](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) · [GitHub](https://github.com/Gruntfuggly/todo-tree) |
| Containers | Container Tools `ms-azuretools.vscode-containers`: images, containers, Dockerfiles | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers) · [GitHub](https://github.com/microsoft/vscode-containers) |
| Dev environments | Dev Containers `ms-vscode-remote.remote-containers`: develop inside a container | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) · [Docs](https://code.visualstudio.com/docs/devcontainers/containers) |
| Kubernetes | Kubernetes `ms-kubernetes-tools.vscode-kubernetes-tools` | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools) · [GitHub](https://github.com/vscode-kubernetes-tools/vscode-kubernetes-tools) |
| AI coding | Claude Code `anthropic.claude-code`: the agent these projects were built with | [Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) · [Docs](https://code.claude.com/docs/en/vs-code) |
| AI coding | Cline `saoudrizwan.claude-dev`: an open-source coding agent | [Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) · [GitHub](https://github.com/cline/cline) |

## 4. Installed on this machine

`python main.py list` on October 10, 2026 (33 extensions). Grouped by what
they're used for; ★ marks the ones these projects use most.

| Group | Extensions |
| --- | --- |
| Python ★ | `ms-python.python@2026.8.0`, `ms-python.vscode-pylance@2026.4.1`, `ms-python.debugpy@2026.6.0`, `ms-python.vscode-python-envs@1.38.0`, `charliermarsh.ruff@2026.86.0` |
| Native ★ | `rust-lang.rust-analyzer@0.3.3073`, `llvm-vs-code-extensions.vscode-clangd@0.6.0`, `vadimcn.vscode-lldb@1.12.3` |
| Other languages | `golang.go@0.56.1`, `redhat.java@1.56.0`, `ms-dotnettools.csharp@2.160.4` (+ `ms-dotnettools.vscode-dotnet-runtime@3.2.0`, pulled in by C#), `tauri-apps.tauri-vscode@0.2.9` |
| Docs and config ★ | `davidanson.vscode-markdownlint@0.62.1`, `tamasfe.even-better-toml@0.21.2`, `redhat.vscode-yaml@1.24.0`, `mechatroner.rainbow-csv@3.24.1` |
| Everywhere ★ | `usernamehw.errorlens@3.29.0`, `eamodio.gitlens@19.3.0`, `gruntfuggly.todo-tree@0.0.226`, `fill-labs.dependi@1.20.0`, `github.vscode-github-actions@0.32.3` |
| Notebooks | `ms-toolsai.jupyter@2025.9.1` and its 4 helpers (keymap, renderers, cell tags, slideshow) |
| Containers | `ms-azuretools.vscode-containers@2.5.2`, `ms-vscode-remote.remote-containers@0.469.0`, `ms-kubernetes-tools.vscode-kubernetes-tools@1.4.1` |
| AI ★ | `anthropic.claude-code@2.1.295`, `saoudrizwan.claude-dev@4.1.23` |

The 9 added on October 10 for the multi-language projects: rust-analyzer,
clangd, CodeLLDB, Go, Java, C#, Tauri, Ruff, GitHub Actions.

## 5. Ones to skip or replace

| Instead of | Use | Why |
| --- | --- | --- |
| Microsoft C/C++ IntelliSense *and* clangd together | one of them (clangd here) | both index the same files and show duplicate errors |
| Pylint / Flake8 / isort / Black extensions | Ruff | Ruff does linting, import sorting and formatting in one fast tool |
| "Bracket Pair Colorizer" | the built-in setting `editor.bracketPairColorization.enabled` | now built into VS Code |
| "Auto Close Tag", "Path Intellisense"-style helpers | built-in features first | every extension is code running with your rights ([SECURITY.md](SECURITY.md)) |
| Two AI agents active at once | one at a time | they compete for the same edits and context |

## References

### Official

- VS Code: [Extension Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) ✔, [Python](https://code.visualstudio.com/docs/languages/python), [C++](https://code.visualstudio.com/docs/languages/cpp), [Rust](https://code.visualstudio.com/docs/languages/rust), [Go](https://code.visualstudio.com/docs/languages/go), [Java](https://code.visualstudio.com/docs/languages/java), [C#](https://code.visualstudio.com/docs/languages/csharp)
- Each extension's own page, linked in the tables above
- `code --list-extensions --show-versions` (run locally) ✔

### Other

- [Language Server Protocol: implementations](https://microsoft.github.io/language-server-protocol/implementors/servers/) (why one server per language)

### Further learning

- [VS Code tips and tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Rust in VS Code (rust-analyzer manual)](https://rust-analyzer.github.io/book/)
