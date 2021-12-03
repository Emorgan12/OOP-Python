number_grid = [ [1, 2], [3, 4] ]

number_grid[0][1] = 99
print(number_grid[0][0])
print(number_grid[0][1])

for row in number_grid:
     for col in row:
          print(col)
          