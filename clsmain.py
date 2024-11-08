agenda = list()
opciones = 1
while opciones:
    
    print(agenda)
    
    personas = list()
    personas.append(input(f"ingrese el nombre{len(agenda)+1}"))
    personas.append(int(input(f"ingrese la edad{len(agenda)+1}")))
    agenda.append(personas)
    opciones = int(input("1si o 0no"))
print(agenda)    



#print("")
#agenda=[]
#for i in range(1,3):
#    nombreF=input("Ingrese nombre: ")
#    edadF=int(input("ingrese la edad: "))
#    personaF=[nombreF,edadF]
#    agenda.append(personaF)
#print(agenda)