import user_interface
from uFile_IO import *
from controller import *


def main():
	new_dict()
	a = user_interface.show_menu()
	while a != 6:
		if a == 1:
			print('Полный список:')
			show_full_list()
			a = user_interface.show_menu()

		elif a == 2:
			print(get_block(data_list, find_text_in_block(data_list)))
			a = user_interface.show_menu()

		elif a == 3:
			print(get_block(data_list, find_text_in_block(data_list)))
			a = user_interface.show_menu()

		elif a == 4:
			add_new_line(file_name)
			# Get_from_Data()
			a = user_interface.show_menu()

		elif a == 5:
			save_txt(file_name)
			a = user_interface.show_menu()

		elif a == 6: quit()

main()
