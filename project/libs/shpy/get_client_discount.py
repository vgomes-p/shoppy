def get_client_discount(txt):
	while True:
		client = input(txt).lower()
		discount = 0.0
		if client == "comum":
			pass
		elif client == "prata":
			discount += 0.05
			pass
		elif client == "ouro":
			discount += 0.10
			pass
		elif client == "diamante":
			discount += 0.15
			pass
		else:
			print("Categoria não encontrada! Nossas categorias são: Comum, Prata, Ouro e Diamante. Por, favor, responda uma categoria válida!")
			continue
		break
	return discount