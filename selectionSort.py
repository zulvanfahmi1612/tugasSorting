list1 = [6, 8, 1, 2, 9, 7, 3, 5, 4]
d1 = [6, 8, 1, 2, 9, 7, 3, 5, 4]
d2 = [6, 8, 1, 2, 9, 7, 3, 5, 4]
d3 = [6, 8, 1, 2, 9, 7, 3, 5, 4]
d4 = [6, 8, 1, 2, 9, 7, 3, 5, 4]

def ascMin(data):
    print(data, "   ascmin")
    for outerLoop in range(len(data)-1):
        num = outerLoop

        for inn in range(outerLoop+1, len(data)):
            #print(outerLoop, inn)
            if data[num] > data[inn]:
                num = inn
        data[outerLoop], data[num]  = data[num], data[outerLoop]
        print(f"iterasi ke- {outerLoop + 1} = {data}")


def dscMax(data):
    print(data,"  dscmax")
    for outerLoop in range(len(data)-1):
        num = outerLoop

        for inn in range(outerLoop+1, len(data)):
            #print(outerLoop, inn)
            if data[num] < data[inn]:
                num = inn
        data[outerLoop], data[num]  = data[num], data[outerLoop]
        print(f"iterasi ke- {outerLoop + 1} = {data}")


def dscmin(data):
    print(data, "   dscmin")
    for outerLoop in reversed(range(1, len(data))):
        num = outerLoop

        for inn in reversed(range(outerLoop)):
            #print(outerLoop, inn)
            if data[num] > data[inn]:
                num = inn
        data[outerLoop], data[num] = data[num], data[outerLoop]
        print(f"iterasi ke- {len(data)-outerLoop} = {data}")


def ascMax(data):
    print(data, "   ascmax")
    for outerLoop in reversed(range(1, len(data))):
        num = outerLoop

        for inn in reversed(range(outerLoop)):
            #print(outerLoop, inn)
            if data[num] < data[inn]:
                num = inn
        data[outerLoop], data[num] = data[num], data[outerLoop]
        print(f"iterasi ke- {len(data)-outerLoop} = {data}")


def modifiedSelection(data):
    print(data, "   mod")

    for outerLoop in range(((len(data) // 2) + (len(data) % 2))):
        num1 = outerLoop
        num2 = len(data)-(outerLoop+1)
        print(f"iterasi ke- {outerLoop+1}")


        for inn in range(outerLoop + 1, len(data)-(outerLoop+1)):
            #print(num1, inn)
            if data[num1] < data[inn]:
                num1 = inn
        data[outerLoop], data[num1] = data[num1], data[outerLoop]
        print(f"minimal = {data}")

        for inn in reversed(range(outerLoop + 1, len(data)-(outerLoop+1))):
            #print("c", num2, inn)
            if data[num2] > data[inn]:
                num2 = inn
        data[outerLoop], data[num2] = data[num2], data[outerLoop]
        print(f"maksimal = {data}")



a = [5, 6, 4, 3, 7]
modifiedSelection(list1)
print("")
ascMin(d1)
print("")
ascMax(d2)
print("")
dscmin(d3)
print("")
dscMax(d4)