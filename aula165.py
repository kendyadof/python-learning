# comentei certas linhas pra nao ficar com erro do modulo relativedelta...
# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2022 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
n_parcelas=60
valor_emp = 1000000 # poderia ter feito: 1_000_000
parcela = valor_emp/n_parcelas
# print(parcela)
data_emp = datetime(2022, 12, 20)
# dif = relativedelta(months=n_parcelas)
# data_fim = data_emp + dif
# dif_time = (data_fim - data_emp)
# dif_stamp = dif_time.timestamp()
# print(dif_time)
fmt = "%d/%m/%Y"
# test_data = datetime(2027,12,20)
# print(test_data)
# for month in range(n_parcelas):
#     data_result = data_emp + relativedelta(months=month)
#     print(f"{data_result.strftime(fmt)} R$ {parcela:,.2f}")
# print(data_fim)
# print(f"Você pegou R${valor_emp:,.2f} para pagar em {dif.years} anos ({dif.years*12} meses) em parcelas de R$ {parcela:,.2f}")
