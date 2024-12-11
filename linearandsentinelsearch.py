# Function for Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

# Function for Sentinel Search
def sentinel_search(arr, target):
    # Adding a sentinel value at the end of the array
    n = len(arr)
    arr.append(target)  # Sentinel value is set to the target
    
    i = 0
    while arr[i] != target:
        i += 1
    
    # If we found the target before the sentinel, return True
    if i < n:
        return True
    else:
        return False

# Main function
def main():
    # Taking the number of students from the user
    n = int(input("Enter the number of students who attended the training program: "))
    
    # Taking roll numbers of students as input from the user
    roll_numbers = []
    print(f"Enter {n} roll numbers of students who attended the training program:")
    for _ in range(n):
        roll_number = int(input(f"Enter roll number {_ + 1}: "))
        roll_numbers.append(roll_number)

    # Ask for roll number to search
    roll_number_to_search = int(input("\nEnter roll number to search: "))

    # Perform Linear Search
    print("\nUsing Linear Search:")
    if linear_search(roll_numbers, roll_number_to_search):
        print(f"Student with roll number {roll_number_to_search} attended the training program.")
    else:
        print(f"Student with roll number {roll_number_to_search} did not attend the training program.")

    # Perform Sentinel Search
    print("\nUsing Sentinel Search:")
    if sentinel_search(roll_numbers, roll_number_to_search):
        print(f"Student with roll number {roll_number_to_search} attended the training program.")
    else:
        print(f"Student with roll number {roll_number_to_search} did not attend the training program.")
main()