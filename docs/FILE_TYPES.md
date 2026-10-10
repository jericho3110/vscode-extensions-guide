# File types

| File | Why it exists |
| --- | --- |
| `*.py` | the tool and its tests |
| `*.md` | the docs |
| `examples/*.txt` | install lists: one id per line, `#` comments |
| `.vscode/extensions.json` | JSONC: this repo's recommended extensions (VS Code reads it) |
| `.gitignore` | keeps caches and virtual environments out of git |
| `.gitattributes` | normalizes line endings |
| `.gitship.json` | the check gitship runs before committing |
| `LICENSE` | MIT |
| `CHANGELOG.md` | what changed in each version |

Files VS Code itself keeps (not in this repo), such as the extensions folder
and its registry `extensions.json`, are in
[HOW_EXTENSIONS_WORK.md §7](HOW_EXTENSIONS_WORK.md#7-on-disk).

## References

### Official

- [gitattributes](https://git-scm.com/docs/gitattributes), [gitignore](https://git-scm.com/docs/gitignore)

### Further learning

- [choosealicense.com](https://choosealicense.com/)
