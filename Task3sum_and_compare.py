def sum_and_compare():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Calculate the sum of the two numbers
    total = num1 + num2

    # Compare the sum with 100 and print the result
    if total >= 100:
        print(f"The sum is {total}, which is greater than or equal to 100.")
    else:
        print(f"The sum is {total}, which is smaller than 100.")


# Run the function
sum_and_compare()
