#!/bin/bash

TARGET_DIR="/mnt/backup1/workspace/development/eternal-torment/static/images"
cd "$TARGET_DIR" || exit 1

echo "Fixing the mess and normalizing..."

# 1. First, strip the accidental double extensions (e.g., .jpg.jpg, .png.jpg)
# We do this before lowercasing so we catch the exact mess created.
for file in *.jpg.jpg *.png.jpg *.kra.jpg *.avif.jpg *.sh.jpg; do
    [ -f "$file" ] || continue
    mv "$file" "${file%.jpg}"
done

# 2. Now run the proper normalization
for file in *; do
    [ -f "$file" ] || continue
    
    # Skip the script itself
    [[ "$file" == "fix.sh" ]] && continue

    # Lowercase and replace spaces with underscores
    new_name=$(echo "$file" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

    # Standardize .jpeg to .jpg
    # This only replaces .jpeg if it exists at the end of the string
    new_name="${new_name/%.jpeg/.jpg}"

    # Rename if changed
    if [ "$file" != "$new_name" ]; then
        if [ -e "$new_name" ]; then
            echo "Collision: '$new_name' exists, skipping '$file'"
        else
            mv "$file" "$new_name"
            echo "Fixed: '$file' -> '$new_name'"
        fi
    fi
done

echo "Normalization complete. Files should be clean now."
