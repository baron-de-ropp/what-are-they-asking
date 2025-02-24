ssh-copy-id -i ~/.ssh/github_actions.pub root@your.server.ip
# OR manually:
cat ~/.ssh/github_actions.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
