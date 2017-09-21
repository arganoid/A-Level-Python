input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

shift = 2
output = ""

for c in input:
    i = ord(c)
    if (c >= 'a' and c <= 'z'):
        i = (((i - ord('a')) + shift) % 26) + ord('a')

    output += chr(i)

print(output)
