#Bir hava yolu firması en fazla 20 kilogram bagaj hakkı vermektedir. 20 kilogramdan sonraki her kilogram
#için 10 TL ek ücret almaktadır. Buna göre bagajı 20 kg ya da daha az olan yolculara “Herhangi bir ücret
#ödemeniz gerekmiyor.”; 20 kg’den fazla olanlar için de ne kadar ek ücret ödeneceğini hesaplayarak “Fazla
#bagaj için ….. TL ödemelisiniz.” çıktılarını veren kodu yazınız.
bagaj=int(input("BAGAJ KG="))
if bagaj<=20:
    print("EK BAGAJ ÜCRETİ YOKTUR")
else:
    fark=(bagaj-20)*10
    print("FAZLA ÖDEMENİZ  GEREKEN "+str(fark)+" TL'DİR.")