# Using a while loop with find (memory efficient for large directories)
find . -name "*:Zone.Identifier" -type f | while read -r file; do
    echo "Removing: $file"
    rm "$file"
done
