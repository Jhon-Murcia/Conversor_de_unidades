def menu():
    while True:
        print("\nMenú")
        print("1. Conversor de símbolo a binario")
        print("2. Conversor de binario a decimal")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            arreglo = []
            def convertir(num):
                c = num
                for pos in range(7, -1, -1):
                    if (c >= 2**pos):
                        arreglo.append(1)
                        c = c - 2**pos
                    else:
                        arreglo.append(0)
                return arreglo

            entrada = input("Ingresa un número o un carácter: ")

            if len(entrada) == 1:  
                num = ord(entrada)
            else:
                try:
                    num = int(entrada)  
                except ValueError:
                    print("Error: Ingresa un número válido o un solo carácter.")
                    continue

            if 0 <= num <= 255:
                mostrar = convertir(num)
                print("Binario:", mostrar)
            else:
                print("Error: El número debe estar entre 0 y 255.")

        elif opcion == "2":
            rta = []
            for i in range(8):
                rta.append(int(input("Ingrese el bit" + str(7-i) + " que corresponde a 1 o 0: ")))

            def convertirDecimal(air):
                suma = 0
                for i in range(8):
                    if (air[i] == 1):
                        suma = suma + (2**(7-i))
                return suma 

            mostrar = convertirDecimal(rta)
            print("Decimal:", mostrar)
            print("Carácter ASCII:", chr(mostrar))

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

menu()
