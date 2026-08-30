'''
    The Cargo Train Scanner
    Scenario: A train has wagons carrying different resources: ["coal", "iron", "gold", "coal", "timber", "coal"]. 
    The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type 
    (e.g., "coal" or "gold").
    Print the total number of wagons carrying that resource (using .count()).
    If the resource is on the train, print the index of the very first wagon carrying it (using .index()). 
    If it is not found, print "Resource not found on train!".
    Sample Input: "coal"
    Sample Output:
    Number of coal wagons: 3
    First coal wagon is at index: 0
    Sample Input: "oil"
    Sample Output: "Resource not found on train!"
'''
import os

def scan_cargo(train_cargo: list, resource: str):
    target = resource.strip().lower()
    count = train_cargo.count(target)
    if count > 0:
        first_index = train_cargo.index(target)
        print(f"Number of {target} wagons: {count}")
        print(f"First {target} wagon is at index: {first_index}")
    else:
        print("Resource not found on train!")

def main():
    train_cargo = ["coal", "iron", "gold", "coal", "timber", "coal"]
    user_resource = input("Enter a resource type to inspect: ")
    scan_cargo(train_cargo, user_resource)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' The Cargo Train Scanner ':^80}")
    print("-" * 80)
    main()