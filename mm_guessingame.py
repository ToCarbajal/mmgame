#First Upload
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
    elif int_user_input < real_mm:
        if i == 5:
            print("Fallaste!")
        else:
            print("Intenta Otra Vez. Hay MAS M&M")
    else:
        if i == 5:
            print("Fallaste!")
        else:
            print("Intenta Otra Vez. Hay MENOS M&M")
