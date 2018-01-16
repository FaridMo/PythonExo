c1={'a':'z','b':'e','c':'a','d':'w','e':'x','f':'s','g':'t','h':'i','i':'j','j':'l','k':'c','l':'y','m':'k','n':'p','o':'d','p':'b','q':'u','r':'m','s':'f','t':'n','u':'g','v':'o','w':'q','x':'h','y':'r','z':'v'}

c2={'a':'c','b':'p','c':'k','d':'o','e':'b','f':'s','g':'u','h':'x','i':'h','j':'i','k':'m','l':'j','m':'r','n':'t','o':'v','p':'n','q':'w','r':'y','s':'f','t':'g','u':'q','v':'z','w':'d','x':'e','y':'l','z':'a'}
print("Bienvenu dans notre programme de chiffrement par substitution \n")
a=input("Veuillez saisir le mot à chiffrer : \n")
chiffre=''
dechiffre=''

for i in a:
    chiffre+=c1[i]
print("Chiffré correspondant à votre mot est : \n")
print("*********    ", chiffre, "    *********")
print("--------------------------------------------\n")



for i in chiffre:
    dechiffre+=c2[i]
print("Dechiffré correspondant à votre chiffré est : \n")
print("*********    ", dechiffre, "    *********")
