class kubs:
      #metode, kas inicializē objektu - konstruktors 
   def __init__(self,garums,krasa):
      if garums>=2 and garums <=10:
         self.garums = garums
      else:
         print("Malas garums neatbilst nosacījumiem!")
         self.garums = 2
      self.krasa = krasa
   
   #metode, kas aprēķina kuba tilpumu 
   def aprekinat_tilpumu(self):
      tilpums = self.garums**3
      return tilpums
   
   #metode, kas nodzēš objektu
   def __del__(self):
      print("Objekts ir likvidēts! Krāsa bija", self.krasa)


#objekti
kubg = kubs(10,"zaļa")
kubr = kubs(1,"sarkana")

print(kubg.krasa,kubg.aprekinat_tilpumu())
print(kubr.garums)
#objekta kubr dzēšana 
del kubr 
#pārbauda vai kubr eksistē
try:
   print(kubr.garums)
except:
   print("Objekts neeksistē!")
print(kubg.garums)

#klase bloks, kas manto no klases kubs

class bloks(kubs):
   def __init__(self, garums, krasa,kubu_skaits,forma):
      super().__init__(garums, krasa)
      if kubu_skaits>= 1 and kubu_skaits<= 4:
         self.__kubu_skaits = kubu_skaits
      else:
         print("Nepareiza kubu skaita vērtība!")
         self.__kubu_skaits = 1
      self.nosaukums = str(self.krasa) + str(self.__kubu_skaits)
      formas_vertibas = [11,12,13,14,22]
      if forma not in formas_vertibas:
         print("Forma neatbilst nosacījumiem! ")
         self.derigums = 0
      else:
         self.derigums = 1

   def tilpums(self):
      kuba_tilpums = self.garums**3
      bloka_tilpums = kuba_tilpums*self.__kubu_skaits
      return bloka_tilpums
   
   def mainit_formu(self,jauna_forma):
         formas_vertibas = [11,12,13,14,22]
         if jauna_forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem! ")
            self.derigums = 0
         else:
            self.derigums = 1


      
#objektu veidošana

orange3 = bloks(5,"oranža",3,13)
print(orange3.nosaukums,orange3.tilpums())

blue5 = bloks(7,"zila",5,23)
print(blue5.nosaukums,blue5.derigums)
blue5.mainit_formu(12)
print(blue5.nosaukums,blue5.derigums)


