import os
from formula.logic import   calcular_propina, calcular_total_con_propina,dividir_total_personas
def desing():
    while True:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input("        Ingrese el monto total de la cuenta: $____"))
        porcentaje = int(input("        Ingrese el porcentaje de propina (por ejemplo: 15): ___ %"))
        persona =  int(input("        Ingrese el número de personas: __"))

        propina = calcular_propina(total, porcentaje)
        totalMasPropina = calcular_total_con_propina(total,propina)
        print(f"""
        =============================================
        La propina calculada es: ${propina}
        El total a pagar es: $___{totalMasPropina}
        Monto por persona: $___{(propina/persona) + dividir_total_personas(total,persona)}
        =============================================

    """)
        options = str(input("¿Deseas calcular nuevamente? (S/N)"))
        if options == "S" or options == "s" :
            os.system("clear")
        else:
            break    
