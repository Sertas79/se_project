'''Напишите программу sort.py, которая получает из первого аргумента командной
 строки слово, а затем выводит все буквы слова в алфавитном порядке. 
 Учитывайте, что буквы слова могут быть в разных регистрах, но при этом 
 они всё равно должны быть отсортированы по алфавиту.'''
import sys

word = sys.argv[1]
result = []
word = sorted(word, key=str.lower)
for i in word:
	if i in result:
		continue
	else:
		result.append(i)
print(''.join(result))