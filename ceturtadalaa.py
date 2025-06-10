saraksts=[]

alfabets1 = "AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽ"

alfabets = list(alfabets1) 
a=0
while a>3:
    print(a)
    vards=input("Ievadiet vārdu: ")
    '''
    vai_pievienot = True
    print(saraksts)
    for i in range(3):
        if not(vards[0].isupper() and i.isalpha()):
            print("error")
            vai_pievienot = False
        else:
            
            if(vai_pievienot):
                burts=vards[0]
                for i in range(3):
                    if burts == alfabets[i] and saraksts[i] == []:
                        saraksts.insert(i,vards)
                        print(f"„Pievienoju vārdu {i} vietā")
                        break

    break    
    '''
    saraksts.append(vards)
    a+=1
    print(saraksts)
            

        