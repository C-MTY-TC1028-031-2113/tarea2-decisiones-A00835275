
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad < 18 and edad > 0:
       print("No cumples requisitos")
    elif edad <= 10:
       print("Respuesta incorrecta")
    elif edad >= 18:
       i = input("¿Tienes identificación oficial? (s/n): ")
    if i == ("s"):
        print("Trámite de licencia concedido")
    elif i == ("n"):
        print("No cumples con los requisitos")
    elif i != "n" or "s":
        print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
