#!/usr/bin/env python3
import sys
import os
import time as tm
sys.path.append(os.path.abspath('../libs'))
import PlusOs # type: ignore
import shpy # type: ignore

PlusOs.clear()
full_name = str(input("Qual o seu nome?\n: "))
PlusOs.clear()
name_cpy = full_name.split(' ')
name = name_cpy[0]

#get_age
while True:
	age = input(f"Qual sua idade? \n{name}: ")
	if int(age) <= 0:
		print("Você nem nasceu ainda... Responda uma idade válida")
		tm.sleep(5)
		PlusOs.clear()
		continue
	elif age.isdigit():
		pass
	else:
		print("Somente números são aceitos como idade. Por favor, tente de novo!")
		tm.sleep(5)
		PlusOs.clear()
		continue
	break
PlusOs.clear()
pcart = shpy.cart()
PlusOs.clear()

discount = 0.0
discount = float(discount)
if int(age) <= 59:
	pass
else:
	discount += 0.05

discount += shpy.get_client_discount(f"Qual é seu tipo de fidelidade? \n{name}: ")
fin_discount = float(pcart) * discount
wdiscount = float(pcart) - fin_discount
wdiscount = str(wdiscount).split('.')
intpart = wdiscount[0]
floatpart = wdiscount[1]
floatpart = str(floatpart)[:2]
final = f'{intpart}.{floatpart}'

tm.sleep(2)
PlusOs.clear()
print(f'Okay, {name}, o valor da sua compra fica em R${final}!')