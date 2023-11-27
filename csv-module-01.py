Path = 'C:\\Users\\jessica.apolinar\\Documents\\google_stock_data.csv'
file = open(Path, "r", newline='')
lines = [line for line in file]

# No format
print(lines[0])
print(lines[1])

# With format
dataset = [line.strip().split(',') for line in open(Path, "r")]
print(dataset[0])
print(dataset[1])

file.close()
