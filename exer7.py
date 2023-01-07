c = input("Enter character:")
character={i+1:c[i] for i in range(len(c))}

luckyNumber=int(input("Enter lucky number:"))
size = int(input("Enter length:"))

dicts={1: [], 2: [], 3: [], 4: [], 5: [], 6: [(1, 2, 3)], 7: [(1, 2, 4)], 8: [(1, 2, 5), (1, 3, 4)], 9: [(1, 2, 6), (1, 3, 5), (2, 3, 4),]}

temp=dicts[luckyNumber]

for i in temp:
    print(character[i[0]]+character[i[1]]+character[i[2]])
