def count_valid_triangles(input):
    counter = 0
    for chunk in triangles:
        for index in range(0, len(chunk), 3):
            triangle = sorted(chunk[index:index + 3])
            counter += (sum(triangle[:2]) > triangle[2])
    return counter


if __name__ == "__main__":
    with open('input.txt') as f:
        triangles = f.readlines()
    triangles = [list(map(int, triangle.split())) for triangle in triangles]

    nbr_valid_triangles = count_valid_triangles(triangles)
    print("Puzzle 1: {}".format(nbr_valid_triangles))

    triangles = zip(*triangles)  # rotate list
    nbr_valid_triangles = count_valid_triangles(triangles)
    print("Puzzle 2: {}".format(nbr_valid_triangles))
