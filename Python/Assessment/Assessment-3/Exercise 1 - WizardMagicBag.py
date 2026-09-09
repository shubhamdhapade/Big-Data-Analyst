'''
    The Wizard's Magic Bag
    Scenario: A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. 
    When the wizard steps through a magic portal, two things happen:
    A new item enters the bag (prompts the user to input the item name to append to the end).
    The oldest item in the bag (at index 0) is dissolved and ejected. Write a program to simulate this portal 
    transition and print the final bag contents.
    Sample Input: (User inputs "amulet")
    Sample Output:
    Portal transition activated!
    Ejected oldest item: staff
    Current items in the magic bag: ['potion', 'spellbook', 'amulet']
'''
import os
def wizard_magic_bag(bag_items, new_item):
    ejected_item = bag_items.pop(0)
    bag_items.append(new_item)
    return ejected_item, bag_items
def main():
    append_item = input("Enter the item to append to the bag: ").strip()
    bag = ["staff", "potion", "spellbook"]
    print("Portal transition activated!")
    ejected_item, updated_bag = wizard_magic_bag(bag, append_item)
    print(f"Ejected oldest item: {ejected_item}")
    print(f"Current items in the magic bag: {updated_bag}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' The Wizard\'s Magic Bag ':^80}")
    print("-" * 80)
    main()