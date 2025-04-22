filename = "output.txt"
user_input = input("Enter some data to write to the file: ")
with open(filename, 'w') as file:
    file.write(user_input + "\n")
additional_data = input("Enter additional data to append: ")
with open(filename, 'a') as file:
    file.write(additional_data + "\n")
print("\nFinal content of the file:")
with open(filename, 'r') as file:
    for idx, line in enumerate(file, start=1):
        print(f"line{idx}:{line.strip()}")
