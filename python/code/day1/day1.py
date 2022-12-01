inpfile = open("../../input/day1/input.txt")

res = []

for e in inpfile.read().split("\n\n"):
    cal = e.split("\n")
    thesum = sum(list(map(int, cal)))

    res.append(thesum)

print("p1: " + str(sum(sorted(res)[-1:])))
print("p2: " + str(sum(sorted(res)[-3:])))
