from math import sin,cos,tan,radians
print("Funciones Trigonometricas sen, cos, tan")
def FUN_TRIGO(Angulo):
    x=radians(Angulo)
    print("sin :",Angulo,"=",sin(x))
    print("cos :",Angulo,"=",cos(x))
    print("tan :",Angulo,"=",tan(x))
    
FUN_TRIGO(30)
FUN_TRIGO(60)
FUN_TRIGO(90)
FUN_TRIGO(120)
