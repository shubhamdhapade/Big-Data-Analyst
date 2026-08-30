'''
    Group Anagrams
    Write a program that starts with a list of strings defined at the top of your script 
    (e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams 
    (words formed by rearranging letters) together. Print the final grouped list of lists.
    Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
'''
import os
def groupAnagrams(words):
    result = []
    used = []
    for i in range(len(words)):
        if( words[i]) in used:
            continue
        group = []
        for j in range(i, len(words)):
            if words[j] in used:
                continue
            if sorted(words[i]) == sorted(words[j]):
                group.append(words[j])
                used.append(words[j])
        result.append(group)
    return result
def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(words)
    print("Grouped Anagrams:", result)
if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Group Anagrams ':^80}")
    print("-" * 80)
    main()