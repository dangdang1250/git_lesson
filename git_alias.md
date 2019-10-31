## git alias
- How to add alias use git config
```shell
git config --global alias.slog "log --submodule=diff"
```
```txt
# alias for daily use
st = status
sst = !git st && git submodule foreach 'git st || :'
br = branch
co = checkout

# for superproject && submoudle 
change-branches = "!f() { git branch -m $1 $2 && git submodule foreach \"git branch -m $1 $2 || :\"; }; f"

# for work but this is really good example for using git describe --tags
greentag = "!git describe --tags --abbrev=0 $(git rev-list --tags --max-count=1) --exclude \"*FAIL*\""
# show head's most recent tag
showtags=!git describe --exact-match --tags $(git log -n1 --pretty='%h')

# good to know alias
open = "!f() { REPO_URL=$(git config remote.origin.url); explorer ${REPO_URL%%.git}; }; f"
browse = !git open
save = !git add -A && git commit -m 'SAVEPOINT'
wip = commit -am "WIP"
undo = reset HEAD~1 --mixed
unstage = reset HEAD --

# for my personal project, this one will commit changes to previous commit, so if pushed, don't do this
caa = commit -a --amend -C HEAD

# for log display all examples
added = diff --cached --name-only
last = log -1 --name-only HEAD
lol = log --graph --decorate --pretty=oneline --all --abbrev-commit
hist = log --pretty=format:'%C(yellow)[%ad]%C(reset) %C(green)[%h]%C(reset) | %C(bold white)%s %C(yellow)%d%C(reset) %C(red){%an}%C(reset)' --graph --date=short

# other people's
ci = commit
da = diff --cached
ls = ls-files -m 
new = ls-files -o --exclude-standard
gone = ls-files -d
```
