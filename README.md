# Ecommerce Automation

This repository contains Selenium-based automation for the Ecommerce demo site.

Contents:
- `pageObjects/` - Page object models
- `testCases/` - PyTest test cases and fixtures
- `utilities/` - Helpers (logger, config reader)
- `Reports/`, `Logs/`, `Screenshots/` - Outputs generated when tests run

How to push to a remote GitHub repository:
1. Create a new repo on GitHub named `Ecommerce Automation`.
2. Add the remote and push from this project:

```powershell
# replace <remote-url> with the repository HTTPS or SSH URL
git remote add origin <remote-url>
git branch -M main
git push -u origin main
```

If you want me to add the remote and push, provide the remote URL (and token if needed).