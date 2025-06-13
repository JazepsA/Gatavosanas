class doktorats:
   def __init__(self):
      self.nosaukums= input("Ievadiet doktorāta nosaukumu: ")
      self.pac_sk= int(input("Ievadiet doktorāta pacientu skaitu: "))
      
   def izvada(self):
      print(f"Doktorāts {self.nosaukums} apkalpo {self.pac_sk} pacientus ")

   def saglaba(self):
      #a=input("Ievadiet doktorāta nosaukumu: ")
      #b=int(input("Ievadiet doktorāta pacientu skaitu: "))
      print(self.nosaukums)
      print(self.pac_sk)


pir= doktorats()

pir.saglaba()
pir.izvada()
