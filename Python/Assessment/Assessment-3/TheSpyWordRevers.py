'''
    The Spy's Word Reverser
    Scenario: A secret agent wants to send an encrypted message. The encryption rule is simple: reverse every word in the sentence, but keep the order of words unchanged. Write a program that prompts the user for a sentence, splits it, uses a list comprehension to reverse the letters of each word, and joins them back together.

    Sample Input: "Meet me at midnight"
    Sample Output: "teeM em ta thgindim
'''
import os

def spy_word_reverser(sentence: str) -> str:
    reversed_words = [word[::-1] for word in sentence.split()]
    return " ".join(reversed_words)

def main():
    user_input = input("Enter a secret sentence: ").strip()
    if not user_input:
        print("Empty sentence entered!")
        return
        
    encrypted_message = spy_word_reverser(user_input)
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' The Spy\'s Word Reverser ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)