## good place to see how git works
- [Learning Git Branch](https://learngitbranching.js.org/?locale=en_US) the best  
- [Visualizing Git](https://git-school.github.io/visualizing-git/) practice place, play ground  
- [5 git fundamentals](https://medium.com/hackernoon/5-git-fundamentals-ded819a34cfe)  

## For windows
- Download https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh to local 
- Modify .bash_profile

```bash
green="\[\033[0;32m\]"
yellow="\[\033[0;33m\]"
blue="\[\033[0;34m\]"
purple="\[\033[0;35m\]"
reset="\[\033[0m\]"

# Change command prompt
source ~/git-prompt.sh

export GIT_PS1_SHOWDIRTYSTATE=1

# '\u' adds the name of the current user to the prompt
# '\$(__git_ps1)' adds git-related stuff
# '\W' adds the name of the current directory
export PS1="$purple\u$green\$(__git_ps1)$yellow \W $ $reset"
```
