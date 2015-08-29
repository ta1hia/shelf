#!/bin/bash
desc="auto book push"
# read -p "Commit description: " desc
git add js/data.js && \
git add -u && \
git commit -m "$desc" && \
git push origin gh-pages
