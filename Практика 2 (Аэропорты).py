import json

airpot_codes = {
    'Bolshoye Savino Airport': 'PEE',
    'Аэропорт Большое Савино': 'PEE',
    'Hpa-An Airport': 'PAA',
    'Аэропорт Хпа-Ан': 'PAA',
    'Pardubice Airport': 'PED',
    'Аэропорт Пардубице': 'PED',
    'Pelican Seaplane Base': 'PEC',
    'Гидроаэропорт Пеликан': 'PEC',
    'Bilaspur Airport': 'PAB',
    'Аэропорт Бисалпур': 'PAB',
    'Paderborn Lippstadt Airport': 'PAD',
    'Аэропорт Падерборн': 'PAD',
    'Pakuba Airfield': 'PAF',
    'Аэродром Пакуба': 'PAF',
    'St. Pete–Clearwater International Airport': 'PIE',
    'Аэропорт Сент-Пит-Клируотер': 'PIE',
    'Pevek Airport': 'PWE',
    'Аэропорт Певек': 'PWE',
    'Polyarny Airport': 'PYJ',
    'Аэропорт Полярный': 'PYJ',
    'Yelizovo Airport': 'PKC',
    'Аэропорт Елизово': 'PKC',
    'Pechora Airport': 'PEX',
    'Аэропорт Печора': 'PEX',
}

with open('airpot_codes.json', 'w') as file:
    json.dump(airpot_codes, file, indent=4)

with open('airpot_codes.json', 'r') as file:
    airpot_codes = json.load(file)


def find_airport_code(airport_name):
    for name, code in airpot_codes.items():
        if airport_name == name:
            return code
    return "Код аэропорта не найден"


airport_name = input("Введите название аэропорта: ")

code = find_airport_code(airport_name)
print(f"Код аэропорта для '{airport_name}': {code}")
