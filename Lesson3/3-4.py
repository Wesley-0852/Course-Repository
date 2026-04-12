#=========================================
#       BOOLIAN OPERATORS (and ; or ; not)
#=========================================

# EXAMPLE:

is_member = True
purchase_total = 120

if is_member and purchase_total >= 100:             # The "and" means that both parts must be true 
    print("Discount Applies")                       # If either part is false, discount will NOT apply
else:                                             
    print("No Discount")

#=========================================================================================================    

has_coupon = False
is_vip = True
if has_coupon or is_vip:                            #The "or" means that only one or or both needs to be true
                                                    # If one part is false, the discount will still apply
                                                    #If none is true, no discount
    print("Discount Applies")
else:
    print("No Discount")