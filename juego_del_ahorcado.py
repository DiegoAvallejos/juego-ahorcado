import random

def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular', 'django', 'tensorflow', 'react', 'git']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print("Bienbenido al juego del ahorcado")
    print(f"tenes {intentos} intentos para descubrir la palabra")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "la cantidad de letras es: ", len(palabra_secreta))
    
    while not juego_terminado:
        adivinanza = input("intrudusca una letra: ").lower()
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor ingrese una letra")
        elif adivinanza in letras_adivinadas:
            print("esa letra ya has utilizado") 
        else:
            letras_adivinadas.append(adivinanza)
            
            if adivinanza in palabra_secreta:
                print(f" bien, la letra {adivinanza} esta presente en la palabra")
            else:
                intentos -= 1
                print(" no esta en la palabra")
                print(f"te quedan {intentos} intentos")               

        prograso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(prograso_actual)
        
        if "_" not in prograso_actual:
            juego_terminado = True
            print(f"GANASTE, la palabra secreta era: {palabra_secreta}")
            
    if intentos == 0:
        print(f"lo sentimos, la palabra secreta era: {palabra_secreta}")
        
juego_ahorcado()


        