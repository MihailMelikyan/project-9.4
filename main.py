'''Задача "Функциональное разнообразие":
Lambda-функция:'''
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x,y : x == y , first,second )
print(list(result))

"""Замыкание:"""
from pprint import pprint
def get_advanced_writer(file_name):
    def write_everything(*data_set):
       with open(file_name, 'a', encoding = 'utf-8' ) as file:
           for data in data_set:
               file.write(f'{data}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

'''Метод __call__:'''
from random import choice
class MysticBall:
    def __init__(self,*word):
        self.word = word
    def __call__(self):
        return random.choice(self.word)

first_ball = MysticBall('Да', 'Нет', 'Наверное','скорее да, чем нет ','скорее нет, чем да')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())


















