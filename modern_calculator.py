import math

def modern_calculator():
    print("Welcome to the Modern Calculator! 🚀")
    print("You can type commands like:")
    print("  - add 5 and 3")
    print("  - multiply 10 by 2")
    print("  - square root of 16")
    print("  - 30 percent of 200")
    print("Type 'exit' to quit.\n")

    while True:
        command = input("Enter your calculation: ").lower()
        if command == "exit":
            print("Goodbye! 👋")
            break

        try:
            if "add" in command and "and" in command:
                nums = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
                print(f"Result: {sum(nums)}")
            elif "multiply" in command and "by" in command:
                nums = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
                print(f"Result: {nums[0] * nums[1]}")
            elif "square root of" in command:
                num = float(command.split()[-1])
                print(f"Result: {math.sqrt(num)}")
            elif "percent of" in command:
                nums = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
                print(f"Result: {nums[0] * nums[1] / 100}")
            else:
                print("Sorry, I didn't understand that. Try again!")
        except Exception as e:
            print(f"Error: {e}. Please check your input.")

modern_calculator()
