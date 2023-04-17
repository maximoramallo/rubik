# define a 3D array for the cube
# white = 1, red = 2, blue = 3, orange = 4, green = 5, yellow = 6
# first sublist = face
# second sublist = (horizontal) line
# third sublist = tile
cube = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 
[[2, 2, 2], [2, 2, 2], [2, 2, 2]],
[[3, 3, 3], [3, 3, 3], [3, 3, 3]],
[[4, 4, 4], [4, 4, 4], [4, 4, 4]],
[[5, 5, 5], [5, 5, 5], [5, 5, 5]],
[[6, 6, 6], [6, 6, 6], [6, 6, 6]]]

# re-assing, three by three
# vertically, jumping to the nearest face above and below
cube[0][0][0] = cube[5][0][0]
cube[0][0][1] = cube[5][0][1]
cube[0][0][2] = cube[5][0][2]
# the above repeated up to 4 faces
# horizontally, jumping to the nearest face from right and left
cube[0][0][0] = cube[1][0][0]
cube[1][0][0] = cube[1][0][1]
cube[2][0][0] = cube[1][0][2]
# the above repeated up to 4 faces
