#!/bin/bash

set -euo pipefail

# This script converts Terraform output to a digraph.

# Get the Terraform output.
output=$(terraform output)
#echo "${output}"

# Parse the output into a JSON object.
json_object=$(jq -r '.' <<< "$output")
echo "${json_object}"

# Create a new digraph.
digraph=$(dot -Tpng)

# Add nodes to the digraph.
for node in "${json_object[@]}"; do
  echo "$digraph \"$node\" [label=\"$node\"];"
  digraph="$digraph \"$node\" [label=\"$node\"];"
done

# Add edges to the digraph.
for edge in "${json_object[@]}"; do
  for dependency in "${json_object[$edge]}"
  do
    digraph="$digraph \"$edge\" -> \"$dependency\";"
  done
done

# Write the digraph to a file.
echo "$digraph" > digraph.dot

# Render the digraph as a PNG image.
dot -Tpng digraph.dot -o digraph.png
