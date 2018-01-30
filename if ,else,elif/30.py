def notas(nota):
    if nota>=0 and nota<=3:
        return "Insuficiente"
    elif nota>=4 and nota<=6:
        return "Suficiente"
    elif nota>=6 and nota<=10:
        return "Bien"
nota=input("Ingrese nota: ")
print notas(nota)
