from random import choices, randrange

print("Nan objektif aplikasyon sa se pou kreye espedo pou ou. Mesi deske ou chwazi aplikasyon si la a.")

akse = input(" Antre Non ou: ")
akse1 = input(" Antre Siyati ou: ")
val = randrange(0, 100)
User = akse + akse1
user1 = akse.split()
user2 = akse1.split()
Users = len(User)

print(" Non'w ak Siyati'w se : ", akse, akse1)

def moun(): 
    global u
    
    for i in user1:
        u =i[0]
        for i in user2:
            u+= i[0]
    users = u
    print(f" Kreyatyon Premye espedo a se: {users}{Users}")
    
    user = User.replace (" ","")
    print(" Kreyatyon Dezyem espedo a se:",user)    
    
    if akse > akse1:
        User1 = akse1.replace(" ","")
        Userr1 = User1[::-1]+"{}".format(val)
        print(" Kreyatyon Twazyem espedo a se: ",Userr1)
        
    if akse < akse1:
        use = akse.replace(" ","")
        usee = use[::-1]+"{}".format(val)
        print(" Twazyem espedo a se: ",usee)
        
        # Kreyasyon lis non an ak kantite karakte

    lis_non = [akse, akse1,  users+format(Users), user, Userr1]
    lis_non_kantie = [len(akse), len(akse1),  len (users+format(Users)), len(user), len(Userr1)]
    print(" Lis espedo yo se: ",lis_non)
    print(" Kantite karakte espedo yo se: ",lis_non_kantie)
    
    # choix non ki pa depase pi piti 7 karakte   
    nouvo_non = []
    
    for non in lis_non:
        if (len(non) <= 7):
            nouvo_non.append(non)
    print(" Lis espedo ki pa depase 7 karakte yo se: ",nouvo_non)
    
    # Kreyasyon fichye espedo yo avan chwa o aza a asosye avek non ki pa depase 7 karakte yo!
    espedo = open("ESPEDO.txt","a")
    
    espedo.write(f'Bonjou {akse} {akse1}, nou rekoni nan sevis nou an, nou deja jenere epsedo pou {(len(nouvo_non))} moun deja... \n\n')
    espedo.write(f'Lis espedo yo se: \n')
    espedo.write(f' {lis_non} \n')
    espedo.write(f"Kantite karakte espedo yo se: \n")
    espedo.write(f' {lis_non_kantie} \n')
    espedo.write('Lis espedo ki pa depase 7 karakte yo se: \n')
    espedo.write(f' {nouvo_non}\n')
    
    
    # Chwa o aza nan fiche espedo a se!
    chwa = choices(nouvo_non)
    print (' Chwa o aza nan fiche espedo a se: ',chwa)
    espedo.write('Chwa o aza nan fiche espedo a se: \n')
    espedo.write(f' {chwa} \n\n')  
    espedo.write(f'Mesi {akse} {akse1}, deske ou chwazi sevis jenerate espedo nou an!!!  \n\n')
    espedo.write(f'--------------------------------------------------------------------------------------------------------------- \n\n')
    
    # Winchel Sytle programming
moun()


