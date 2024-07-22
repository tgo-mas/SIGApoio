

def converter_horarios(dias, horarios):
    '''Converte 2 vetores de strings, um de dias e outro de horarios, em apenas horarios com seus respectivo dias'''
    horarios_final = []
    for dia in dias:
        for horario in horarios:
            horarios_final.append(dia + horario)
    return horarios_final
    
