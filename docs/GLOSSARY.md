# Glossary

| Term | Meaning | Explained in |
| --- | --- | --- |
| extension id | `publisher.name`, optionally `@version` | [INSTALLING §1](INSTALLING.md#1-the-extension-id) |
| Marketplace | Microsoft's catalog of VS Code extensions | [SECURITY §2](SECURITY.md#2-what-protects-you-and-what-doesnt) |
| VSIX | an extension package: a zip with `package.json` | [INSTALLING §7](INSTALLING.md#7-offline-vsix-files) |
| activation event | what makes VS Code start an extension | [HOW §3](HOW_EXTENSIONS_WORK.md#3-activation-lazy-loading) |
| contribution point | something an extension declares in `package.json` (commands, settings) | [HOW §2](HOW_EXTENSIONS_WORK.md#2-the-manifest-packagejson) |
| extension host | the Node.js process that runs extensions | [HOW §4](HOW_EXTENSIONS_WORK.md#4-the-extension-host-a-separate-process) |
| LSP | Language Server Protocol: one server per language, usable by any editor | [HOW §5](HOW_EXTENSIONS_WORK.md#5-language-servers-why-one-editor-fits-every-language) |
| DAP | Debug Adapter Protocol: the same idea for debuggers | [HOW §6](HOW_EXTENSIONS_WORK.md#6-debug-adapters) |
| recommendations | `.vscode/extensions.json`: what a repo suggests | [INSTALLING §5](INSTALLING.md#5-per-project-recommendations) |
| profile | a named set of extensions and settings | [INSTALLING §6](INSTALLING.md#6-per-workflow-profiles) |
| JSONC | JSON with comments and trailing commas | [INSTALLING §5](INSTALLING.md#5-per-project-recommendations) |
| Workspace Trust | VS Code's restricted mode for folders you haven't trusted | [SECURITY §2](SECURITY.md#2-what-protects-you-and-what-doesnt) |
| typosquatting | a look-alike name meant to trick you into installing it | [SECURITY §1](SECURITY.md#1-threat-model-extensions-are-code-with-your-rights) |
| BatBadBut | argument injection when running a Windows batch file | [SECURITY §3](SECURITY.md#3-the-cmd-batch-file-trap) |
| idempotent | running it twice has the same effect as running it once | [ARCHITECTURE](ARCHITECTURE.md#principles-used) |

## References

### Official

- [VS Code Extension API](https://code.visualstudio.com/api)

### Further learning

- [Language Server Protocol overview](https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/)
