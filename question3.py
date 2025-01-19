# Soru3: Bir "Şekil" sınıfı oluşturun. Bu sınıfın altında, "Dikdörtgen" ve "Kare" sınıfları olmak üzere iki alt sınıf oluşturun.

# "Şekil" sınıfının iki özelliği olsun: "genişlik" ve "yükseklik".
# "Rectangle" sınıfının "Shape" sınıfından miras almasını sağlayalım ve ek bir "calculate_area()" metodu ekleyelim.
# "Square" sınıfının "Shape" sınıfından miras almasını sağlayalım ve aynı "area_calculate()" metodunu kullanarak 
# karenin alanını hesaplayalım.
# Bir "Dikdörtgen" ve bir "Kare" örneği oluşturun, her birinin genişliğini ve yüksekliğini belirleyin 
# ve her birinin alanını hesaplayın ve sonuçları yazdırın.


class Shape:
    def __init__(self,width, height):
        self.width  = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def calculate_area (self):
        return 2 * (self.width * self.height)
    
rectangle = Rectangle(4,4)
square = Square(10,20)

print(rectangle.calculate_area())
print(square.calculate_area())
