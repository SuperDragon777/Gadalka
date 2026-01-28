import random
vibor_bota = random.randint(1, 10)
while True:
    vibor_chela = int(input())
    if vibor_chela == vibor_bota:
        print("Попеда еблан")
        vibor_bota = random.randint(1, 10)
    else:
        if vibor_chela > vibor_bota:
            print("Меньше")
        else:
            if vibor_chela < vibor_bota:
                print("Больше")    
