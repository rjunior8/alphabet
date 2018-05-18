import string

d1 = {}
l1 = []
l2 = []
l3 = []

alphabet = string.ascii_lowercase
counter = 0

for i in alphabet:
    counter += 1
    d1.update({str(counter) : i})

sequence = input("Enter with the sequence: ")
sequence = sequence.split(" ")

for n in sequence:
    if n in d1:
        l1.append(d1[n])
        l2.append(d1[n])

print("".join(l1))

while True:
    choice = input("Enter the letter(s) here: ")
    l3.append(choice)

    for j in choice:
        l2.remove(j)

    print(l3, "\t" + "".join(l2))
