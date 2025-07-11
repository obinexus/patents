# Enable globstar for recursive matching
shopt -s globstar

# Remove all Zone.Identifier files
for file in **/*:Zone.Identifier; do
    if [[ -f "$file" ]]; then
        echo "Removing: $file"
        rm "$file"
    fi
done
