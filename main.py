
# Paste Signature Below
sig = "A1 ? ? ? ? C3 00 00 00 00 00 00 00 00 00 00 B8 ? ? ? ? 00 00 00 B0" 
newsig = "{ "
flag = False
for i in range(len(sig)-1):
    if flag:
        flag = False
        continue
    if sig[i] == "?":
        newsig = newsig + "-1,"
        continue
    if sig[i] == " ":
        newsig = newsig + " "
        continue
    newsig = newsig + "0x" + sig[i] + sig[i+1] + ","
    flag = True
newsig = newsig + "};"
print(newsig)

# newsig -> { 0xA1, -1, -1, -1, -1, 0xC3, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xB8, -1, -1, -1, -1, 0x00, 0x00, 0x00, 0xB0,};
