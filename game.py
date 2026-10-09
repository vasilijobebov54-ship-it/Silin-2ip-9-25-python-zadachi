# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ»
# Автор: Матвей Силин
# Дата: сентябрь 2026
#
# Пункт 4 — «прислушаться»: герой замирает
# и слушает, что происходит в темноте. Пока
# пункт только выводится в меню — обрабатывать
# его будем на третьем занятии.
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

# --- Меню действий ---------------------------------
print("Что делаешь?")
print("1 - осмотреться")
print("2 - идти вперёд")
print("3 - отдохнуть")
print("4 - посмотреть в карман")
print("5 - свериться с картой")
print("6 - тренировка")
print()

# --- Выбор действия --------------------------------
choice = input()
match choice:
    case "1":
        print("Вы осмотрелись. Комната пуста, только пыль на полу.")
    case "2":
        stamina = stamina - 2
        print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
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
            print(f"Здоровье: {health} Запас сил: {stamina}")
    case _:
        print("Такого действия нет.")

# --- Состояние героя (добавлено на прошлом занятии) ---
print(f"Здоровье: {health} Запас сил: {stamina}")

# Прощание
frame1 = "=" * 55
print(frame1)
print(f"Вы покидаете подземелье мастера. Удачи, {hero_name}!")
print(frame1)
