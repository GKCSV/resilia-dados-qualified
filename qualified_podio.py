def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    t1 = int(tempo_chegada1)
    t2 = int(tempo_chegada2)
    t3 = int(tempo_chegada3)

    if (t1 < t2 and t1 < t3) and (t2 < t3):
        return print("1 -", t1, "minutos\n2 -", t2, "minutos\n3 -", t3, "minutos")
    
    elif (t1 < t2 and t1 < t3) and (t2 > t3):
        return print("1 -", t1, "minutos\n2 -", t3, "minutos\n3 -", t2, "minutos")

    elif (t2 < t1 and t2 < t3) and (t1 < t3):
        return print("1 -", t2, "minutos\n2 -", t1, "minutos\n3 -", t3, "minutos")
    
    elif (t2 < t1 and t2 < t3) and (t1 > t3):
        return print("1 -", t2, "minutos\n2 -", t3, "minutos\n3 -", t1, "minutos")
    
    elif (t3 < t1 and t3 < t2) and (t1 < t2):
        return print("1 -", t3, "minutos\n2 -", t1, "minutos\n3 -", t2, "minutos")
    
    elif (t3 < t1 and t3 < t2) and (t1 > t2):
        return print("1 -", t3, "minutos\n2 -", t2, "minutos\n3 -", t1, "minutos")

##Atualização        