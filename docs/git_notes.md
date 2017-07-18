Create git repository: **git init**
	
	* Creates the repository in the directory in which you are located!
	

	
Add a file from the working directory to the staging area
	
	**git add -filename**
	
	**git add filename1 filename2 ...**

Inspect the contents of the working directory and staging area
	
	**git status**

Check the location of a forked git repository
	
	**git remote -v**

Track differences between working project and staging area
	
	**git diff -filename-**

Commit the changes from the staging area to the repository
	
	**git commit -m "comment on changes made in present tense"**

Refer back to an earlier version of a project
	
	**git log**

In Git, the commit you are currently on is known as the HEAD commit.

	**git show HEAD**

	* In many cases, the most recently made commit is the HEAD commit.


# Restore the file in your working directory to look exactly as it did when you last made a commit.
git checkout HEAD filename

# Unstage a file from the staging area
git reset HEAD filename

# Rewind to the part before you made several mistakes
# This command works by using the first 7 characters of the SHA of a previous commit.
git reset SHA

# “which branch am I on?”
git branch

# Create a new git branch
git branch new_branch_name

# switch to the new branch
git checkout branch_name

# merging the branch into master
git merge branch_name

# Delete a branch after it has been integrated into master
git branch -d branch_name
