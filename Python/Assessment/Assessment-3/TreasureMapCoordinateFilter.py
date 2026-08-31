'''
    Treasure Map Coordinate Filter
    Scenario: You have a list of coordinate pairs representing suspected treasure locations on a map: 
    coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]. However, the treasure can only exist in the first quadrant of 
    the map (where both the X coordinate and Y coordinate are strictly greater than zero (i.e., x > 0 and y > 0)). 
    Write a program that uses a list comprehension to filter the list and print only the valid coordinates.

    Hardcoded Input: coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    Sample Output: [[12, 5], [15, 9]]
'''
import os

def filter_first_quadrant_coords(coords: list[list[int]]) -> list[list[int]]:
    # List comprehension filtering for x > 0 and y > 0
    return [[x, y] for x, y in coords if x > 0 and y > 0]

def main():
    coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6], [23, 34]]
    
    valid_coords = filter_first_quadrant_coords(coords)
    
    print(f"Original Coords: {coords}")
    print(f"Valid First-Quadrant Coords: {valid_coords}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Treasure Map Coordinate Filter ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)