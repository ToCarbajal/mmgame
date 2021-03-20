#FUO
import random

real_mm = random.randint(1, 100)
total_chances = 5
i = 0

while i < total_chances:
    user_input = input(f"Cuantos m&m hay en el jarron? (0 - 100). Tienes {total_chances - i} intentos. ") 
    int_user_input = int(user_input)    
    i += 1
    if int_user_input == real_mm:
        print(f"Acertaste en {i} turnos!")
        break

    if i == total_chances:
        print("Fallaste!")
    else:
        if int_user_input < real_mm:
            print("Intenta nuevamente; hay MAS m&m's")
        else:
            print("Intenta nuevamente; hay MENOS m&m's")
