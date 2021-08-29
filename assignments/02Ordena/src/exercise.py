def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    if (x > y):
       if (z < y):
           print(z)
           print(y)
           print(x)
        
       elif (x > z):
           print(y)
           print(z)
           print(x)
        
       else:
           print(y)
           print(x)
           print(z)
        
    elif (y > x):
        if (z < x):
            print(z)
            print(x)
            print(y)
    
        elif (z > x):
            print(x)
            print(z)
            print(y)
    
        else:
            print(x)
            print(y)
            print(z)

    else:
        if(x < y):
            print(x)
            print(y)
            print(z)
    
        elif (y > z):
            print(x)
            print(z)
            print(y)
        
        else:
            print(x)
            print(y)
            print(z)


if __name__=='__main__':
    main()
