def portfolio_cost(filename):
    result = 0.0
    with open(f"Data/{filename}", "r") as file:
        f = file.read()
        lines = f.strip().split("\n")
        for line in lines:
            arr = line.split(" ")
            result += int(arr[1]) * float(arr[2])
        pass
    return result


print(portfolio_cost("portfolio.dat"))
