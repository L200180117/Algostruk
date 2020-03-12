from lat3 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIS,kota,us,lk=[]):
        """Metode inisiai ini menutupi metode inisiai di class Manusia."""
        self.nama = nama
        self.NIS = NIS
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = lk
    def __str__(self):
        s = self.nama + ', NIS ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang Saku Rp ' + str(self.uangSaku) \
            + ' tiap harinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIS(self):
        return self.NIS
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, k):
        self.kotaTinggal = k
    def tambahUangSaku(self, u):
        self.uangSaku += u
#4
    def ambilKuliah(self, ambil):
        self.listKuliah.append(ambil)
#5
    def hapusKuliah(self, hapus):
        for x in self.listKuliah:
            if hapus in self.listKuliah:
                self.listKuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")


