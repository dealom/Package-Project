def alpharight(pw,n=1):
    newpw = ""
    alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in pw:
        if l in alpha:
            l = alpha[alpha.index(l)+n]
        elif l in ALPHA:
            l = ALPHA[ALPHA.index(l)+n]
        newpw += l
    return newpw

def keyright(pw,n=1):
    newpw = ""
    alpha = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
    ALPHA = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM"
    for l in pw:
        if l in alpha:
            l = alpha[alpha.index(l)+n]
        elif l in ALPHA:
            l = ALPHA[ALPHA.index(l)+n]
        newpw += l
    return newpw
