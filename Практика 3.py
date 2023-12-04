from collections import Counter
from functools import reduce
import json

with open('countries.json', 'r') as file: countries = json.load(file)

countries_uppercase = list(map(lambda x: x['name'].upper(), countries))
print('Страны прописными буквами:', countries_uppercase)

countries_with_land = list(filter(lambda x: 'land' in x['name'], countries))
print('Страны содержащие "land":', countries_with_land)

six_letter_countries = list(filter(lambda x: len(x['name']) == 6, countries))
print('Страны содержащие в названии ровно 6 букв:', six_letter_countries)

six_or_more_letter_countries = list(
    filter(lambda x: len(x['name']) >= 6, countries))
print('Страны содержащие в названии 6 и более букв:',
      six_or_more_letter_countries)

starting_with_e = list(filter(lambda x: x['name'].startswith('E'), countries))
print('Страны название которых начинаются на "Е"', starting_with_e)

combined_countries = reduce(
    lambda x, y: x + ' ' + y, [x['name'] for x in countries], '') + ' are countries in Northern Europe.'
print('Finland, Sweden, Denmark, Norway, Iceland are countries in Northern Europe.')

capitalized_land_countries = list(map(lambda x: x['name'].capitalize(), filter(
    lambda x: 'land' in x['name'], countries)))
print(capitalized_land_countries)
six_letter_e_countries = list(filter(lambda x: len(
    x['name']) == 6 and 'e' in x['name'], countries))
print(six_letter_e_countries)
combined_countries = reduce(lambda x, y: f"{x}, {y}", map(
    lambda x: x['name'], filter(lambda x: len(x['name']) >= 6, countries))) + ' are countries in the world.'
print(combined_countries)


def categorize_countries(pattern):
    def categorize(countries):
        return list(filter(lambda x: pattern.lower() in x['name'].lower(), countries))
    return categorize


land_countries = categorize_countries('land')(countries)
ia_countries = categorize_countries('ia')(countries)
island_countries = categorize_countries('island')(countries)
stan_countries = categorize_countries('stan')(countries)

print('Страны с land в названии', land_countries)
print('Страны с ia в названии', ia_countries)
print('Страны с island в названии', island_countries)
print('Страны с stan в названии', stan_countries)

with open('countries-data.json', 'r', encoding='utf-8') as file:
    countries_data = json.load(file)

sorted_countries_by_name = sorted(countries_data, key=lambda x: x['name'])
print(sorted_countries_by_name)

sorted_countries_by_capital = sorted(
    countries_data, key=lambda x: x['capital'])
print(sorted_countries_by_capital)

sorted_countries_by_population = sorted(
    countries_data, key=lambda x: x['population'])
print(sorted_countries_by_population)

languages = [
    language for country in countries_data for language in country['languages']]
most_common_languages = Counter(languages).most_common(10)
print('Наиболее популярные языки:', most_common_languages)

most_populated_countries = sorted(
    countries_data, key=lambda x: x['population'], reverse=True)[:10]
print('Наиболее населенные страны:', most_populated_countries)
