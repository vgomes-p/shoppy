import time as tm
import sys
import os
sys.path.append(os.path.abspath('../'))
import PlusOs # type: ignore

def cart():
	total = 0

	while True:
		product_name = input("Produto: ")
		if product_name.lower() == 'acabou':
			break
		while True:
			amount = input(f"Quantas unidades de {product_name}: ")
			if amount.isdigit():
				amount = int(amount)
				pass
			else:
				print("A quantidade não pode ser caracteres")
				continue
			break
		while True:
			uniPrice = input(f"Qual o valor da unidade de {product_name}: R$")
			try:
				uniPrice == float(uniPrice)
				break
			except ValueError:
				print("O valor do produto não pode ser caractere!")
			break
		total += amount * float(uniPrice)
		should_continue = input('Tem mais produtos? \n["sim", "s" ou 0 para sim, "não", "n" ou 1]\n').lower()
		if should_continue == "sim" or should_continue == "s" or should_continue == 0:
			PlusOs.clear()
			continue
		elif should_continue == "não" or should_continue == "n" or should_continue == 1:
			tm.sleep(1)
			PlusOs.clear()
			break
		else:
			print("Por favor, responde como requerido!")
	return int(total)