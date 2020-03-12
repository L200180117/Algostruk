from lat3 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(selft,nama,NIM,kota,us):
        """Metode inisiasi ini menutupimetode diclass Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM' + str(self.NIM)\
            + ', Tinggal di ' + self.kotaTinggal\
            + ', Uang Saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya,'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan smabil belajar."""
        print("Saya baru saja makan", s, "sambil belajar")
        self.keadaan = 'kenyang'
