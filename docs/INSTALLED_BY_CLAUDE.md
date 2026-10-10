# Extensions Claude Code installed, and why

A log of every extension that Claude Code (the AI coding agent) installed on
this machine, with the reason, so you can review or undo each one. All were
installed from the command line (`code --install-extension <id>`), which
doesn't show VS Code's publisher-trust prompt, so each publisher was checked
first ([SECURITY.md](SECURITY.md)).

Undo any of them with `code --uninstall-extension <id>`.

## Contents

1. [October 10, 2026: language support for the side projects](#1-october-10-2026-language-support-for-the-side-projects)
2. [October 10, 2026: looks and fun](#2-october-10-2026-looks-and-fun)
3. [Turning the fun ones on](#3-turning-the-fun-ones-on)
4. [References](#references)

---

## 1. October 10, 2026: language support for the side projects

The side projects had grown to Rust, C, C++, Go, Java and C#, but VS Code
only had Python support. Without these, those files open as plain text: no
errors, no go-to-definition, no debugger.

| Extension (id) | Version | Publisher | Why | Used by |
| --- | --- | --- | --- | --- |
| rust-analyzer `rust-lang.rust-analyzer` | 0.3.3073 | the Rust project | Rust errors, types and completion as you type | Teto (`rust/shell`), Unstoppable Force (`rust/collide`) |
| clangd `llvm-vs-code-extensions.vscode-clangd` | 0.6.0 | LLVM | C/C++ errors and navigation from clang, the compiler the projects build with | Teto (`c/`, `cpp/physics`), Unstoppable Force (`cpp/floats`), Disk Cleanup |
| CodeLLDB `vadimcn.vscode-lldb` | 1.12.3 | Vadim Chugunov (open source) | a debugger for Rust and C/C++: breakpoints and variables | the same Rust and C/C++ code |
| Go `golang.go` | 0.56.1 | the Go team | Go language support (`gopls`), tests, debugging | Teto (`go/brain`) |
| Language Support for Java `redhat.java` | 1.56.0 | Red Hat | Java language server | Teto (`java/reminders`) |
| C# `ms-dotnettools.csharp` | 2.160.4 | Microsoft | C# language server; it also pulled in `ms-dotnettools.vscode-dotnet-runtime` | Teto (`csharp/Companion`) |
| Tauri `tauri-apps.tauri-vscode` | 0.2.9 | the Tauri project | checks `tauri.conf.json` and helps with Tauri commands | Teto (the desktop shell) |
| Ruff `charliermarsh.ruff` | 2026.86.0 | Astral (Ruff's makers) | shows the same `ruff check` problems the check gates catch, while you type | every Python project here |
| GitHub Actions `github.vscode-github-actions` | 0.32.3 | GitHub | checks workflow YAML and shows CI runs | Teto, mr-factory-workspace, Reddit_PTracker |

**Rule used to pick them:** made by the language's own team or a well-known
publisher, open source where possible, and doing something VS Code can't do
by itself ([TOP_EXTENSIONS.md](TOP_EXTENSIONS.md)).

## 2. October 10, 2026: looks and fun

Asked for: "an anime sprite or a pet, and VS Code better in general".

| Extension (id) | Version | What it adds | Safety notes | Links |
| --- | --- | --- | --- | --- |
| **Doki Theme** `unthrottled.doki-theme` | 88.1.18 | 88 colour themes based on anime characters (counted in this version's manifest); optional **stickers** (a character in the corner) and **wallpapers** | the themes are normal. Stickers and wallpapers work by **editing VS Code's own CSS files**, which makes VS Code show an "Unsupported" warning; a VS Code update erases them (run **Restore Assets**); remove them with **Remove Sticker/Background** *before* uninstalling | [Marketplace](https://marketplace.visualstudio.com/items?itemName=unthrottled.doki-theme) · [GitHub](https://github.com/doki-theme/doki-theme-vscode) |
| **VS Code Pets** `tonybaloney.vscode-pets` | 1.36.0 | small animated pets (cats, dogs, a fox, a rubber duck, …) living in a panel; throw a ball, add more pets | runs only inside its own webview panel; changes no VS Code files; MIT | [Marketplace](https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets) · [GitHub](https://github.com/tonybaloney/vscode-pets) |
| **Material Icon Theme** `pkief.material-icon-theme` | 5.39.0 | clear file and folder icons by type (`.rs`, `.go`, `Cargo.toml`, `docs/` …) | an icon theme: only pictures, no code that touches your files | [Marketplace](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) · [GitHub](https://github.com/material-extensions/vscode-material-icon-theme) |

Installing doesn't change anything you see. You choose when to turn each one on (§3).

## 3. Turning the fun ones on

Open the Command Palette with `Ctrl+Shift+P`, then:

| To | Type |
| --- | --- |
| pick an anime colour theme | **Preferences: Color Theme**, then choose a "Doki" theme (arrow keys preview them) |
| add a character sticker / wallpaper (edits VS Code's files, see §2) | **Doki-Theme: Install <Character>'s Sticker** / **…'s Wallpaper**, e.g. *Doki-Theme: Install Essex's Sticker* (type "Doki-Theme: Install" to see them all) |
| remove sticker and wallpaper | **Doki-Theme: Remove Sticker/Background** |
| start the pets | **Pet Coding: Start pet coding session**; add more with **Pet Coding: Spawn pet** |
| file icons | **Preferences: File Icon Theme** → **Material Icon Theme** |

Undo a theme by choosing your old one again (the default is **Dark Modern**).

## References

### Official

- VS Code: [Color themes](https://code.visualstudio.com/docs/configure/themes), [Extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) ✔ (CLI installs skip the publisher-trust prompt)
- [Doki Theme README](https://github.com/doki-theme/doki-theme-vscode) ✔ (assets modify VS Code's CSS; Remove/Restore commands); command names and theme count read from the installed `package.json` ✔
- [VS Code Pets README](https://github.com/tonybaloney/vscode-pets)

### Further learning

- [VS Code: Create a color theme](https://code.visualstudio.com/api/extension-guides/color-theme): make your own anime theme
