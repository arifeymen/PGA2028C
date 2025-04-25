ort = float(input("Ortalamanizi giriniz: "))
zayif = int(input("Zayif sayinizi giriniz: "))

if zayif == 0:
  if ort >= 85:
    print("Takdir Belgesi alarak sinifi gecmeye hak kazandiniz!")
  elif ort >= 70:
    print("Tesekkur Belgesi alarak sinifi gecmeye hak kazandiniz!")
  elif ort >= 50:
    print("Sorunsuz sekilde sinifi gecmeye hak kazandiniz!")
  else:
    print("Ortalama yukseltme sinavlarina giriniz!")
else:
  if ort >= 50:
    print("Sorumlu olarak sinifi gecmeye hak kazandiniz!")
  elif ort >= 25:
    print("Sorumluluk sinavlarina giriniz!")
  else:
    print("Lutfen sinifi tekrar ediniz!")
