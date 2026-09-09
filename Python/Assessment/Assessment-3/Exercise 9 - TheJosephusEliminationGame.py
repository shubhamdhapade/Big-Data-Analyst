'''
    Exercise 9: The Josephus Elimination Game
    Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every K-th soldier is eliminated from the circle. 
    The count continues with the next remaining soldier, moving clockwise. This process repeats until only one soldier remains. Write a program that prompts the user to enter 
    N(number of soldiers) and K (elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.

    Sample Input: N = 5, K = 2
    Sample Output:
    Soldier circle initialized: [1, 2, 3, 4, 5]
    Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
    Eliminated soldier: 4 (Remaining: [1, 3, 5])
    Eliminated soldier: 1 (Remaining: [3, 5])
    Eliminated soldier: 5 (Remaining: [3])
    The sole survivor is: 3
'''

def josephus_elimination_game(N, K):
    soldiers = list(range(1, N + 1))
    print(f'Soldier circle initialized: {soldiers}')
    current_index = 0

    while len(soldiers) > 1:
        # Calculate the index of the soldier to be eliminated
        current_index = (current_index + K - 1) % len(soldiers)
        eliminated_soldier = soldiers.pop(current_index)
        print(f'Eliminated soldier: {eliminated_soldier} (Remaining: {soldiers})')

    print(f'The sole survivor is: {soldiers[0]}')

if __name__ == "__main__":
    try:
        N = int(input("Enter the number of soldiers (N): "))
        K = int(input("Enter the elimination interval (K): "))
        if N <= 0 or K <= 0:
            raise ValueError("N and K must be positive integers.")
        josephus_elimination_game(N, K)
    except ValueError as e:
        print(f"Invalid input: {e}")