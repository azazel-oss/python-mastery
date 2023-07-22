with open("../../Data/portfolio.dat", "r") as file:
    f = file.read()
    lines = f.strip().split("\n")
    result = 0.0
    for line in lines:
        arr = line.split(" ")
        result += int(arr[1]) * float(arr[2])
print(result)
