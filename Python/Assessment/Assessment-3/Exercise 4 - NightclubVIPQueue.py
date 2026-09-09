'''
    Nightclub VIP Queue
    Scenario: A nightclub bouncer maintains a list of VIP guests who are allowed inside: ["Guido", "Esha", "Rajan", "Kishori"].
    As guests arrive at the door, the bouncer prompts the user to enter their name.

    If the guest is on the VIP list, move them from their current position in the queue and insert them at the front of the 
    queue (index 0).
    If the guest is not on the VIP list, print "Access denied. Not on the VIP list." and do not modify the list. Run this 
    program in a loop. The loop should stop when the user types "exit". Print the updated queue state after each guest 
    arrives.
    Sample Walkthrough:
    Current VIP queue: ['Guido', 'Esha', 'Rajan', 'Kishori']
    Enter guest name: Rajan
    Rajan moved to the front!
    Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

    Enter guest name: Vinod
    Access denied. Not on the VIP list.
    Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

    Enter guest name: exit
'''

import os
def process_vip_guest(vip_queue: list, guest_name: str) -> None:
    for i, name in enumerate(vip_queue):
        if name.lower() == guest_name.lower():
            moved_guest = vip_queue.pop(i)
            vip_queue.insert(0, moved_guest)
            print(f"{moved_guest} moved to the front!")
            return   
    print("Access denied. Not on the VIP list.")
def main():
    vip_queue = ["Guido", "Esha", "Rajan", "Kishori"]
    while True:
        print(f"\nCurrent VIP queue: {vip_queue}")
        guest_name = input("Enter guest name: ").strip()
        if guest_name.lower() == "exit":
            break
        if not guest_name:
            continue
        process_vip_guest(vip_queue, guest_name)
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Nightclub VIP Queue ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)