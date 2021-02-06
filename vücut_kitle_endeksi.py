print(" Vücut Kitle Endeksi Hesaplama Programı ")

boy = float(input("Boy 'metre' (Örnek:1.75): "))
kilo = int(input("Kilo (kg):"))

endeks = kilo/(boy*boy)

if endeks <=18:
    print(" Zayıf Vücut Kitle Endeksi: {} ".format(endeks))

elif endeks >18 and endeks <=25:
    print(" Normal Kilolu Vücut Kitle Endeksi: {} ".format(endeks))

elif endeks >25 and endeks<40:
    print(" Ciddi Obez Vücut Kitle Endeksi: {} ".format(endeks))

elif endeks>40:
    print(" İleri Derecede Obez (Morbid Obez) Vücut Kitle Endeksi: {} ".format(endeks)) 
