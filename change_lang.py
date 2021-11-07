import pyperclip
temp = pyperclip.paste()


Lang1 = "qwertyuiop[]asdfghjkl;'zxcvbnm,? .:"
Lang2 = ['ض','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','چ','ش','س','ی','ب','ل','ا','ت','ن','م','ک','گ','ظ','ط','ز','ر','ذ','د','پ','و','.',' ','?',':']


s = str(temp)

for i in temp:
    if Lang1.find(i) == -1:
        n = Lang2.find(i)
    else:
        n = Lang1.find(i)
    
    
    s = s.replace(i,Lang2[n])
pyperclip.copy(s)
