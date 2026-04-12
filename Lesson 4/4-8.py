


numbers = [2,7,4,9,10,3]
count = 0

for n in numbers:
    if n > 5:
        count = count + 1

print(count)                    #? What this is doing, is it's counting the numbers that is higher than 5

                                #? It will print:
                                #*  3  (because in the list, 3 numbers are higer than 5)


#?                              We can also find the SUM of the numbers in a list:

numbers = [2, 4, 5, 7, 9, 4, 7, 4, 8, 7, 4]
total = 0

for n in numbers:
    total = total + n

print(total)

