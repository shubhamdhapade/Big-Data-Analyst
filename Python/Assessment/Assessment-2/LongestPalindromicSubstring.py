'''
Longest Palindromic Substring
    Write a program that prompts the user to enter a text string and finds the longest substring within 
    it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, 
    print any one of them.
    Sample Input: "babad"
    Sample Output: "bab" (or "aba")
    Sample Input: "cbbd"
    Sample Output: "bb"
'''
import os
def isPalindromic(string):
    if string == string[::-1]:
        return True
    else:
        return False
def findLongestSubString(string):
    longestSubstring = ''
    for i in range(len(string)):
        for j in range(len(string)+1):
            substring = string[i:j]
            if isPalindromic(substring):
                if len(substring) > len(longestSubstring):
                    longestSubstring = substring
    return longestSubstring
def main():
    string = input("Enter a string : ")
    result = findLongestSubString(string.strip())
    if len(result) == 1 or len(result) == 0:
        print("No Palindromic Substring found!")
    else: 
        if len(result.strip()) == len(string.strip()) and result.strip() == string.strip():
            print("No longest Palindromic Substring is found but given string is a Palindromic.")
        else:
            print("Longest Palindromic SubString : ", result)
if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Longest Palindromic Substring ':^80}")
    print("-" * 80)
    main()