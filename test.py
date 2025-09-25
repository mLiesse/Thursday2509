import time

# m = 7
# print(m**2)

# def square(number):
#    return number**2

# print(square(m))

def solve_pythagorean_triplets_z_limited(limit:int) -> list[tuple[int]]:
    """Finds all Pythagorean triplets (x, y, z) such that x^2 + y^2 = z^2 for z < limit."""

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    else:
        start_time = time.time()
        solutions = []
        for z in range(1, limit):
            for x in range(1, z):
                for y in range(1, x+1):
                    if x**2 + y**2 == z**2:
                        solutions.append((x, y, z))
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return solutions
    
def solve_pythagorean_triplets_z_limited_bis(limit:int) -> list[tuple[int]]:
    """
    Finds all Pythagorean triplets (x, y, z) such that x^2 + y^2 = z^2 for z < limit.
    """

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    else:
        start_time = time.time()
        list = [(i,i**2) for i in range(1, limit)]
        solutions = []
        for (z,z_squared) in list:
            for (x,x_squared) in list:
                for (y,y_squared) in list[:x+1]:
                    if x_squared + y_squared == z_squared:
                        solutions.append((x, y, z))
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")    
        return solutions

def square_list(numbers: list[int]) -> list[int]:
    return [x**2 for x in numbers]

def add_list(list1: list[int], list2: list[int]) -> dict[tuple, int]:

    dictionary = {}
    for a in list1:
        for b in list2:
            dictionary[(a,b)] = a + b
    return dictionary

def pythagorean_triplets_smart(limit:int) -> list[list[int]]:
    """
    Finds all Pythagorean triplets (x, y, z) such that x^2 + y^2 = z^2 for z < limit more efficiently.
    """

    numbers = list(range(1, limit+1))
    squares = square_list(numbers)
    added_squares = add_list(squares, squares)

    solutions = []
    for key, value in added_squares.items():
        if value in squares:
            #print(value, key)
            solutions.append((int(key[0]**0.5), int(key[1]**0.5), int(value**0.5)))

    return solutions
        

def main():
    limit = 20
    #print(solve_pythagorean_triplets_z_limited(limit))
    #print(solve_pythagorean_triplets_z_limited_bis(limit))
    start_time = time.time()
    solutions = pythagorean_triplets_smart(limit)
    print(solutions)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
