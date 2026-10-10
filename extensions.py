"""Pure logic for managing VS Code extensions from a list: parse, validate, plan.

No I/O to VS Code here; main.py runs the `code` command. That split keeps
this file testable without VS Code installed (functional core).
"""

import json
import re

# publisher.name, optionally @version. Letters, digits and hyphens only, so an
# id can never carry shell syntax: on Windows `code` is a .cmd batch file, and
# cmd.exe re-parses its arguments (see docs/SECURITY.md).
EXT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*\.[A-Za-z0-9][A-Za-z0-9-]*(@\d+(\.\d+){0,3})?$")
MAX_LIST_BYTES = 200_000


def validate(ext_id: str) -> str:
    """Return the id unchanged if it's well-formed; raise ValueError otherwise."""
    if not EXT_ID.fullmatch(ext_id):
        raise ValueError(f"not a valid extension id: {ext_id!r} (expected publisher.name[@version])")
    return ext_id


def base_id(ext_id: str) -> str:
    """`Publisher.Name@1.2` -> `publisher.name`: ids are case-insensitive."""
    return ext_id.split("@", 1)[0].lower()


def parse_txt(text: str) -> list[str]:
    """One id per line; `#` starts a comment; blank lines ignored."""
    ids = []
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            ids.append(validate(line))
    return ids


def strip_jsonc(text: str) -> str:
    """Remove // and /* */ comments outside strings, then trailing commas.

    VS Code's .vscode/extensions.json is JSON with comments (JSONC), which
    json.loads rejects.
    """
    out, i, n = [], 0, len(text)
    in_str = False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 1
            elif c == '"':
                in_str = False
        elif c == '"':
            in_str = True
            out.append(c)
        elif text.startswith("//", i):
            i = text.find("\n", i)
            i = n if i == -1 else i
            continue
        elif text.startswith("/*", i):
            end = text.find("*/", i + 2)
            i = n if end == -1 else end + 2
            continue
        else:
            out.append(c)
        i += 1
    # shortcut: this also edits ",]" inside strings; extension lists never contain that.
    return re.sub(r",(\s*[\]}])", r"\1", "".join(out))


def parse_recommendations(text: str) -> list[str]:
    """The `recommendations` array of a .vscode/extensions.json file."""
    data = json.loads(strip_jsonc(text))
    recs = data.get("recommendations", []) if isinstance(data, dict) else []
    if not isinstance(recs, list) or not all(isinstance(r, str) for r in recs):
        raise ValueError("recommendations must be a list of strings")
    return [validate(r) for r in recs]


def parse_list(name: str, text: str) -> list[str]:
    """Pick the parser by file name; refuse oversized input."""
    if len(text.encode("utf-8")) > MAX_LIST_BYTES:
        raise ValueError(f"{name} is larger than {MAX_LIST_BYTES} bytes")
    return parse_recommendations(text) if name.endswith(".json") else parse_txt(text)


def plan(wanted: list[str], installed: list[str]) -> tuple[list[str], list[str]]:
    """(to_install, already_installed), compared case-insensitively, order kept, duplicates dropped."""
    have = {base_id(i) for i in installed}
    to_install, present, seen = [], [], set()
    for ext in wanted:
        key = base_id(ext)
        if key in seen:
            continue
        seen.add(key)
        (present if key in have else to_install).append(ext)
    return to_install, present
