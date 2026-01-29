import random

max_number = 10
min_number = 1
vibor_bota = random.randint(min_number, max_number)
max_trys = 5
trys = 5

while True:
    if not trys == 0:
        print(f"Ваши попытки: {trys}")
    else:
        print("Кончились попытки, лох")
        break
    
    while True:
        try:
            vibor_chela = int(input("🌚Выбери число🌚 "))
            
            if vibor_chela > max_number or vibor_chela < min_number:
                print(f"Пожалуйста, выберите число от {min_number} до {max_number}")
                continue
            else:
                break
                
        except ValueError:
            print("Инвалид")
            continue
    
    if vibor_chela == vibor_bota:
        print("Попеда еблан")
        vibor_bota = random.randint(min_number, max_number)
        trys = max_trys
    else:
        trys -= 1
        if vibor_chela > vibor_bota:
            print("Меньше")
        else:
            print("Больше")
