class CSDD:
    def __init__(self,zimols,modelis,reg_dat,masa,deg_veids):
        self.zimols=zimols
        self.modelis=modelis
        self.reg_dat=reg_dat
        self.masa=masa
        self.deg_veids=deg_veids

    def info(self):
        print(f" Zīmols: {self.zimols} \n Modelis: {self.modelis} \n Reģistrācijas datums: {self.reg_dat} \n Pilna masa: {self.masa} \n Degvielas veids: {self.deg_veids}")


a=CSDD("Audi","A5","12.12.2025","1200","B")

a.info()