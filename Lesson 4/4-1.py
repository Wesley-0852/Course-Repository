#============================================
#           LOOPS (   FOR   ;  WHILE  )
#============================================

#  Loops are how you repeat code without having to copy the same lines over and over
#  FOR LOOP = Used when you want to ITERATE over some sequence of values
#  WHILE LOOP = Used when you want to keep looping as long the condition stays True. 

#=======================================================================================
# range(5)                # 0, 1, 2, 3 ,4 (Note thet 5 is not printed, thats because, 
#                         # range will always start at 0 )
# for i in range(5):
#     print(i)
#===================================================================================

# range(1, 5)

# for i in range(1, 5):   #This will print 1, 2, 3, 4
#     print(i)
#===================================================================================    
#   NOW WE CAN ADD A 3rd PARAMETER --> STEP (step parameter)
#   This is how much the number changes each time
#   The default above was one. Meaning if we say step = 1, it will also look like 
#   1, 2, 3, 4      or      0, 1, 2, 3, 4

# range(1, 5, 2)  # Here the range is 1 - 5 but the step-parameter is 2. It will look like
                # 1, 3  (It will still not print 5, because that'll violate the code)

                # range(1, 6, 2) will print 1, 3, 5

range(1, 6, 2)

for i in range(1, 6, 2):
    print(i)
