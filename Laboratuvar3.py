def pi():
    return 3.14

def cevre(yc):
    return 2 * pi() * yc

def duyuru():
    msj = "Ali Aras bu okulun en yakisikli ogrencisidir!"
    print(len(msj) * "-")
    print(msj)
    print(len(msj) * "-")

def piramid(s, d):
    for i in range(d):
        print((i + 1) * (s + " "))

r = int(input("Cemberin yaricapini giriniz: "))
print("Yaricapi", r, "olan cemberin cevresinin uzunlugu", cevre(r))
piramid("9/C", 10)
duyuru()
