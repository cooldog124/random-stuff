from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
#replace 1 with 0 to get more walls
#replace 0 with 1 to delete a wall
map = [
[1,1,1,1,1,1],
[1,1,0,1,1,1],
[1,1,1,1,1,1]]

grid=Grid(matrix=map)
#change coordinates to change starting point and the end point
start=grid.node(1,1)
end=grid.node(5,2)

finder=AStarFinder(diagonal_movement=DiagonalMovement.always)

path,runs,=finder.find_path(start,end,grid)

print(path)
print(str(runs)+" runs")
