class doktorats:
   def __init__(self,nosaukums,pac_sk):
      self.nosaukums= nosaukums
      self.pac_sk= pac_sk
      
   def ievade(self):
      self.nosaukums= input("Ievadiet doktorāta nosaukumu: ")
      self.pac_sk= int(input("Ievadiet doktorāta pacientu skaitu: "))


   def izvada(self):
      print(f"Doktorāts {self.nosaukums} apkalpo {self.pac_sk} pacientus ")




pir= doktorats("XXX",12)
pir.saglaba()
pir.izvada()

pur=doktorats("",1)
pur.ievade()
pur.izvada()


