
rev=$(git rev-parse --short HEAD)

mkdir -p deployed_gh_pages/${rev}
cd deployed_gh_pages/${rev}

git init
git config user.name "Anselmos"
git config user.email "Github.com/Anselmos"

git remote add upstream "https://$GH_TOKEN@github.com/anselmos/Biking-Endorphines.git"
git fetch upstream
git reset upstream/gh-pages

cp ../../generate_pyreverse/* .

git add -A .
git commit -m "rebuild pages at ${rev}"
git push -q upstream HEAD:gh-pages
