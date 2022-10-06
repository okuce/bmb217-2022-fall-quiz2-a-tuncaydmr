class Otobus:
    """Otobus bilet satis takip sinifi"""
    nereden:str=""
    nereye:str=""
    plaka:str=""
    bos_koltuk:int=0
    dolu_koltuk:int=0
    
    def __init__(self,nereden,nereye,plaka,bos_koltuk,dolu_koltuk):
        self.nereden =nereden
        self.nereye = nereye
        self.plaka = plaka
        self.bos_koltuk = bos_koltuk
        self.dolu_koltuk = dolu_koltuk
    

    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        
        for i in range(len(self.dolu_koltuk)):
            self.bos_koltuk -=1
        
        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        for i in range(len(self.dolu_koltuk)):
            self.dolu_koltuk -= 1
            

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print(f"{self.nereden},{self.nereye},{self.plaka},{self.bos_koltuk},{self.dolu_koltuk}")

