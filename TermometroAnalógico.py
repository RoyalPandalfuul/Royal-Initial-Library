negative = -273

positive = 5526

numbers = []

loop = int(input())

if loop == 0:
    print(0)
else:
    entry = input()

    StrEntry = entry.split(" ")

    for i in StrEntry:
        numbers.append(int(i))

    MaxNegative = negative
    MaxPositive = positive

    for i in numbers:
        if i > 0 and i < MaxPositive:
            MaxPositive = i
        if i < 0 and i > MaxNegative:
            MaxNegative = i
    if MaxPositive == 5526:
        MaxPositive = 0
    if (MaxNegative + MaxPositive +MaxPositive) == MaxPositive:
        print(MaxPositive)
    else:

        PositiveInd = 0
        NegativeInd = 0
        for i in range(NegativeInd,0):
            NegativeInd +=1
        for i in range(0,MaxPositive):
            PositiveInd +=1

        if PositiveInd > NegativeInd:
            print(MaxPositive)
        else:
            print(MaxNegative)
