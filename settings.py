try:
    with open(".env", "r") as file:
        print("Файл уже имеется в наличии. Эти данные верны?")
        for line in file:
            print(line)
        if input("Y/N: ").upper().count("Y") > 0:
            print("Сохранено")
        else:
            raise FileNotFoundError
except FileNotFoundError:
    print("Файл отсутствует. Начинается настройка")
    with open(".env", "w+") as file:
        print("Введите токен своего бота, который вам прислал @BotFather при создании вашего бота.")
        a = input("Токен бота: ")
        file.write(f"TOKEN={a}\n")
        print("Введите свой айди. Его можно узнать в @TheGetAnyID_bot")
        a = input("Айди владельца канала: ")
        file.write(f"BOT_MASTER={a}\n")
        while True:
            print("Введите айди телеграм-канала. Для этого перешлите пост оттуда в @TheGetAnyID_bot")
            a = input("Айди ТГК(начинается с -100): ")
            if a.startswith("-100"):
                file.write(f"CHANNEL_ID={a}")
                break
            else:
                print("Айди должно начинаться с -100!")

print("Настройка завершена!\n теперь можете запускать main.py!")
