filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        print("Reading file content")
        for idx, line in enumerate(file, start=1):
            print(f"line{idx}:{line.strip()}")
except FileNotFoundError:
    print(f"error: The file '{filename}' was not found")
