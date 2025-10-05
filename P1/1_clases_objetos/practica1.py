def area_rectangulo(base,altura):
    return base*altura
print(area_rectangulo(5,3))


class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    def area(self):
        return self.base * self.altura

rect=rectangulo(5,3)
print(rect.area())
