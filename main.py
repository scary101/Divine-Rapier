import os
import pygame
import asyncio
import random
rand = random.randint(0, 5)


folder_path = 'C:\\Users\\user\\PycharmProjects\\pythonProject8\\music'
file_names = os.listdir(folder_path)
file_path = folder_path + '\\' + file_names[rand]
answer = ["Bad Gyu", "Love The Way You Lie", "За деньги ДА", "In the end", "Numb", "Мама Люба"]
print(rand)

async def start():
    run = True
    while run != False:
        a = input("Добро пожаловать на шоу Угадай Песню"
                  "\n Чтобы начать введите Да, если хотите выйте Нет")
        if a == "да":
            run = False
        elif a == 'Нет':
            exit()
        else:
            pass

async def play_music():
    await start()

    pygame.init()
    correct_guess = False
    track = file_path  

    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() and not correct_guess:
        print(rand)
        guess = input("Угадайте название песни: ")
        if guess.lower() == answer[rand].lower():
            correct_guess = True
            print("Вы угадали!")
        else:
            print("Попробуйте еще раз!")

    pygame.mixer.music.stop()
    pygame.quit()


async def main():
    await play_music()

run = True
while run != False:
    asyncio.run(main())
    b = input("Хотите попробовать еще раз? Да или Нет")
    if b == "Да":
        pass
    else:
        break
