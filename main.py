import random

vibor_bota = random.randint(1, 10)
trys = 5

while True:
    if not trys == 0:
        print(f"Ваши попытки: {trys}")
    else:
        print("Кончились попытки, лох")
        break
        
    try:
        vibor_chela = int(input("🌚Выбери число🌚 "))
    except:
        print("Инвалид")
        break
        
    if vibor_chela == vibor_bota:
        print("Попеда еблан")
        vibor_bota = random.randint(1, 10)
        trys = 5
    else:
        trys -= 1
        if vibor_chela > vibor_bota:
            print("Меньше")
        else:
            if vibor_chela < vibor_bota:
                print("Больше")    
