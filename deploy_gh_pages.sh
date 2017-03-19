
rev=$(git rev-parse --short HEAD)

if [ "$TRAVIS_BRANCH" != "master" ]
then
    echo "This commit was made against the $TRAVIS_BRANCH and not the master! No deploy!"
    exit 0
fi

mkdir -p deployed_gh_pages/${rev}
cd deployed_gh_pages/${rev}

git init
git config user.name "Anselmos"
git config user.email "Github.com/Anselmos"

git remote add upstream "https://$GH_TOKEN@github.com/anselmos/Biking-Endorphines.git"
git fetch upstream
git reset upstream/gh-pages

cp ../../generated_pyreverse/* .

git add -A .
git commit -m "rebuild pages at ${rev}"
git push -q upstream HEAD:gh-pages
