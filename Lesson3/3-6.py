#==========================================
#               NESTED CONDITIONALS - (IF STATEMENTS INSIDE OHER IF STATEMENTS)
#==========================================

is_logged_in = True
is_admin = False

if is_logged_in:
    print("user is logged in!")
    if is_admin:
        print("show admin panel")
    else:
        print("show regular dashboard")
else:
    print("Redirect login page")
