import math

def subperimetro(s1, s2, s3):
    return (s1+s2+s3)/2

def area_triangulo(s1, s2, s3):
    s = subperimetro(s1, s2, s3)
    return round(math.sqrt( s * (s-s1) * (s-s2) * (s-s3) ), 1)
