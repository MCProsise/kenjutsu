import sys
def add_them_all(filename):
    sum = 0
    file = open("a.txt", "r")
    line = file.read()
    line.split(",")
    print (line.split(","))
    total = sum([int(num) for num in line.split(',')])
    print(total)
    return sum
if __name__ == "__main__":
    fname = sys.argv[1]
    print(f"Processing {fname}")
    print(add_them_all(fname))