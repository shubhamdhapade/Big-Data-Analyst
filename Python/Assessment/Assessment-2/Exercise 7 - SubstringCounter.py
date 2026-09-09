'''
    Manual Substring Counter
    Write a program that prompts the user to enter a main text string and a substring. Count how many times 
    the substring appears in the main string without using Python's built-in .count() method.
    Sample Input:
    String = "banana"
    Substring = "an"
    Sample Output: 2
'''

import os
def countString(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count
def main():
    string = input("Enter a string: ")
    substring = input("Enter substring: ")
    result = countString(string, substring)
    print("Substring Count:", result)
if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Manual Substring Counter':^80}")
    print("-" * 80)
    main()