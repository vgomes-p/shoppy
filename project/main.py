import imports.PlusOs

PlusOs.clear()

#get name
full_name = str(input("Qual o seu nome?\n: "))
name_cpy = full_name.split(' ')
name = name_cpy[0]

#get_age
while True:
	age = input(f"Qual sua idade? \n{name}: ")
	if age.isdigit():
		pass
	else:
		print("Somente números são aceitos como idade. Por favor, tente de novo!")
		continue
	break

#get_cart_price
while True:
	cart = input(f"Okay, e qual o valor de sua compra? \n{name}: ")
	if cart.isdigit():
		pass
	else:
		print("O valor da compra não pode ser caracteres, apenas digitos! Por favor, informe um valor válido!")
	break

#get_age_discount
discount = 0.0
discount = float(discount)
if int(age) <= 59:
	pass
else:
	discount += 0.05

#get_client_type
while True:
	client = input(f"Qual é seu tipo de fidelidade? \n{name}: ").lower()
	if client == "comum":
		pass
	elif client == "prata":
		discount += 0.05
	elif client == "ouro":
		discount += 0.10
	elif client == "diamante":
		discount += 0.15
	else:
		print("Categoria não encontrada! Nossas categorias são: Comum, Prata, Ouro e Diamante. Por, favor, responda uma categoria válida!")
		continue
	break

#calc_discount
fin_discount = float(cart) * discount
wdiscount = float(cart) - fin_discount
wdiscount = str(wdiscount).split('.')
intpart = wdiscount[0]
floatpart = wdiscount[1]
floatpart = str(floatpart)[:2]
final = f'{intpart}.{floatpart}'

#print_final_discount
print(f'Okay, {name}, sendo cliente {client}, o valor da sua compra fica em R${final}!')