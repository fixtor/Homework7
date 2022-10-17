from uFile_IO import *


# def File_Name():
# 	file_name = input('Введите имя файла: ')
# 	yield file_name

file_name = input('Введите имя файла: ')
data = open(file_name, 'a')

data_string = (Output_data_file_string(file_name))
data_list = data_string.split('\n')

def Get_from_Data(Data_string):
	return Data_string


#Считаем строки в текстовом файле
def Count_lines(data_string):
	count_lines = data_string.count('\n')
	print(count_lines)

#Находим слово в тексте
def find_text(data_string):
	searching_text = str(input('Введите ключевое слово для поиска:'))
	index = data_string.find(searching_text)
	return index


#Считаем блоки в списке
def count_blocks(data_list):
	del data_list[len(data_list) - 1]
	return len(data_list) - 1


#Получаем блок из списка по позиции
def get_block(data_list, block_number):
	if block_number == None:
		print('Значение не найдено')
		quit()
	a = data_list[block_number].split(',')
	block_number -= 1
	return a


#Находим слово в блоке, возвращает номер блока или None
def find_text_in_block(data_list):
	searching_text = str(input('Введите ключевое слово для поиска:'))
	a = [data_list[x].count(searching_text) for x in range(0, len(data_list))]
	count = 0
	for i in a:
		if i != 0:
			return count
		count += 1


def show_full_list():
	a = Output_data_file_string(file_name)
	print(Output_data_file_string(file_name))
	return a


def add_new_line(file_name):
	ne_line = input('Введите новую запись в справочник в порядке:\n Фамилия, Имя, Телефон, Примечание:\n')
	Input_data_file(file_name, ne_line, 'a')



def save_txt(file_name):
	a  = input('Введите имя файла в которыый созранить: ')
	Input_data_file(a, show_full_list(), 'w')

def new_dict():
	print('Добро пожаловать в Справочник!')



