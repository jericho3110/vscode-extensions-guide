# Learning path

| Stage | Read | Concepts | Exercise | Self-check |
| --- | --- | --- | --- | --- |
| 1 | [TOP_EXTENSIONS.md](TOP_EXTENSIONS.md) | what each extension adds, by language and by job | pick 3 you don't have and read their GitHub READMEs | why clangd *or* Microsoft C/C++, not both? |
| 2 | [INSTALLING.md](INSTALLING.md) §1–3 | ids, the CLI and its flags | `code --list-extensions --show-versions` | what does `--force` change? |
| 3 | INSTALLING §4–8 | scripted installs, recommendations, profiles, VSIX | export your list; make a profile | why is `install` safe to run twice? |
| 4 | [HOW_EXTENSIONS_WORK.md](HOW_EXTENSIONS_WORK.md) | manifest, activation, extension host, LSP, DAP | read Ruff's `package.json` | why don't 35 extensions slow the editor down? |
| 5 | [SECURITY.md](SECURITY.md), `extensions.py`, [CONCEPTS.md](CONCEPTS.md) | threat model, the `.cmd` trap, allow-lists | INSTALLING exercise 2 | why does a Python *list* of arguments not protect you from `cmd.exe` here? |

## References

### Official

- [VS Code documentation](https://code.visualstudio.com/docs)

### Further learning

- [VS Code: Introductory videos](https://code.visualstudio.com/docs/getstarted/introvideos)
