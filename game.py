# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ»
# Автор: Матвей Силин
# Дата: сентябрь 2026
# ================================================

title = "DUNGEON MASTER"
frame = "=" * 17
print(frame)
print(" " + title + " ")
print(frame)

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в подземелье, здесь темно и пахнет магнезией, на фоне слышен голос некого Billy")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
stamina = int(input())

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {stamina}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print()

# --- Подготовка к главному циклу (Раздел 4.2 и 4.3) -
running = True
actions = 0

# --- Главный цикл игры -----------------------------
while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - посмотреть в карман")
    print("5 - свериться с картой")
    print("6 - тренировка")
    print("0 - выйти из подземелья")
    print()

    # --- Защита от неверного ввода (Раздел 4.5) --------
    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()
    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()

    # --- Выбор действия --------------------------------
    match choice:
        case "0":
            print("Вы разворачиваетесь и поднимаетесь обратно к выходу. Подземелье Мастера остается позади.")
            running = False

        case "1":
            print("Вы осмотрелись. Комната пуста, только пыль на полу.")

        case "2":
            cost = 2
            if stamina >= cost:
                stamina -= cost
                print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
            else:
                health -= (cost - stamina)
                stamina = 0
                print("Сил больше нет — вы идёте на одном упорстве.")

        case "3":
            stamina += 4
            print("Вы садитесь на холодный пол и переводите дух. Силы постепенно возвращаются.")

        case "4":
            print("Вы заглядываете в карман. Там лежит пара старых вещей и немного крошек.")

        case "5":
            print("Вы разворачиваете потертую карту, но в этой темноте сложно что-то разобрать.")

        case "6":
            strikes = 5
            cost = 1
            
            if stamina < cost:
                print("Слишком мало сил для тренировки.")
            else:
                stamina -= cost
                print("Вы подходите к старому тренировочному манекену.")
                print("Его набили тряпьём и оставили здесь шахтеры, чтобы не терять хватку в дни простоя.")
                print()
                print(f"Наносите {strikes} ударов.")
                
                total_damage = 0
                crit_count = 0
                
                for i in range(1, strikes + 1):
                    if i % 3 == 0:
                        hit_damage = crit_damage
                        is_crit = True
                    else:
                        hit_damage = damage
                        is_crit = False
                    
                    if is_crit:
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    
                    total_damage += hit_damage
                    if is_crit:
                        crit_count += 1
                
                print()
                print(f"Итог: {strikes} ударов, {crit_count} критический{'и' if crit_count != 1 else ''}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")

    # --- Подсчет действий (Раздел 4.3) -----------------
    if running:
        actions += 1

    # --- Строка состояния и проверка гибели (Раздел 4.4)
    print()
    print(f"Здоровье: {health} Запас сил: {stamina}")
    
    if health <= 0:
        print(f"Голос Billy затихает... {hero_name} падает без сил. Подземелье Мастера забирает еще одного искателя.")
        running = False

# --- Прощание за циклом (Раздел 4.4) ----------------
frame1 = "=" * 55
print(frame1)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Вы покидаете подземелье мастера. Удачи, {hero_name}!")
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame1)
