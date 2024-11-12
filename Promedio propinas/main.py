import sys


from menu.mainMenu import desing
from menu.calculateTipMenu import desing as desingOption1
from menu.divideAmointsMenu import desing as desingOption2

option = desingOption1()
if option == 1:
    desing()
elif option == 2:
    desingOption2()    
elif option == 3:
    print("        Gracias por usar el programa")
    sys.exit()
else :
    sys.exit()