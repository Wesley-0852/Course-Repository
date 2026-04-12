
#!==================================================================
#?                          WHILE LOOPS
#!==================================================================

#*      a WHILE LOOP repeats as long as it's condition stays TRUE.
#*      The difference between WHILE and FOR LOOPS are that WHILE loops dont
#*      automatically moves on to the next value. You have to update the variales involved
#*      in the condition so that the LOOP can eventually stop.

#?      EXAMPLE:

counter = 0

while counter < 5:
    print(counter)
    counter = counter + 1