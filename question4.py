# Soru4: Python'da bir "Vehicle" sınıfı oluşturun. Bu sınıfın aşağıdaki özelliklere sahip olduğundan emin olun:

# Özellikler:
# "marka" (Aracın markası)
# "model" (Araç modeli)
# "yıl" (Aracın üretim yılı)
# Bir "Araç" sınıfı oluşturun ve ardından "Arazi Aracı" (SUV) ve "SporOtomobil" sınıfları olmak üzere 
# iki türetilmiş alt sınıf oluşturun.

# "Arazi Aracı" sınıfı, "Araç" sınıfından türetilmiştir ve ek olarak "dört tekerlekten çekiş" özelliğini ekler.
# "SportCar" sınıfının "Vehicle" sınıfından miras almasını sağlayalım ve bir "max_speed" özelliği ekleyelim.
# Her sınıfın bir örneğini oluşturun, özelliklerini belirleyin ve bu özellikleri görüntüleyen bir program yazın.

class Vehicle:
    def __init__(self, merk, model, jaar):
        self.merk   = merk
        self.model  = model
        self.jaar   = jaar
    def display(self):
        print("Voertuig Informatie")
        print(f"Voertuig Merk  : {self.merk}")
        print(f"Voertuig Jodel : {self.model}")
        print(f"Voertuig Jaar : {self.jaar}")


class OffRoad(Vehicle):
    def __init__(self, merk, model, jaar, vier_drive):
        super().__init__(merk, model, jaar)  
        self.vier_drive = vier_drive

    def display(self):
        super().display()  
        print(f"Vier Drive: {self.vier_drive}")


class SportsCar(Vehicle):
    def __init__(self, merk, model, jaar, max_sneel):
        super().__init__(merk, model, jaar)  
        self.max_sneel = max_sneel

    def display(self):
        super().display()  
        print(f"Max Sneel: {self.max_sneel} km/h")


voertuig = Vehicle("Honda","Civic",2021)
off_road_vehicle = OffRoad("Toyota","Raw4",2023,True)
sports_car = SportsCar("Ferrari", "488 Spider", 2021, 330)


print("---------- Voertuig Info ----------")
voertuig.display()

print("\n---------- Off-Road voertuig Info ----------")
off_road_vehicle.display()

print("\n---------- SportsCar Info ----------")
sports_car.display()



