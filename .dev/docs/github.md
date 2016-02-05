# Github Setup

1. Create repository on Github.

- https://github.com/new

2. Create local repository.

    mkdir ~/projects/pug
    echo "# PUG" >> README.md
    git init
    git add README.md
    git commit -m "Adds README.md."

3. Configure Github as remote repository using tatwell SSH key.

    vim .git/config

- Add these settings (no indent). Not url with entry from ssh config file:

    [core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
    [remote "origin"]
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = git@github-tatwell:tatwell/pug.git
    [branch "master"]
        remote = origin
        merge = refs/heads/master
    [user]
        email = tatwell@gmail.com
        name = tatwell

4. Push first commit.

    git push origin master
