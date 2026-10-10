# How VS Code extensions work

What an extension *is*, how VS Code decides when to run it, where it lives
on disk, and how one editor supports many languages.

## Contents

1. [An extension is a Node.js package](#1-an-extension-is-a-nodejs-package)
2. [The manifest: package.json](#2-the-manifest-packagejson)
3. [Activation: lazy loading](#3-activation-lazy-loading)
4. [The extension host: a separate process](#4-the-extension-host-a-separate-process)
5. [Language servers: why one editor fits every language](#5-language-servers-why-one-editor-fits-every-language)
6. [Debug adapters](#6-debug-adapters)
7. [On disk](#7-on-disk)
8. [Compared with Claude Code plugins](#8-compared-with-claude-code-plugins)
9. [Exercises](#9-exercises)
10. [References](#references)

---

## 1. An extension is a Node.js package

VS Code is built on Electron (Chromium + Node.js). An extension is a folder
with a `package.json` and JavaScript code, packaged as a `.vsix` (a zip).
Some extensions also bring native programs. rust-analyzer ships a
`server/` folder with the Rust-written language server, which is why its
folder name ends in `-win32-x64`: it's a platform-specific build.

## 2. The manifest: package.json

Real fields from the installed rust-analyzer and Ruff:

| Field | rust-analyzer | Ruff | Meaning |
| --- | --- | --- | --- |
| `main` | `./out/main` | `./dist/extension.js` | the code VS Code loads |
| `engines.vscode` | `^1.93.0` | `^1.91.0` | the oldest VS Code it supports |
| `activationEvents` | `workspaceContains:Cargo.toml`, ... | `onLanguage:python`, `workspaceContains:*.py`, ... | **when** to start it (§3) |
| `contributes` | `commands`, `configuration`, `keybindings`, `languages`, `grammars`, `taskDefinitions`, `problemPatterns`, ... | `configuration`, `commands` | what it adds to the editor, declared without running code |

**Contribution points** are declarative: VS Code can show an extension's
settings and commands from the manifest alone, before any of its code runs.

## 3. Activation: lazy loading

An extension's code runs only when one of its **activation events** happens:

| Event | Example | Meaning |
| --- | --- | --- |
| `onLanguage:<id>` | `onLanguage:python` | a file of that language is opened |
| `workspaceContains:<glob>` | `workspaceContains:Cargo.toml` | the opened folder has such a file |
| `onCommand:<id>` | — | the user runs one of its commands (now implied by `contributes.commands`) |
| `onStartupFinished` | — | shortly after startup, without slowing it |
| `*` | — | always, at startup (discouraged: slows everyone down) |

That's why 35 extensions don't make the editor slow: opening a Markdown
file never starts rust-analyzer. It's the **lazy initialization**
pattern, the same idea as a Python import inside a function.

## 4. The extension host: a separate process

```text
 VS Code window (renderer process: the UI)
      │  RPC messages
      ▼
 Extension host (a Node.js process)  ── runs every extension's JavaScript
      │  stdio / sockets
      ├──► rust-analyzer server (native process)
      ├──► clangd (native process)
      ├──► gopls, Pylance, Ruff server, Java server ...
```

Extensions don't run in the UI process, so a slow or crashing extension
can't freeze the editor. They also **don't run in a sandbox**: the official
docs say *"The extension host has the same permissions as VS Code itself"*.
It can read and write files, use the network and start processes. See
[SECURITY.md](SECURITY.md).

## 5. Language servers: why one editor fits every language

Before 2016, every editor needed its own plugin for every language
(*M editors × N languages*). The **Language Server Protocol** (LSP) fixed
that: one **server per language** speaks JSON-RPC, and any editor that
speaks LSP can use it (*M + N*).

| Language | Server | Written in | Brought by |
| --- | --- | --- | --- |
| Python | Pylance (types), Ruff (lint/format) | TypeScript / Rust | `ms-python.vscode-pylance`, `charliermarsh.ruff` |
| Rust | rust-analyzer | Rust | `rust-lang.rust-analyzer` |
| C/C++ | clangd | C++ | `llvm-vs-code-extensions.vscode-clangd` |
| Go | gopls | Go | `golang.go` |
| Java | Eclipse JDT LS | Java | `redhat.java` |
| C# | Roslyn | C# | `ms-dotnettools.csharp` |

Each server is written in (or for) its own language, by the people who know
it best. That's the multi-language idea from the side projects
(a separate process per language, talking over pipes), applied to the editor.
Claude Code uses the same servers through its LSP plugins.

## 6. Debug adapters

Debugging uses a sibling protocol, the **Debug Adapter Protocol** (DAP).
CodeLLDB is a debug adapter for LLDB (Rust, C, C++), and debugpy is one for
Python. `launch.json` in `.vscode/` tells VS Code which adapter to start.

## 7. On disk

| Path (Windows) | Contents |
| --- | --- |
| `%USERPROFILE%\.vscode\extensions\<publisher.name>-<version>[-platform]\` | each installed extension |
| `%USERPROFILE%\.vscode\extensions\extensions.json` | the registry: each id, version, source (`gallery` = Marketplace), whether it's pre-release or pinned |
| `.vscode/extensions.json` in a repo | that repo's recommendations (different file, same name) |

macOS and Linux use `~/.vscode/extensions`. `--extensions-dir` or the
`VSCODE_EXTENSIONS` environment variable change the location.

## 8. Compared with Claude Code plugins

| | VS Code extension | Claude Code plugin |
| --- | --- | --- |
| Package | `.vsix` zip with `package.json` | folder with `.claude-plugin/plugin.json` |
| Catalog | one central Marketplace (malware scan, signing) | any GitHub repo can be a marketplace |
| Runs code | always (it *is* code) | only hooks, servers, monitors, `bin/` |
| Starts | on activation events | at session start (hooks), or when Claude uses it |
| Sandbox | none: same rights as VS Code | none for hooks and servers |
| Auto-update | on by default | off by default for third-party marketplaces |

See the [Claude Code plugin guide](https://github.com/jericho3110/claude-code-plugin-guide).

## 9. Exercises

1. Open `~/.vscode/extensions/charliermarsh.ruff-*/package.json`. Which activation events would start it in a Markdown-only folder?
2. Run **Developer: Show Running Extensions** in this repo, then in a Rust repo. What's different?
3. Find which extension uses `*` (start always) among yours: search the `package.json` files for `"*"` in `activationEvents`.

**Self-check:** why can a crashing extension not freeze the editor's UI, and why does that not make it safe?

## References

### Official

- VS Code API: [Extension anatomy](https://code.visualstudio.com/api/get-started/extension-anatomy), [Activation events](https://code.visualstudio.com/api/references/activation-events), [Contribution points](https://code.visualstudio.com/api/references/contribution-points), [Extension host](https://code.visualstudio.com/api/advanced-topics/extension-host), [Extension manifest](https://code.visualstudio.com/api/references/extension-manifest)
- VS Code: [Extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) ✔ (same permissions as VS Code), [Extension Marketplace: common questions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_common-questions) ✔ (install location)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/), [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/)

### Other

- [VS Code: Language Server Extension Guide](https://code.visualstudio.com/api/language-extensions/language-server-extension-guide)

### Further learning

- [Your first extension](https://code.visualstudio.com/api/get-started/your-first-extension): build "Hello World" in 10 minutes
