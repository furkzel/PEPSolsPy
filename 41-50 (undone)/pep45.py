def triangle_number_generator(n):
    for i in range(1, n+1):
        yield int(i*(i+1)/2)

def pentagonal_number_generator(n):
    for i in range(1, n+1):
        yield int(i*(3*i-1)/2)

def hexagonal_number_generator(n):
    for i in range(1, n+1):
        yield int(i*(2*i-1))

triangles = triangle_number_generator(100000)
pentagonals = pentagonal_number_generator(100000)
hexagonals = hexagonal_number_generator(100000)

triangles_set = set()
pentagonals_set = set()
hexagonals_set = set()

for i in range(100000):
    triangles_set.add(next(triangles))
    pentagonals_set.add(next(pentagonals))
    hexagonals_set.add(next(hexagonals))

print(triangles_set.intersection(pentagonals_set, hexagonals_set))

