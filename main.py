import csv
import re


def get_age():
    print('Укажите ваш возраст(ОБЯЗАТЕЛЬНО!):')
    while True:
        age = 0
        try:
            age = int(input())
            return age
        except ValueError:
            print('Введите целое число!')


def get_price():
    print('Укажите максимальную стоимость игры(666 - если стоимость не важна):')
    while True:
        price = 0
        try:
            price = int(input())
            return price
        except ValueError:
            print('Введите число')


def filter_date(variable, i_date):
    if '-' in i_date:
        i_date = i_date.split('-')
        return i_date[0] <= variable <= i_date[1]
    else:
        return (variable == i_date) or (i_date == '')


def filter_developer(variable):
    return any(developer in variable for developer in developers) or (developers == [''])


def filter_platform(variable):
    return any(platform in variable for platform in platforms) or (platforms == [''])


def filter_age(variable, i_age):
    return variable <= i_age


def filter_category(variable):
    return any(category in variable for category in categories) or (categories == [''])


def filter_genre(variable):
    return any(genre in variable for genre in genres) or (genres == [''])


def filter_rating(variable):
    return ((ratings == 'Good') and variable > 0) or (ratings == '')


def filter_price(variable, i_price):# Сделать промежуток
    if i_price == '':
        return 1
    else:
        return float(i_price) >= variable


age = get_age()
date = input('Год выпуска(Введите число или промежуток \'YYYY-YYYY\'):\n')
developers = input('Разработчик игры:\n').split(',')
platforms = input('Платформа игры:\n').split(',')
genres = input('Жанр игры:\n').split(',')
categories = input('Категория игры:\n').split(',')
price = get_price()
ratings = input('Отзывы?\nНапишите \'Good\', если нужны игры только с положительными отзывами')


def filter_final():
    return (filter_date(file_date, date) and filter_developer(file_developer)
                and filter_platform(file_platforms) and filter_age(file_age, age)
                and filter_category(file_categories) and filter_genre(file_genres)
                and filter_rating(file_ratings) and filter_price(file_price, price))


with open('steam.csv', encoding='utf-8') as f1, \
        open('List_of_games.txt', 'w', encoding='utf-8') as f2:
    reader = csv.reader(f1)
    for line in reader:
        if line[0] == 'appid':
            continue

        file_date = line[2][:4]
        file_developer = line[4].split(';')
        file_platforms = line[6].split(';')
        file_age = int(line[7])
        file_categories = line[8].split(';')
        file_genres = line[9].split(';')
        file_ratings = int(line[12]) - int(line[13])
        file_price = float(line[17])
        if filter_final(): f2.write(line[1] + '\n')