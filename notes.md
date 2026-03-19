# DevOps Journey

## Phase 1 — Linux, Git, Bash

### Commands learned so far

| Command | What it does |
|---|---|
| pwd | print current directory |
| cd ~ | go to home directory |
| ls -la | list all files including hidden |
| mkdir | create a new folder |
| cat | print file contents to terminal |
| sudo | run command as administrator |
| apt update | refresh list of available packages |
| apt install | install a package |
| ssh-keygen | generate SSH key pair |
| code . | open VS Code in current folder |

### Setup completed
- Ubuntu installed via WSL2
- Git installed and configured
- SSH key generated and added to GitHub
- VS Code installed and connected to WSL

## Git Workflow

### Branches
- main → production code, always stable
- feature branches → isolated work, never breaks main

### Professional Git flow
1. Create a feature branch
2. Make changes and commit
3. Push branch to GitHub
4. Open a pull request
5. Review and merge into main
6. Delete the feature branch

### Commands
| Command | What it does |
|---|---|
| git branch | list all branches |
| git checkout -b name | create and switch to new branch |
| git checkout main | switch back to main |
| git merge branch | merge branch into current branch |
| git branch -d name | delete a branch |
| git pull | fetch and merge remote changes |