class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
c3 = c1 + c2
print("First Complex Number :", c1)
print("Second Complex Number:", c2)
print("Sum of Complex Numbers:", c3)
