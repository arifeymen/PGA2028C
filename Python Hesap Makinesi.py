print("ISLEMLER\nToplama\nCikarma\nCarpma\nBolme\nBolum alma\nKalan alma")
islem = str(input("Islem adini giriniz: \n"))
say1 = int(input("Birinci sayiyi giriniz: \n"))
say2 = int(input("Ikinci sayiyi giriniz: \n"))
if islem == "Toplama":
  print(say1 + say2)
elif islem == "Cikarma":
  print(say1 - say2)
elif islem == "Carpma":
  print(say1 * say2)
elif islem == "Bolme":
  print(say1 / say2)
elif islem == "Bolum alma":
  print(say1 // say2)
elif islem == "Kalan alma":
     print(say1 % say2)
else:
    print("Gecerli bir islem giriniz!")
