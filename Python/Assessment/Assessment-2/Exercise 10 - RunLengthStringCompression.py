'''
    Run-Length String Compression
    Write a program that prompts the user to enter a text string and compresses it using run-length encoding 
    (listing character counts next to each repeated character). If the compressed string is not smaller in size than 
    the original string, print the original string.
    Sample Input: "aabcccccaaa"
    Sample Output: "a2b1c5a3"
    Sample Input: "abcd"
    Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")
'''

import os
def stringCompression(string):
    stringCompressionResult = ''
    count = 1
    for i in range(len(string)):
        if i + 1 < len(string) and string[i] == string [i+1]:
            count += 1
        else:
            stringCompressionResult += string[1] + str(count)
            count = 1
    if len(stringCompressionResult) < len(string):
        return stringCompressionResult
    else:
        return string
def main():
    string = input("Enter a string : ")
    result = stringCompression(string.strip())
    print("Compressed String : ", result)
if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Run-Length String Compression ':^80}")
    print("-" * 80)
    main()

