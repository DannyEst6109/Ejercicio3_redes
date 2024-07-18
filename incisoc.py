import numpy as np

# Matriz de verificación de paridad para Hamming(11, 7)
H = np.array([
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
], dtype=int)

# Lista de bloques recibidos con los corregidos
received_blocks = [
    "10110010000",
    "10110011111", # Corregido: 10110111111 -> 10110011111
    "10110011100", # Corregido: 00110001100 -> 10110011100
    "10100001001",
    "10011000000",
    "01010010101", # Corregido: 10110010101 -> 01010010101
    "01100100101",
    "01110010110",
    "01100000100", # Corregido: 11100001000 -> 01100000100
    "10110011111"
]

def hamming_decode(block):
    block = np.array(list(map(int, block)), dtype=int)
    
    # Calcula el síndrome
    syndrome = np.dot(H, block) % 2
    
    # Convierte el síndrome a un entero
    syndrome_value = int("".join(map(str, syndrome)), 2)
    
    # Si el síndrome no es cero y está dentro del rango válido, hay un error
    if syndrome_value != 0 and syndrome_value <= len(block):
        block[syndrome_value - 1] ^= 1
    
    # Los bits de datos son las posiciones: 3, 5, 6, 7, 9, 10, 11 (índices 2, 4, 5, 6, 8, 9, 10)
    data_bits = [2, 4, 5, 6, 8, 9, 10]
    data = block[data_bits]
    
    # Convierte los bits de datos a un carácter ASCII
    char_value = int("".join(map(str, data)), 2)
    return chr(char_value)

# Decodifica cada bloque y forma el mensaje
message = "".join([hamming_decode(block) for block in received_blocks])
print("Mensaje oculto:", message)
