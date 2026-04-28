import json

# Faylni ochamiz
with open("prodscts.JSON", "r", encoding="UTF-8") as file:
    mahsulot = json.load(file)

menyu = """
Menyular:
1) Meva
2) Shirinlik
3) Ichimlik
4) Ovqat
0) Chiqish
"""

while True:
    print(menyu)
    meyular = input("Menyudan birini tanlang: ")

    if meyular == "1" or meyular == "Meva" or meyular == "meva":
        for nomi, malumoti in enumerate(mahsulot["Meva"].items(), 1):
            print(f"{malumoti[0]} -> {malumoti[1]} so'm")
        break
    elif meyular == "2" or meyular == "Shirinlik" or meyular == "shirinlik":
        for nomi, malumoti in enumerate(mahsulot["Shirinlik"].items(), 1):
            print(f"{malumoti[0]} -> {malumoti[1]} so'm")
        break
    elif meyular == "3" or meyular == "Ichimlik" or meyular == "ichimlik":
        for nomi, malumoti in enumerate(mahsulot["Ichimlik"].items(), 1):
            print(f"{malumoti[0]} -> {malumoti[1]} so'm")
        break
    elif meyular == "4" or meyular == "Ovqat" or meyular == "ovqat":
        for nomi, malumoti in enumerate(mahsulot["Ovqat"].items(), 1):
            print(f"{malumoti[0]} -> {malumoti[1]} so'm")
        break
    elif meyular == "0":
        print("Tashrifingiz uchun rahmat!")
        break

    else:
        print("Bunday menyu yo'q!")