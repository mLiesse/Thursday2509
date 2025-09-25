m = 7
# print(m**2)

def square(number):
    return number**2

# print(square(m))

def solve_pythagorean_triplets_z_limited(limit):
    """Finds all Pythagorean triplets (x, y, z) such that x^2 + y^2 = z^2 for z < limit."""
    solutions = []
    for z in range(1, limit):
        for x in range(1, z):
            for y in range(1, x+1):
                if x**2 + y**2 == z**2:
                    solutions.append((x, y, z))
        
    return solutions

def main():
    limit = 20
    print(solve_pythagorean_triplets_z_limited(limit))

if __name__ == "__main__":
    main()
