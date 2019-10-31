[core]
	longpaths = true
	preloadindex = true
	fscache = true
	excludesfile = ~/.gitignore_global

[color "diff"]
  meta = yellow bold ul  
  frag = cyan bold ul
  old = red bold  
  new = green bold 

[color "status"]  
  added = green bold  
  changed = yellow bold  
  untracked = red bold

[grep]
  break = true
  heading = true
  lineNumber = true

[alias]
  g = grep --extended-regexp --break --heading --line-number

[diff]
	tool = diffmerge
[difftool "diffmerge"]
	cmd = "C:/Program\\ Files/SourceGear/Common/DiffMerge/sgdm.exe" $LOCAL $REMOTE
	prompt = false

[merge]
	tool = kdiff3

[mergetool "kdiff3"]
	path = C:/Program Files/KDiff3/kdiff3.exe
	trustExitCode = false

[credential]
	helper = manager