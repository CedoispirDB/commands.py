def password(pw):
    right = False
    for k in str(pw):
        if k == "1" or k == "9" or k == "3" or k == "0":
            right = True
        else:
            right = False
            break
    if right:
        return True
    else:
       return False
