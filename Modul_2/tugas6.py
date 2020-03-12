from lat3 import Manusia
import datetime
class SiswaSMA(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self,nama,NIS,kota,umur,us):
        """Metode inisiai ini menutupi metode inisiai di class Manusia."""
        self.nama = nama
        self.NIS = NIS
        self.kotaTinggal = kota
        self.umur = umur
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIS ' + str(self.NIS) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Berumur ' + str(self.umur) \
            + '. Uang Saku Rp ' + str(self.uangSaku) \
            + ' tiap harinya.'
        return s

    def tahunLahir(self):
        thnskr = datetime.datetime.now().year
        tl = thnskr - self.umur
        return tl

