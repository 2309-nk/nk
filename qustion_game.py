ulist=[]
user={}

lang = input("enter 1 for add user / signup")
lang = input("enter 2 for login")
lang = input("enter 3 for delete")

def swi(lang):
    if lang == "1":
        return signup
    elif lang == "2":
        return login
    else:
        return exit()


def signup():

    user['Username'] = input("enter user name")
    user['Email'] = input("Enter email address")
    user['Password'] = input("Enter Password")
    ulist.append(user)


def login():

    u_name = input("enter user name")
    u_email = input("enter Emial address")
    u_pass = input("enter password")

    for u in ulist:
        if(u['Username'] == u_name ):
            print(u['Username'])
        else:
            print("user does not exist")




