# 12205, HS12MBR - Minimum Bounding Rectangle

# input
t = int(input())        # no. of test cases
n = [None] * t
objects_in_the_set = [None] * t

for i in range(t):
    n[i] = int(input())  # no. of objects in the set
    objects_in_the_set[i] = [None] * n[i]
    for j in range(n[i]):   # loop for every object in the set
        objects_in_the_set[i][j] = input()
    if i != t-1:
        empty = input()

# calculations
for i in range(t):      # every set
    points_per_object = [None] * n[i]
    # Boundary values per object
    for j in range(n[i]):   # every object in the set
        if objects_in_the_set[i][j][0] == "p":
            x, y, = map(int, objects_in_the_set[i][j][2:].split())
            points_per_object[j] = (x, y, x, y)
        elif objects_in_the_set[i][j][0] == "c":
            x, y, r, = map(int, objects_in_the_set[i][j][2:].split())
            points_per_object[j] = (x-r, y-r, x+r, y+r)
        elif objects_in_the_set[i][j][0] == "l":
            x, y, x1, y1 = map(int, objects_in_the_set[i][j][2:].split())
            points_per_object[j] = (min(x, x1), min(y, y1),
                                    max(x, x1), max(y, y1))

    # Boundary value of set
    for j in range(n[i]):   # every object in the set
        if j == 0:
            Boundary_values = list(points_per_object[j])
        if points_per_object[j][0] < Boundary_values[0]:
            Boundary_values[0] = points_per_object[j][0]
        if points_per_object[j][1] < Boundary_values[1]:
            Boundary_values[1] = points_per_object[j][1]
        if points_per_object[j][2] > Boundary_values[2]:
            Boundary_values[2] = points_per_object[j][2]
        if points_per_object[j][3] > Boundary_values[3]:
            Boundary_values[3] = points_per_object[j][3]
    output_string = str(Boundary_values)[1:-1].replace(",", "")
    print(output_string)
