# frozen_string_literal: true

require 'grid'
require 'binary_tree'

grid = Grid.new(10, 10) # Let's make it bigger to see the pattern!
BinaryTree.on(grid)

# This is the line that shows the output:
puts grid