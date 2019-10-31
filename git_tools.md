## git tools

### git describe
- This command finds the **most recent tag** is reachable from a commit
- Options **--tags** : only show annotated tags
- Options **--exact-match** : Only output exact match(a tag directly references the supplied commit)

- Base on this : we can create an alias to show head's most recent tag
```txt
# put this in .gitconfig [alias] both are good examples
    showtags=!git describe --exact-match --tags $(git log -n1 --pretty='%h')
    greentag="!git describe --tags --abbrev=0 $(git rev-list --tags --max-count=1) --exclude \"*FAIL*\""
```

### git rev-list
- The output is given in reverse chronological order by default.
```shell
# show SHA between $newrev and $oldrev
git rev-list $newrev..$oldrev
```

### git ls-files 
- Show information about files in the index and the working tree
  
## Other commands
```shell
git tag --points-at HEAD # will show all tags on the HEAD 

```