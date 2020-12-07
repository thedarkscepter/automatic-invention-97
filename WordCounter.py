string = input("enter your introduction")
cc = 0
wc = 1
for i in string:
    cc = cc+1
    if( i == ' '):
        wc = wc+1
print("number of words in the string: ")
print(wc)
print("number of characters in the string: ")
print(cc)