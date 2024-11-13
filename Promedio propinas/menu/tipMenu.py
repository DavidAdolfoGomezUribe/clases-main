from formula.logic import calcular_propina, calcular_total_con_propina
import os

def desing():
    while True:
        print(f"""
        =============================================
                    Cálculo de Propina
        =============================================      """)

        try:
            total = float(input("     Ingrese el monto total de la cuenta: $"))
            
            if total < 0:
                raise ValueError("El monto no puede ser negativo.")
            
            porcentaje = int(input("     Ingrese el porcentaje de propina (por ejemplo: 10, 15, 20): ___ %"))
            
            # Validar que el porcentaje sea razonable (por ejemplo, entre 0 y 100)
            if porcentaje < 0:
                raise ValueError("El porcentaje no puede ser negativo.")
            
            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)

            print(f"""      
            =============================================
            La propina calculada es: ${propina}
            El total a pagar es: ${total_con_propina}
            =============================================
        """)
            
            options = str(input("¿Deseas calcular nuevamente? (S/N): "))
            if options.lower() == "s":
                # Limpiar la pantalla (compatible con Windows y Unix)
                os.system("cls" if os.name == "nt" else "clear")
            else:
                break

        except ValueError as e:
            print(f"Error: {e}. Datos no válidos.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Terminando ejecución.")
            break  # Esto terminará el ciclo mientras

# Llamar la función desing() para ejecutar el código
desing()
