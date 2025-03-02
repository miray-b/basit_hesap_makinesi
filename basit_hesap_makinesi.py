def hesap_makinesi():

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")


    if islem == '+':
        sonuc = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sonuc}")
    elif islem == '-':
        sonuc = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sonuc}")
    elif islem == '*':
        sonuc = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sonuc}")
    elif islem == '/':
        if sayi2 == 0:
            print("Bölme işleminde ikinci sayı 0 olamaz! (!TANIMSIZ!)")
        else:
            sonuc = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {sonuc}")
    else:
        print("Geçersiz işlem!")

hesap_makinesi()

