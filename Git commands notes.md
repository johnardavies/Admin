# Git commands

## Adding and committing files

**within the repo initalise git**\
`$ git init`

**adds modified and new files to the index prior to committing**\
`$ git add .`

**commits changes that have been made, in this case called test commit**\
`$ git commit -m "test commit"`

**combines the add and the commit command in one line**\
`$ git commit -a -m "test commit"`

## Getting information

**produces a record of commits, type q to exit**\
`$ git log`

**See the files that have been added**\
`$ git diff --name-only --cached`

**shows files in last commit**\
`$ git diff-tree --name-only -r indexofcommit`

**gets the difference between two branches (branch 1 and branch 2) head**\
`$ git diff branch1..branch2`

**Lists the files that are being tracked in the master branch**\
`$ git ls-tree -r master --name-only`

**See the files committed in a branch (--name-only returns file names only, r goes into sub-folders)**\
`$ git ls-tree --name-only -r branch_name`

**Searches the git history**\
`$ git grep <regexp> $(git rev-list --all)` # git rev-list --all lists all the commit objects in reverse chronological order (The commit hashes)


## Undoing/Amending changes that have been made 

*git commit --amend to edit the last commit*

**Gives the opportunity to revise the last commit message or if you need to**\
**make further changes incorporate them into an updated version of the last commit**\
`$ git commit --amend`

**Change the commit message of the last commit that has not yet been pushed**\
`$ git commit --amend -m "New commit message."`

*git revert to undo an existing commit that has been made. It does not rewrite commit history*

**Reverts the commit with index indexofcommit**\
`$ git revert indexofcommit`

 *git reset to undo uncommited changes or commits in a private branch. Three different kinds of reset (mixed, soft and hard - mixed is the default)*

**Remove a file from the index that has been added, but not commited**\
`$ git reset manual_check_av.csv`

**Remove the changes in the last commit from the index, but keep them locally e.g. you just made a commit you don't like, but want to keep the work and fix the commit**\
`$ git reset --mixed HEAD~1`

**Keeps the files in the index and locally the same - changes show up as changes to be committed**\
`$ git reset --soft HEAD~1`

**Remove all of the change in the past commit, both locally and from the index (use with care)**\
`$ git reset --hard HEAD~1`

*git checkout undoes changes at the file level*

**Go back to the state after a past commit with commit hash abcd1**\
`$ git checkout abcd1`

**Undoes uncommited changes to a file permanently. It updates the working directory and not the indez**\
`git checkout -- file`

## Stashing

**Removes uncommited changes to a 'stash'**\
`$ git stash`

**Removes the changes from the stash and applies them to branch you are working on**\
`$ git stash pop`

## Working on branches

**Shows the current branch that is being worked on only**\
`$ git branch --show-current`

**lists the branches and which one is being worked on (if tag -a is added both local and remote branches listed. If tag -r remote branches only listed)**\
`$ git branch`

**branches the repo into a new branch**\
`$ git branch new_branch`

**branch off a previous commit**\
`$ git branch new_branch commit-id`

**switch to working on the new branch (If a -b tag is added you create the branch at the same time)**\
`$ git checkout new_branch`

**switch back to the previous active branch**\
`$ git checkout -`

**switch to working on a new branch branching off another branch**\
`git checkout -b new_branch branch_branched_off`

  **Selects specific commits e.g. commit1  commit2 from another branch and applies it to the branch you're on**\
`$ git cherry-pick commit1  commit2`

**Delete a branch (use with care)**\
`$ git branch -D branch_name`

**Visualising the branching**\
`$ git log --all --decorate --oneline --graph`

**Clone a specifc branch (the_branch_you_want) from a repo, rather than getting all the branches**\
`$ git clone -b the_branch_you_want --single-branch https://github.com/some_repo`

## Merging and rebasing branches

**Merging the banch feature into the branch main**\
`$ git checkout feature`
`$ git merge main`

**Adds in the features branch into the master branch (creates new commits to do so which are then added on top of main)**\
`$ git checkout feature`
`$ git rebase main`

## Which remote repo the local repo is linked to 

**Checks which online repos the local repo is linked with**\
`$ git remote -v`

**Changes the url of the remote repo that the local copy is linked to**\
`$ git remote set-url origin new.git.url/here`

## Interacting with the remote repo

**pulls the latest version from the remote repo if run from local repo**\
`$ git pull` (when a commit message is needed for this, press Esc then :wq , ctrl x and then ctrl c to exit the editor - if it's nano)

**pushes local changes to online repo where origin is the remote and main is the branch name**\
**If you have branched to a new branch and want to push that, main changes to the new branch name**\
`$ git push origin main`

**To set up a new branch upstream**\
`$ git push --set-upstream origin branch_name` or `$ git push -u origin branch_name`

**Merges remote changes with local changes**\
`$ git pull origin master`

**Merges the git commit history of two previously unrelated projects, pulling the main branch from the remote origin that has been set up to the local repo**\
`$ git pull origin main --allow-unrelated-histories`

## Deleting files and folders

**Removing a folder and its contents from git history (use carefully) --ignore-unmatch means it doesn't throw an error if no match -r deletes contents**\
`$  git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch filepath/folder' HEAD`

**Deleting the .git file so you can get rid of the repo  -r is recursive for subfolders -f is force (use with caution!)**\
`$ rm -fr .git`


