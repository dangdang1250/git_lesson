```shell
git push -u origin LearningUnitTest
git init -bare

#                      --remove url
git remote add origin https://github.com/dangdang1250/learnShell.git

git clone https://github.com/dangdang1250/learnShell.git
git push --set-upstream origin master
git push -u origin master

git diff --cached --name-only # show add staged files, only give name
git ls-files -o  # -o 這個選項顯示沒有被git管理的所有文件包括在.gitignore裡面的。
#--exclude-standard 這個選項考慮.gitignore了。
```

```bash
#count the number of lines attributed to each author
git blame --line-porcelain <file's name> | sed -n 's/^author //p' | sort | uniq -c | sort -rn

git reset --hard # 1)Changed the HEAD 2)Updats files on disk
#當你做了一個commit但突然不想要了。但又想做原來但基礎上改。就可以做--soft reset
#git會把改動但文件拉回來。去掉那個commit，感覺實際工作中是很需要的
git reset --soft # 1)Changed the HEAD 2) Does not update files on disk
```

## move where?
- commit_hash
- HEAD~n
  - where n is a number (go back n commits)
- HEAD@{n}
  - where n is number (go back n commits)

## Stashing
- Stash is global
```
# 創建一個新的branch，apply stash{0} switch originalwork branch at the same time
git stash branch originalwork stash{0}
```

## Git rebase
1. finds the common commit of the two trees - point1
2. "saves" all the commits from point1 to the current HEAD
3. reset HEAD to commit or branch passed to the rebase command
4. applies all the commits from step2, one by one
理解rebase就是把當前branch的根，改成 rebased branch
比如：branch new; branch bugfix
在bugfix上做
git rebase new #就是把bugfix上的改動，一個一個apply到new 的改動上。然後把HEAD 移動到 bugfix上。

很靈活：可以rebase 很多commit as you wish
git rebase -i

但只能rebase你沒有push的改動。

## git branch basic
### -f, --force Reset <branchname> to <startpoint>
git branch -f master 1258f0d0aae
### -m, --move Move/rename a branch and the corresponding reflog
git branch -m 

## git push
- force-push will cause confilicts for other people

## reflog
```bash
git reflog
# find your hash
git reset --hard <hash number>
```

## Bisect
- git bisect automates history navigation
- Binary search on a range of commits

## You don't want to commit binary file
They can't be diff, so every time you commit a binary file, will create a copy, and waste space and will cause a lot of time

lfs stands for : large files storage
```bash
git lfs install
# check you repo before you commit
git lfs track '*.jpg'
# if you already has binary submitted

```

## git submodule
```bash
git submodule add <url>
```
## good place to see how git works
https://git-school.github.io/visualizing-git/