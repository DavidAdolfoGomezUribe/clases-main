import sys


from menu.mainMenur import desing0 as desingOption1
from menu.tipMenu import desing 
from menu.divideAmointsMenu import desing as desingOption2

while True:
    
    
    match desingOption1() :
    
        case 1:
            desing()
        case 2:
            desing()    
        case 3 :
            print("""        
        =============================================
        ¡Gracias por usar el Simulador de Propina!
        =============================================
                """)
            sys.exit()
        