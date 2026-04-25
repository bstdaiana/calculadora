# Calculadora en Python reutilizable con funciones y manejo de errores
def Sumar(a, b):
    return a + b


def Restar(a, b):
    return a - b


def Multiplicar(a, b):
    return a * b


def Dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


def main():
    while True:
        try:
            print("\n--- CALCULADORA ---")
            num1 = float(input("Ingresá el primer número: "))
            num2 = float(input("Ingresá el segundo número: "))

            print("\nElegí una operación:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")

            opcion = input("Opción: ")

            if opcion == "1":
                resultado = Sumar(num1, num2)
            elif opcion == "2":
                resultado = Restar(num1, num2)
            elif opcion == "3":
                resultado = Multiplicar(num1, num2)
            elif opcion == "4":
                resultado = Dividir(num1, num2)
            else:
                raise ValueError("Opción inválida.")

            print("Resultado:", resultado)

        except ValueError:
            print("Error: ingresaste un valor inválido.")
        except ZeroDivisionError as e:
            print("Error:", e)
        except Exception as e:
            print("Ocurrió un error inesperado:", e)

        repetir = input("\n¿Querés hacer otra cuenta? (s/n): ").lower()

        if repetir != "s":
            print("Calculadora finalizada.")
            break


if __name__ == "__main__":
    main()