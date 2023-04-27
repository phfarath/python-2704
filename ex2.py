moeda = 1
nota5 = 5
nota10 = 10
nota20 = 20
nota50 = 50
troco = 0
preço = float(input("digite o valor da compra: "))
valorpago = float(input("digite o valor pago aqui: "))
troco = valorpago - preço
div50 =int(troco/nota50)
resto = int(troco - nota50*div50)
div20 = int(resto/nota20)
resto2 = int(resto - nota20*div20 )
div10 = int(resto2/nota10)
resto3 = int(resto2 - nota10*div10)
div5 = int(resto3 / nota5)
resto4 = int(resto3 - nota5*div5)
print(f'voce deu R${valorpago} para R${preço} do(s) produto(s), seu troco será de R${troco}')
print(f'voce recebera {div50} notas de 50, {div20} notas de 20, {div10} notas de 10, {div5} notas de 5 e {resto4} moedas de 1')
    
    
    