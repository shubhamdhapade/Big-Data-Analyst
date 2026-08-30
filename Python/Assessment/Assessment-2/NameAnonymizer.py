'''
    Name Anonymizer
    Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. 
    The output should print the initials of the first and middle names followed by the full last name. If the name consists 
    of only a single word, print it as-is.
    Sample Input: "Vinod Kumar Kayartaya"
    Sample Output: "V. K. Kayartaya"
    Sample Input: "Bangalore"
    Sample Output: "Bangalore"
'''
import os
def anonymizer(string):
    result = ''
    words = string.split()
    if len(words) == 1:
        result = words[0][0].upper() + words[0][1:].lower()
    else:
        for word in words[:-1]:
            result += word[0].upper() + ". "
        result += words[-1][0].upper() + words[-1][1:].lower()
    return result


def main():
    string = input("Enter a string: ")
    result = anonymizer(string)
    print("Anonymized Name:", result)

if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Name Anonymizer ':^80}")
    print("-" * 80)
    main()