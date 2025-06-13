class Skolotajs:
   def __init__(self,st_sk_ned,uzvards):
      self.ned= st_sk_ned
      self.uzvards=uzvards
   
class SakumskolasSkolotajs(Skolotajs):
   def __init__(self,uzvards,pas_st_sk_kon_klase):
      super().__init__(uzvards)
      self.konklase=pas_st_sk_kon_klase
      skol_tips=1
   
   def izvada(self):
      print(f"Sākumskolas ")



Ievadiet sākumskolas skolotāja uzvārdu:
Ievadiet skolotāja klasi: 
Ievadiet skolotāja stundu skaitu: