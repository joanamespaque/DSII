# atributos: ponto1, ponto2, ponto3
# métodos: isosceles (retorno boolean), equilatero (retorno boolean), escaleno (retorno boolean) e
# perimetro()

import math
class Triangulo:
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def _get_p1(self):
        return self._p1 
    def _set_p1(self, p1):
        self._p1 = p1 
    p1 = property(_get_p1, _set_p1)

    def _get_p2(self):
        return self._p2 
    def _set_p2(self, p2):
        self._p2 = p2 
    p2 = property(_get_p2, _set_p2)

    def _get_p3(self):
        return self._p3 
    def _set_p3(self, p3):
        self._p3 = p3 
    p3 = property(_get_p3, _set_p3)
    def isosceles(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if(((d1==d2)and(d2!=d3)) or ((d2==d3)and(d2!=d1)) or ((d1==d3)and(d2!=d3))):
            return True
        else:
            return False
    def equilatero(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if((d1==d2)and(d2==d3)):
            return True
        else:
            return False
    def escaleno(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if((d1!=d2)and(d2!=d3)and(d1!=d3)):
            return True
        else:
            return False
    def perimetro(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        return (d1+d2+d3)



        
t1 = Triangulo([5,6],[5,9], [2,3])
t2 = Triangulo([1,3],[4,3], [1,0])
print(t1.isosceles())
print(t1.equilatero())
print(t1.escaleno())
print(t1.perimetro())
print(t2.isosceles())
print(t2.equilatero())
print(t2.escaleno())
print(t2.perimetro())

x1 = int(input("digite x1:"))
y1 = int(input("digite y1:"))
x2 = int(input("digite x2:"))
y2 = int(input("digite y2:"))
x3 = int(input("digite x3:"))
y3 = int(input("digite y3:"))
c1 = [x1, y1]
c2 = [x2, y2]
c3 = [x3, y3]
d1 = (c1[0] - c2[0])**2 + (c1[1] - c2[1])**2
d2 = (c2[0] - c3[0])**2 + (c2[1] - c3[1])**2
d3 = (c3[0] - c1[0])**2 + (c3[1] - c1[1])**2
print(d1)
print(d2)
print(d3)

if(d1>d2+d3 or d2>d3+d1 or d3>d2+d1):
    print("nao eh triangulo")
else:
    triangulo = Triangulo(c1, c2, c3)
    if(triangulo.isosceles() == True):
        print("eh um triangulo isosceles")
    elif(triangulo.equilatero() == True):
        print("eh um triangulo equilatero")
    else:
        print("eh um triangulo escaleno")




    

