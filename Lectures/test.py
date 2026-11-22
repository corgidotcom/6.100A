mystr = " The quick brown fox jumped over the lazy dog "

def strToTuple(str):
    returnTuple = ()
    tempstr = " ".join(str.strip().split())
    count = 0
    for c in " ".join(str.strip().split()):
        count += 1
        if c == " ":
            returnTuple += (tempstr[:tempstr.find(c)],)
            tempstr = tempstr[tempstr.find(c)+1:]
        elif count == len(" ".join(str.strip().split())):
            returnTuple += (tempstr,)
    return returnTuple

print(strToTuple(mystr))