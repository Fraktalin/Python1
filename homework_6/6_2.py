seconds = int(input("Введіть кількість секунд (між 0 та 8640000): "))

if 0 <= seconds < 8640000:
    days = seconds // 86400
    remainder = seconds % 86400

    hours = remainder // 3600
    remainder %= 3600

    minutes = remainder // 60
    secs = remainder % 60

    if days == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    h_str = str(hours).zfill(2)
    m_str = str(minutes).zfill(2)
    s_str = str(secs).zfill(2)

    print(f"{days} {day_word}, {h_str}:{m_str}:{s_str}")
else:
    print("Число повинно бути від 0 до 8640000")
