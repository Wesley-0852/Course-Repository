#=========================================================================
#                  CREATING A LOOP WITH SIMPLE CONDITIONALS

#             combine LOOPS with ->  if   ,   elif   ,   else statements
#=========================================================================

# EXAMPLE:

for i in range(10):
    if i < 3:
        print(i, "is low")
    elif i < 7:
        print(i, "is medium")
    else:
        print(i, "is high")

#this will print the following:

# 0 is low
# 1 is low
# 2 is low
# 3 is medium
# 4 is medium
# 5 is medium
# 6 is medium
# 7 is high
# 8 is high
# 9 is high

