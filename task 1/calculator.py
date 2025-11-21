first_number = float(input("Р’РІРµРґРёС‚Рµ РїРµСЂРІРѕРµ С‡РёСЃР»Рѕ: "))
second_number = float(input("Р’РІРµРґРёС‚Рµ РІС‚РѕСЂРѕРµ С‡РёСЃР»Рѕ: "))
operator = input("Р’РІРµРґРёС‚Рµ РѕРїРµСЂР°С‚РѕСЂ (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "РћС€РёР±РєР°: РґРµР»РµРЅРёРµ РЅР° РЅРѕР»СЊ"
else:
    result = "РћС€РёР±РєР°: РЅРµРІРµСЂРЅС‹Р№ РѕРїРµСЂР°С‚РѕСЂ"

print(f"Р РµР·СѓР»СЊС‚Р°С‚: {result}")