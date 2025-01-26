def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer


def procesar_buffer(entrada, tamano_buffer):
    inicio = 0
    avance = 0
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexema = ""
    
    while True:
        char = buffer[avance]
        
        if char == "eof":  
            if lexema: 
                print(f"Lexema procesado: {lexema}")
            break
        
        if char.isspace():  
            if lexema: 
                print(f"Lexema procesado: {lexema}")
                lexema = ""
        else:
            lexema += char  
        
        avance += 1
        
        if avance >= len(buffer):
            inicio += tamano_buffer
            buffer = cargar_buffer(entrada, inicio, tamano_buffer)
            avance = 0


entrada = list("Esto es un ejemplo eof")
tamano_buffer = 10
procesar_buffer(entrada, tamano_buffer)
