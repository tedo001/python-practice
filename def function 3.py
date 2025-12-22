def subject(name,mark):
    if mark >101:
        return("enter crt mark")
    elif "tamil" in name:
        if mark>30 and mark<101:
            return("pass")
        else:
            return("fail")
    elif "english" in name:
        if mark>30 and mark<101:
            return("pass")
        else:
            return("fail")
    else:
        return("wrong entry")
print(subject( "tamil",100))
print(subject( "english",35))
print(subject( "math",20))
print(subject( "english",102))

