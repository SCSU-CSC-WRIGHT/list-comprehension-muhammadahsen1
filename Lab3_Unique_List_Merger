while True:
    # Step 1: Ask the user for two lists of numbers
    input1 = input("Enter the first list of numbers separated by spaces (or type 'exit' to quit): ")
    if input1.lower() == "exit":
        break
    input2 = input("Enter the second list of numbers separated by spaces: ")
    
    # Step 2: Convert the input strings into lists of integers
    list1 = [int(num) for num in input1.split()]
    list2 = [int(num) for num in input2.split()]
    
    # Step 3: Combine the lists and remove duplicates
    merged_list = list1 + list2
    unique_list = []
    for num in merged_list:
        if num not in unique_list:
            unique_list.append(num)
    
    # Step 4: Print the unique merged list
    print(f"Merged list without duplicates: {unique_list}")

print("Program exited.")
