# Libraries and built-ins

No external Python dependencies.

| Module / built-in | Where | What for | Why this |
| --- | --- | --- | --- |
| `re` | `extensions.py` | the id allow-list, trailing-comma removal | standard; one compiled pattern |
| `json` | `extensions.py` | parse `extensions.json` after removing comments | standard; never `eval` |
| `subprocess` | `main.py` | run `code` and the check tools | argument lists, explicit `check=` |
| `shutil.which` | `main.py` | find `code` (`code.CMD` on Windows) and the check tools | cross-platform `PATH` search |
| `pathlib.Path` | `main.py`, tests | files | object paths |
| `sys` | `main.py`, tests | argv, exit codes, `sys.path` | — |
| `unittest` | tests | test runner | standard |
| `input`, `set`, `len`, `isinstance`, `all`, `str.split` / `strip` / `lower` | core | prompting, lookups, checks | built-ins |
| `match` statement | `main.main` | command dispatch | a Python 3.10+ language feature |
| `__name__ == "__main__"` | `main.py` | run only when executed | standard idiom |

**External tools (not imported):** the `code` CLI; `ruff` and
[devtools](https://github.com/jericho3110/mr-factory-workspace/tree/main/packages/devtools) in the check gate.

## References

### Official

- [The Python Standard Library](https://docs.python.org/3/library/index.html)

### Further learning

- [Python Module of the Week](https://pymotw.com/3/)
