import os

FILENAME = "tasks.txt"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    print("\n" + "в•ђ" * 50)
    if tasks:
        print("Р’Р°С€Рё Р·Р°РґР°С‡Рё:")
        print("в”Ђ" * 50)
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("РЎРїРёСЃРѕРє Р·Р°РґР°С‡ РїСѓСЃС‚")
    print("в•ђ" * 50)


def add_task(tasks):
    task = input("\nР’РІРµРґРёС‚Рµ Р·Р°РґР°С‡Сѓ: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Р—Р°РґР°С‡Р° '{task}' РґРѕР±Р°РІР»РµРЅР°!")
    else:
        print("Р—Р°РґР°С‡Р° РЅРµ РјРѕР¶РµС‚ Р±С‹С‚СЊ РїСѓСЃС‚РѕР№!")


def delete_task(tasks):
    if not tasks:
        print("\nРЎРїРёСЃРѕРє Р·Р°РґР°С‡ РїСѓСЃС‚!")
        return
    
    show_tasks(tasks)
    try:
        index = int(input("\nР’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ Р·Р°РґР°С‡Рё РґР»СЏ СѓРґР°Р»РµРЅРёСЏ: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Р—Р°РґР°С‡Р° '{removed}' СѓРґР°Р»РµРЅР°!")
        else:
            print("РќРµРІРµСЂРЅС‹Р№ РЅРѕРјРµСЂ Р·Р°РґР°С‡Рё!")
    except ValueError:
        print("Р’РІРµРґРёС‚Рµ РєРѕСЂСЂРµРєС‚РЅС‹Р№ РЅРѕРјРµСЂ!")


def main():
    tasks = load_tasks()
    
    print("в•”" + "в•ђ" * 48 + "в•—")
    print("в•‘" + " " * 18 + "TO-DO LIST" + " " * 20 + "в•‘")
    print("в•љ" + "в•ђ" * 48 + "в•ќ")
    
    while True:
        print("\n1. РџРѕРєР°Р·Р°С‚СЊ Р·Р°РґР°С‡Рё")
        print("2. Р”РѕР±Р°РІРёС‚СЊ Р·Р°РґР°С‡Сѓ")
        print("3. РЈРґР°Р»РёС‚СЊ Р·Р°РґР°С‡Сѓ")
        print("4. Р’С‹С…РѕРґ")
        
        choice = input("\nР’С‹Р±РµСЂРёС‚Рµ РґРµР№СЃС‚РІРёРµ (1-4): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nР”Рѕ СЃРІРёРґР°РЅРёСЏ!")
            break
        else:
            print("\nРќРµРІРµСЂРЅС‹Р№ РІС‹Р±РѕСЂ! РџРѕРїСЂРѕР±СѓР№С‚Рµ СЃРЅРѕРІР°.")


if __name__ == "__main__":
    main()