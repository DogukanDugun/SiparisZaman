

from datetime import datetime, timedelta,date



def teslimat():
    yil = input('siparis tarihi yılı')
    ay=input('siparis tarihi ay')
    gun = input('siparis tarihi gun')
    yil = int(yil)
    ay = int(ay)
    gun = int(gun)
    a = date(yil,ay,gun)
    true = True
    ucakkalkis =[]
    while true:
        ucakkalk=input("bu ay hangi günler ucak kalkacak//yeterli ise 0")
        ucakkalk=int(ucakkalk)
        if (ucakkalk == 0):
            true= False
        else:
            ucakkalkis.append(ucakkalk)
    ucakkalkis.sort()
    # print(ucakkalkis)
    siparishazirlik=input("siparisin hazırlık süresi")
    siparishazirlik=int(siparishazirlik)
    ulkedencikis=timedelta(days=siparishazirlik)+a
    # print(ulkedencikis)
    i = 0
    i2 = 0
    s = True
    while i<len(ucakkalkis):
        d = date(yil,ay,ucakkalkis[i])
        i2=i2+1
        if ulkedencikis<=d:
            print("siparis " + str(d) + " tarihindeki ucak ile çıkış yapacaktır")
            s= False
            i = i+100
        i=i+1
    if s:
        print("siparis " + str(date(yil,ay,ucakkalkis[0])) + " tarihindeki ucak ile çıkış yapacaktır")
    gumruk = input("siparişin ülkeye geldikten sonraki gübrük / kargo süresi")
    gumruk = int(gumruk)


    if s:
        bitis = date(yil, ay, ucakkalkis[0]) + timedelta(days=gumruk)
    else:
        bitis = date(yil, ay, ucakkalkis[i - 101]) + timedelta(days=gumruk)
    print("tahmini teslimant günü: " + str(bitis))

teslimat()

