# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions: [SemVer](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-10-10

### Added
- Guide: the top 10 extensions for a multi-language workspace, picks by language and by job, the 33 installed on this machine, and ones to skip. Each links to its Marketplace page and its source or docs.
- How extensions work (manifest, activation, extension host, LSP, DAP, disk layout) and every way to install them (editor, CLI flags, Python, PowerShell, bash, Node, recommendations, profiles, VSIX).
- `extensions.py` + `main.py`: list, export, and install from a `.txt` or `.vscode/extensions.json` list, with a plan and a [y/N] prompt. 11 tests.

### Security
- On Windows, `code` is a `.cmd` batch file, so `cmd.exe` would act on `&` or `|` in an id. Every id is checked against a strict `publisher.name[@version]` pattern first. Pinned by `test_rejects_anything_cmd_exe_could_interpret`.
