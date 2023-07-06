echo "This script will reset all this stuff."

read -p "Are you sure? [y/N] " -n 1 -r
echo
if [[ ! $REPLY == ^[Yy]$ ]]
then
    echo "project reset"
    rm -rf .git
    git init
    git add .
    git commit -m "chore: setup project"
    git checkout -b main
fi