# Soru5: Bir "Müşteri" sınıfı ve bir "Hesap" sınıfı oluşturun. "Hesap" sınıfının "Müşteri" sınıfından miras almasına 
# ve bir müşterinin banka hesap bilgilerini temsil etmesine izin verin.

# Müşteri Sınıfı Özellikleri:
# "isim" (müşteri adı)
# "soyadı" (müşterinin soyadı)
# "tc_identification" (müşterinin TC kimlik numarası)
# "telefon" (müşteri telefon numarası)
# Hesap Sınıfı Özellikleri:
# "müşteri" (Müşteri nesnesi)
# "hesap_numarası" (hesap numarası)
# "bakiye" (hesap bakiyesi)
# Müşteri Sınıf Yöntemi:
# "display_information()": Müşterinin adını, soyadını, TC kimlik numarasını ve telefon numarasını görüntüler.
# Hesap Sınıfı Yöntemleri:
# "deposit(self, amount)": Hesaba belirli bir miktar para yatıran bir yöntem.
# "money_check(self, amount)": Hesaptan belirli bir miktar para çeken bir yöntem. 
# Ancak, hesapta yeterli bakiye yoksa, işlem gerçekleşmemeli ve bir mesaj görüntülenmelidir.
# "display_balance()": Hesap bakiyesini görüntüleyen bir yöntem.
# Bu iki sınıfı oluşturun, ardından bir Müşteri nesnesi ve bir Hesap nesnesi oluşturun, 
# müşteri bilgilerini Hesap nesnesine ekleyin ve hesap işlemlerini gerçekleştirin ve sonuçları görüntüleyin.

class Customer:
    def __init__(self, naam, achternaam, digid, telephone):
        self.naam = naam
        self.anaam = achternaam
        self.digid = digid
        self.telepfone = telephone
    def display(self):
        print("Kalnt Informatie:")
        print(f"Klant Naam       : {self.naam}")
        print(f"Klant AchterNaam : {self.anaam}")
        print(f"Klant Digid      : {self.digid}")
        print(f"Klant Telephone  : {self.telepfone}")

class Account(Customer):
    def __init__(self, customer, account_number, evenwicht=0):
        super().__init__(customer.naam, customer.anaam, customer.digid, customer.telepfone)
        self.customer = customer
        self.account_number = account_number
        self.evenwicht = evenwicht

    def deposit(self, bedrag):
        if bedrag > 0:
            self.evenwicht += bedrag
            print(f"Gestort: {bedrag} €. Nieuw Evenwicht: {self.evenwicht} €.")
        else:
            print("Gestort bedrag moet positief zijn.")

    def money_check(self, hoeveelheid):
        # Method to withdraw money, if balance is sufficient
        if hoeveelheid <= self.evenwicht:
            self.evenwicht -= hoeveelheid
            print(f"Withdrew: {hoeveelheid} TL. New Balance: {self.evenwicht} €.")
        else:
            print("Insufficient funds. Transaction failed.")

    def display_balance(self):
        print(f"Account Balance: {self.evenwicht} €.")


klant1 = Customer("Necmi","Mert","123456789","0641055017")
print("---------- Klant Gegevens ----------")
klant1.display()

account = Account(klant1, "TR1234567890", 1000)
account.display_balance()
deposit = float(input("Geld Storten : "))
account.deposit(deposit)
withdraw = float(input("Geld Opnemen : "))
account.money_check(withdraw)