#!/usr/bin/env bash
set -e
if [[ -d ./.git ]]; then
	echo "Repo exists"
       exit
fi
mkdir .git
pushd .
cd .git
printf "[global]\n\tbare=false\n" > config
mkdir objects
mkdir -p refs/heads
echo "ref: refs/heads/master" > HEAD
popd 
