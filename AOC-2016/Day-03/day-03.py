if __name__ == "__main__":
    with open('input.txt') as f:
        triangles = f.readlines()
    triangles = [list(map(int, triangle.split())) for triangle in triangles]

    counter = 0
    for row in triangles:
        triangle = sorted(row)
        counter += (sum(triangle[:2]) > triangle[2])
    print("Puzzle 1: {}".format(counter))

    counter = 0
    triangles = zip(*triangles)  # rotate list
    for colomn in triangles:
        for index in range(0, len(colomn), 3):
            triangle = sorted(colomn[index:index + 3])
            counter += (sum(triangle[:2]) > triangle[2])
    print("Puzzle 2: {}".format(counter))
