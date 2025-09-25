m = 7
# print(m**2)

def square(number):
    return number**2

# print(square(m))

def main(limit):
    solutions = []
    for z in range(limit):
        for x in range(z+1):
            for y in range(x,z):
                if x**2 + y**2 == z**2:
                    solutions.append((x, y, z))
        
    return solutions

#print(solve_pythagorean_triplets_z_limited(20))

if __name__ == "__main__":
    print(main(20))
