import numpy as np
import random

# Función para calcular los bits de paridad para Hamming(11,7)
def calculate_parity_bits(data_bits):
    parity_positions = [0, 1, 3, 7]
    hamming_code = np.zeros(11, dtype=int)
    
    # Colocar los bits de datos en la posición correcta
    j = 0
    for i in range(11):
        if i not in parity_positions:
            hamming_code[i] = data_bits[j]
            j += 1
    
    # Calcular los bits de paridad
    for p in parity_positions:
        parity = 0
        for i in range(p, 11, 2*(p+1)):
            parity ^= np.sum(hamming_code[i:i+p+1])
        hamming_code[p] = parity % 2
    
    return hamming_code

# Función para introducir un error aleatorio en el código de Hamming
def introduce_error(hamming_code):
    error_position = random.randint(0, 10)
    hamming_code[error_position] ^= 1
    return hamming_code, error_position

# Función para detectar el error en el código de Hamming
def detect_error(hamming_code):
    parity_positions = [0, 1, 3, 7]
    error_position = 0
    
    for p in parity_positions:
        parity = 0
        for i in range(p, 11, 2*(p+1)):
            parity ^= np.sum(hamming_code[i:i+p+1])
        if parity % 2 != 0:
            error_position += (p+1)
    
    return error_position

# Mensaje original (7 bits)
data_bits = np.array([0, 1, 1, 0, 1, 0, 1])

# Codificación del mensaje
hamming_code = calculate_parity_bits(data_bits)
print("Código de Hamming (11,7):", hamming_code)

# Introducir un error en el código de Hamming
hamming_code_with_error, error_pos = introduce_error(hamming_code.copy())
print("Código de Hamming con error:", hamming_code_with_error)
print("Posición del error introducido:", error_pos + 1)

# Detectar el error
detected_error_pos = detect_error(hamming_code_with_error)
print("Posición del error detectado:", detected_error_pos)
