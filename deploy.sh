#!/bin/bash
desc="book_push"
# read -p "Commit description: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push origin gh-pages
