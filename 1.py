hints = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = 'map'
def trans(words):
    for c in words:
        if c.isalpha():
            asc = (ord(c) + 2 - ord('a')) % (ord('z') - ord('a') + 1) + ord('a')
            print(chr(asc), end='')
        else:
            print(c, end='')
    print()
trans(hints)
trans(url)