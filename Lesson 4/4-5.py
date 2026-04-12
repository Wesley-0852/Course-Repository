#========================================================
#                   BREAK and CONTINUE
#========================================================

# Loop controll tools that change the FLOW of a loop while it's running

#   BREAK = Stop the loop entirely and the loop then end immediatly, and then
#   execution continues after the loop.

#   EXAMPLE: 

#for i in range(10):
#    if i == 5:                  #This will print the following:
#        break                   #0
#    print(i)                    #1
                                 #2
                                 #3
                                 #4


# for i in range(10): 

#     print(i)
#     if i == 5:
#         break
                            #If print is moved above the condition, it will look like:
                            # 0
                            # 1
                            # 2
                            # 3
                            # 4
                            # 5

#========================================================
#                   CONTINUE
#========================================================

for i in range(10): 
    if i == 5:
        continue
    elif i == 6:
        continue
    elif i == 8:
        continue
    print(i)