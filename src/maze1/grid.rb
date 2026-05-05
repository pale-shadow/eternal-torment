# frozen_string_literal: true

require 'cell'

class Grid
  attr_reader :rows, :columns

  def initialize(rows, columns)
    @rows = rows
    @columns = columns
    @grid = prepare_grid # This will now find the method below
    configure_cells
  end

  def prepare_grid
    Array.new(rows) do |row|
      Array.new(columns) do |column|
        Cell.new(row, column)
      end
    end
  end

  def configure_cells
    each_cell do |cell|
      row = cell.row
      col = cell.column
      cell.north = self[row - 1, col]
      cell.south = self[row + 1, col]
      cell.west  = self[row, col - 1]
      cell.east  = self[row, col + 1]
    end
  end

  def [](row, column)
    return nil unless row.between?(0, @rows - 1)
    return nil unless column.between?(0, @grid[row].count - 1)
    @grid[row][column]
  end

  def each_row
    @grid.each do |row|
      yield row
    end
  end

  def each_cell
    each_row do |row|
      row.each do |cell|
        yield cell if cell
      end
    end
  end
def to_s
    # Top border of the entire maze
    output = "+" + "---+" * columns + "\n"

    each_row do |row|
      top = "|"
      bottom = "+"

      row.each do |cell|
        # If cell is nil (boundary safety), treat as a wall
        cell ||= Cell.new(-1, -1)

        body = "   " # Three spaces for the cell center
        
        # Draw East boundary (is there a link to the right?)
        east_boundary = cell.linked?(cell.east) ? " " : "|"
        top += body + east_boundary

        # Draw South boundary (is there a link below?)
        south_boundary = cell.linked?(cell.south) ? "   " : "---"
        bottom += south_boundary + "+"
      end

      output += top + "\n"
      output += bottom + "\n"
    end

    output
  end
end # THIS 'end' must be at the end of the file