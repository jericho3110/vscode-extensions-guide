# Concepts (Python, in this repo's code)

| Concept | Where | Example | Gotcha |
| --- | --- | --- | --- |
| **regular expression as an allow-list** | `extensions.EXT_ID` | letters, digits, hyphens, one dot, optional `@1.2.3` | describe what's *allowed*; a list of what's forbidden always misses something |
| **`fullmatch`** | `validate` | `EXT_ID.fullmatch("a.b\nc.d")` is `None` | `re.match` with `$` accepts a trailing newline; `fullmatch` doesn't |
| **raising `ValueError`** | `validate`, `parse_list` | `raise ValueError(f"not a valid extension id: {ext_id!r}")` | `!r` shows the value with quotes, so hidden spaces and newlines are visible |
| **a tiny state machine** | `strip_jsonc` | `in_str` flips on `"`; comments are skipped only outside strings | an escaped quote (`\"`) must not end the string: the code copies the escaped character as-is |
| **`re.sub` with a group** | `strip_jsonc` | `re.sub(r",(\s*[\]}])", r"\1", text)` removes trailing commas | `\1` puts back what the group matched |
| **`match` / `case`** (3.10+) | `main.main` | `case ["install", file, *flags] if set(flags) <= {"--yes"}:` | `*flags` collects the rest; the `if` guard rejects unknown flags |
| **set operations** | `main.main`, `plan` | `set(flags) <= {"--yes"}` (subset); `key in have` | a set lookup is O(1); a list lookup is O(n) |
| **choosing the list to append to** | `plan` | `(present if key in have else to_install).append(ext)` | compact; fine for two targets, not more |
| **`input()` with a safe default** | `main.install` | `input("[y/N] ").strip().lower() != "y"` | anything except `y`, including Enter or end of input, means no |
| **`subprocess.run(check=...)`** | `main.py` | `check=True` raises if `code` fails | use `check=False` where the exit code *is* the answer (`check()`) |
| **`sys.exit("message")`** | `main.py` | prints to stderr and exits with code 1 | a string argument means failure, not success |
| **`encoding="utf-8-sig"`** | `main.install` | reads files saved with a BOM by Windows tools | plain `utf-8` would keep the BOM in the first id, failing validation |

## Exercises

1. Add `python main.py diff FILE`: print what's in FILE but not installed, and the other way round. Reuse `plan`.
2. Write a test proving `strip_jsonc` keeps `"a // b"` inside a string.
3. Replace the `match` in `main.py` with `argparse`. Which is clearer for four commands? For fifteen?

**Self-check:** why is `validate()` also called on the output of `code --list-extensions`?

## References

### Official

- [re](https://docs.python.org/3/library/re.html) ✔ (`fullmatch`), [PEP 634: structural pattern matching](https://peps.python.org/pep-0634/), [subprocess](https://docs.python.org/3/library/subprocess.html), [codecs: utf-8-sig](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig)

### Other

- [Python Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

### Further learning

- Real Python: [Regular expressions](https://realpython.com/regex-python/), [Structural pattern matching](https://realpython.com/structural-pattern-matching/)
