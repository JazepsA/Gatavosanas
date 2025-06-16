class Skolotajs:
   def __init__(self,uzvards):

      self.uzvards=uzvards
      self.tips=None

   def info(self):
      print(f"Skolotājs (tips={self.tips}) skolotājs {self.uzvards}")
   
class SakumskolasSkolotajs(Skolotajs):
   def __init__(self,uzvards,klase,st_sk_ned):
      super().__init__(uzvards)
      self.klase=klase
      self.ned= st_sk_ned
      self.tips=1

   def info_a(self):
      value = super().info()
      print(f"Sākumskolas {value}")
      return value
      

class Vidusskolasskolotajs(Skolotajs):
   def __init__(self,uzvards,pirm_prieks,otr_prieks,pirm_prieks_st,otr_prieks_st):
      super().__init__(uzvards)
      self.tips=3
      self.pir_prieks=pirm_prieks
      self.otr_prieks=otr_prieks
      self.pir_prieks_st=pirm_prieks_st
      self.otr_prieks_st=otr_prieks_st



   def info_v(self):
      a=super().info()
      print(f"Vidusskolas {a} māca šādus priekšmetus: {self.pir_prieks} un {self.otr_prieks} kopā {self.stundu_skaits} stundas  ")

   def stundu_sk(self):
      self.stundu_skaits=int(self.pir_prieks_st) + int(self.otr_prieks_st)
      
uzvards_s = input("Ievadiet sakumskolasskolotaja uzvardu: ")
klase= input("Ievadiet sakumskolas skolotaja klasi: ")
st_sk= input("Ievadiet skolotaju stundu skaitu: ")
uzvards_v = input("Ievadiet vidusskolas skolotāju uzvardu: ")
p_pr = input("Ievadiet pirmo skolotāju priekšmetu: ")
p_pr_sk = input("Ievadiet pirmo skolotāju priekšmetu stundu skaitu: ")
o_pr = input("Ievadiet otro skolotāju priekšmetu: ")
o_pr_sk = input("Ievadiet otro skolotāju priekšmetu stundu skaitu: ") 

a =SakumskolasSkolotajs(st_sk, uzvards_s, klase)
a.info_a()

b = Vidusskolasskolotajs(uzvards_v, p_pr, o_pr, p_pr_sk, o_pr_sk)
b.stundu_sk()
b.info() 


