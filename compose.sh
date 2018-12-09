#!/usr/bin/env bash

./git_init.sh

BLOB_ID=$(echo "blah blah" | python create_blob_object.py)
echo "Created blob with ID: $BLOB_ID"

TREE_ID=$(echo "100644,temp.txt,${BLOB_ID}" | python create_tree_object.py)
echo "Created tree with ID: $TREE_ID"

COMMIT_ID=$(python create_commit_object.py --tree-id ${TREE_ID} --msg "My Commit message" --name "matan" --email "a@b.com")
echo "Created commit with ID: ${COMMIT_ID}"
