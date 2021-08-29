import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    
    if a == 0 and b == 0:
      print("No tiene solución")
    
    elif a == 0 and b != 0:
        x = -c / b
        print(x)
    
    elif a != 0 and b != 0:
      d = b * b - 4 * a * c
    
    if d < 0:
        print("Raíces complejas")

    elif d > 0:
        x1 = (-b + d ** (1 / 2) ) / ( 2 * a )
        x2 = (-b - d ** (1 / 2) ) / ( 2 * a )
        print(x1)
        print(x2)

    else:
        x = -b / (2 * a)
        print(x)

if __name__ == '__main__':
    main()
