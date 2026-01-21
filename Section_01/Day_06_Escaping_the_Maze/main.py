# Day06_TreasureMap.py

# Create rows of the map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

# Combine rows into a 2D list (map)
map = [row1, row2, row3]

# Display initial map
print(f"{row1}\n{row2}\n{row3}")

# Ask user where to place treasure (columnRow)
position = input("Where do you want to put the treasure? Type columnRow (e.g., 23 for col2 row3): ")

# Convert input to row and column indices
col = int(position[0]) - 1
row = int(position[1]) - 1

# Place treasure
map[row][col] = "X"

# Display updated map
print(f"{row1}\n{row2}\n{row3}")
