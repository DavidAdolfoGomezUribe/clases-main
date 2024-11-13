import sys


from menu.mainMenur import desing as desingOption0
from menu.tipMenu import desing as desingOption1
from menu.divideAmointsMenu import desing as desingOption2

while True:
    awser = desingOption0()
    match awser:
        case 1:
           desingOption1()
           
        case 2:
           desingOption2()    
        case 3 :
          print("""        
      =============================================
      ¡Gracias por usar el Simulador de Propina!
      =============================================
              """)
          sys.exit()
        