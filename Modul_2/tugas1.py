class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumlahKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
#a
    def apakahTerkandung(self, h):
        if self.teks.find(h) == -1:
            return False
        else:
            return True
#b
    def hitungKonsonan(self):
        vokal=['b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n' 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        hitung=0
        for i in self.teks:
            if i not in vokal:
                hitung+=1
        return hitung
#c
    def hitungVokal(self):
        vokal=['a','i','u','e','o','A','I','U','E','O']
        hitung=0
        for i in self.teks:
            if i in vokal:
                hitung+=1
        return hitung
