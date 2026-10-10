"""Front door.

  python main.py list                      installed extensions with versions
  python main.py export [FILE]             save installed ids to FILE (default extensions.txt)
  python main.py install FILE [--yes]      install what FILE lists and you don't have yet
  python main.py check                     tests, ruff, security scan, links

FILE is a .txt (one id per line) or a .vscode/extensions.json.
"""

import shutil
import subprocess
import sys
from pathlib import Path

from extensions import parse_list, plan, validate

ROOT = Path(__file__).resolve().parent


def code_cli() -> str:
    exe = shutil.which("code")
    if not exe:
        sys.exit("`code` isn't on PATH. In VS Code: Command Palette > 'Shell Command: Install code command in PATH'.")
    return exe


def installed(show_versions: bool = False) -> list[str]:
    cmd = [code_cli(), "--list-extensions"] + (["--show-versions"] if show_versions else [])
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return [validate(line.strip()) for line in out.splitlines() if line.strip()]


def install(path: Path, yes: bool) -> int:
    wanted = parse_list(path.name, path.read_text(encoding="utf-8-sig"))
    to_install, present = plan(wanted, installed())
    print(f"{len(present)} already installed, {len(to_install)} to install:")
    for ext in to_install:
        print(f"  + {ext}")
    if not to_install:
        return 0
    # Extensions run with your user rights, so installing is opt-in, default no.
    if not yes and input("Install these? [y/N] ").strip().lower() != "y":
        print("Nothing installed.")
        return 1
    failed = 0
    for ext in to_install:
        # Each id was validated against EXT_ID above: no cmd.exe metacharacters can reach the .cmd shim.
        r = subprocess.run([code_cli(), "--install-extension", validate(ext)], check=False)
        failed += r.returncode != 0
    print(f"done: {len(to_install) - failed} installed, {failed} failed")
    return 1 if failed else 0


def check() -> int:
    steps = [("tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"])]
    for name, cmd in (("ruff", ["ruff", "check", "."]),
                      ("security", ["devtools", "scan"]),
                      ("links", ["devtools", "links", "--offline"])):
        if shutil.which(cmd[0]):
            steps.append((name, cmd))
        else:
            print(f"== {name}: SKIPPED ({cmd[0]} not on PATH)")
    results = {}
    for name, cmd in steps:
        print(f"== {name}: {' '.join(cmd)}")
        results[name] = subprocess.run(cmd, cwd=ROOT, check=False).returncode == 0  # the exit code is the answer
    print("\n" + "  ".join(f"{n}:{'ok' if ok else 'FAIL'}" for n, ok in results.items()))
    return 0 if all(results.values()) else 1


def main(argv: list[str]) -> int:
    match argv:
        case ["list"]:
            print("\n".join(installed(show_versions=True)))
            return 0
        case ["export", *rest] if len(rest) <= 1:
            target = Path(rest[0] if rest else "extensions.txt")
            target.write_text("\n".join(installed()) + "\n", encoding="utf-8")
            print(f"wrote {target}")
            return 0
        case ["install", file, *flags] if set(flags) <= {"--yes"}:
            return install(Path(file), yes="--yes" in flags)
        case ["check"]:
            return check()
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except (ValueError, OSError) as e:  # bad list file: say why, no traceback
        sys.exit(f"error: {e}")
