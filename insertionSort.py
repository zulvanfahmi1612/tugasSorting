
def ascAwal(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key <= data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
        print(data)

def ascAkhir(data):
    for i in reversed(range(1, len(data))):
        key = data[i-1]
        j = i
        while j <= len(data)-1 and key >= data[j]:
            data[j - 1] = data[j]
            j += 1
        data[j - 1] = key
        print(data)

def dscAwal(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key >= data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        print(data)

def dscAkhir(data):
    for i in reversed(range(1, len(data))):
        key = data[i-1]
        j = i

        while j <= len(data)-1 and key <= data[j]:
            data[j - 1] = data[j]
            j += 1
        data[j-1] = key
        print(data)

li = [10, 5, 7, 11, 5, 13, 2, 8]
li2 = [10, 5, 7, 11, 5, 13, 2, 8]
li3 = [10, 5, 7, 11, 5, 13, 2, 8]
li4 = [10, 5, 7, 11, 5, 13, 2, 8]

print("asc awal")
ascAwal(li)
print("dsc awal")
dscAwal(li2)
print("dsc akhir")
dscAkhir(li3)
print("asc akhir")
ascAkhir(li4)