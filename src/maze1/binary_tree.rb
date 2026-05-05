# frozen_string_literal: true

class BinaryTree
  def self.on(grid)
    grid.each_cell do |cell| # Must be each_cell (no space)
      neighbors = []        # Must initialize this array
      neighbors << cell.north if cell.north
      neighbors << cell.east if cell.east

      neighbor = neighbors.sample
      cell.link(neighbor) if neighbor
    end
    grid
  end
end