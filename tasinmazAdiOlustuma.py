class tasinmazAdi():
    def __init__(self, ilceAdi, mahalleAdi, adaNo, parselNo):
        self.ilceAdi = ilceAdi
        self.mahalleAdi = mahalleAdi
        self.adaNo = adaNo
        self.parselNo = parselNo

        if adaNo != 0:
            self.olusanTasinmazAdi = (ilceAdi + " İlçesi, " + mahalleAdi + " Mahallesi, " + str(adaNo) + " Ada " + str(
                parselNo) + " Parsel")
        else:
            self.olusanTasinmazAdi = (ilceAdi + " İlçesi, " + mahalleAdi + " Mahallesi, " + str(parselNo) + " Parsel")