alt_sinir = 1.0                #kokun bulundugu araligin alt ve ust siniri tanımlanır.
ust_sinir = 2.0
def f(x):                           #f(x) seklinde bir fonksiyon olusturur.
    return x**3 + 4*x**2 - 10
sayac = 0
for _ in range(4):                           # 4 iterasyon islemi gerceklesecek bicimde bir dongu olusturur
    kok = (alt_sinir + ust_sinir) / 2        #ara deger bulunur.
    fk = f(kok)
    if fk * f(alt_sinir) < 0:           #ara deger teoremi kullanilarak yeni ust sinir/alt sinir belirlenir.
        ust_sinir = kok
    else:
        alt_sinir = kok
    sayac+=1                         # her islem sonucunda kacinci iterasyon oldugunu kaydetmek icin sayaci 1 artirir.
print("4 iterasyon sonucunda kokun yaklasik degeri: {:.4f}".format((alt_sinir+ust_sinir)/ 2))
          #olusan sayiyinin float degiskeni yardimiyla virgulden sonraki 4 basamagi yazdirilir.