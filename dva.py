
class kubs:
    global statuss
    statuss = True
    def __init__(self,malas_garums,krasas_nosaukums):
        self.malas_garums=malas_garums
        self.krasas_nosaukums=krasas_nosaukums
        
    def aprekinat_tilpumu(self):
        if self.malas_garums in range(2,11):
            tilp=self.malas_garums**3
            print(f"{tilp} kubikcentimetri ")
        else:
            print("Kuba malas garums nav intervālā 2-10 cm.")
    
    def likvidesana(self):
        statuss= False
        print(f"Tiks dzēsts kubs, kura krāsa ir {self.krasas_nosaukums}.")

    def info(self):
        print(f"Kuba īpašības \n malas garums: {self.malas_garums} \n krasas nosaukums: {self.krasas_nosaukums} \n")


class bloks(kubs):
    def __init__(self,malas_garums,krasas_nosaukums,kubu_skaits,forma):
        super().__init__(malas_garums, krasas_nosaukums)
        self.forma = forma
        if kubu_skaits in range(1,5):
            self.__kubu_skaits= kubu_skaits
            self.krasas_nosaukums=str(self.krasas_nosaukums + str(self.__kubu_skaits))
            print(self.krasas_nosaukums)
        else:
            print("Neatbilst nosacījumiem!")
            self.__kubu_skaits= kubu_skaits
            self.krasas_nosaukums= str(self.krasas_nosaukums + str(self.__kubu_skaits))
            print(self.krasas_nosaukums)

    
    def nosaukums_funk(self):
        self.nosaukums = str(self.krasas_nosaukums + str(self.__kubu_skaits))
        print(self.nosaukums)

    def der_funk(self):
        if self.forma in [11,12,13,14,22]:
            self.derigums = 0 
            print(self.derigums)
        else:
            self.derigums= 1
            print(self.derigums)
    def tilpums(self):
        tilp=self.__kubu_skaits * self.malas_garums**3
        print(tilp)




kubr=kubs(1,"sarkans")

print(f" kubr malas garums: {kubr.malas_garums}")
kubr.likvidesana()
print(statuss)
if kubr.statuss == True:
    print("Objekts ir pieejams")
else:
    print("Objekts ir pieejams")

kubg=kubs(10,"zaļš")

#kubg.aprekinat_tilpumu()
print(f" kubg krāsu un tilpumu: {kubg.krasas_nosaukums}")
kubg.aprekinat_tilpumu()


print(f" kubg malas garums: {kubg.malas_garums}")

Objekt1=bloks(5,"oranžs",3,13)

Objekt1.nosaukums_funk()
Objekt1.tilpums()

Objekt2=bloks(7,"zils",5,23)

Objekt2.nosaukums_funk()
Objekt2.der_funk()

Objekt2.forma=12

Objekt2.nosaukums_funk()
Objekt2.der_funk()
