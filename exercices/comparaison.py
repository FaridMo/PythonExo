n=int(input("Entrez le premier entier\n"))
p=int(input("Entrez le deuxième entier\n"))
print("vous avez saisi {} et {}\n".format(n,p))
if n<p:
    print("{} est plus petit que {} :".format(n,p))
elif n==p:
    print("{} et {} sont égaux".format(n,p))
else:
    print("{} est plus grand que {}".format(n,p))
