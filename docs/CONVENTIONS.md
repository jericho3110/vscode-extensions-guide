# Conventions

| Topic | Rule |
| --- | --- |
| Code | Python 3.10+, standard library only, `ruff check` clean |
| Ids | `publisher.name`, copied from the Marketplace URL |
| Links | each extension gets its Marketplace page plus its source code or docs |
| Claims | versions and output come from `code` on this machine; behaviour from the official docs (✔ in References) |
| Data | no real user paths or account data: use `%USERPROFILE%` or `~` |
| Commits | made with [gitship](https://github.com/jericho3110/mr-factory-workspace/tree/main/packages/gitship), which runs `python main.py check` first |
| Versions | SemVer in [CHANGELOG.md](../CHANGELOG.md) |

## References

### Official

- [PEP 8](https://peps.python.org/pep-0008/), [Semantic Versioning](https://semver.org/)

### Further learning

- [How to Write a Git Commit Message](https://cbea.ms/git-commit/)
