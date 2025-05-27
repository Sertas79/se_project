'''Вы отправились в магазин и попросили друзей составить список покупок и 
прислать его вам. Каждый из друзей написал свой список и в итоге вам 
прислали три файла: shopping_list_1.txt, shopping_list_2.txt и 
shopping_list_3.txt. Когда вы открыли списки покупок, то сразу заметили, 
что некоторые товары повторяются, поэтому вы решили составить свой собственный
 нормализованный список, где продукты не повторяются и записаны по алфавиту.

Напишите программу shopping_list.py, которая читает строки из трех файлов: 
shopping_list_1.txt, shopping_list_2.txt и shopping_list_3.txt, а затем 
создает новый файл shopping_list.txt, в который помещает все прочитанные 
строки без повторов и в алфавитном порядке.'''
list_shopping = set()
with open('shopping_list_1.txt') as file:
	list_shopping.update(file.readlines())

with open('shopping_list_2.txt') as file:
	list_shopping.update(file.readlines())

with open('shopping_list_3.txt') as file:
	list_shopping.update(file.readlines())

result = []

for i in list_shopping:
	if i != '\n':
		result.append(i.strip('\n'))

result.sort()

with open('shopping_list.txt', 'w') as file:
	file.write('\n'.join(result))

