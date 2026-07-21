# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
# pytz = para timezone
from datetime import datetime
# from pytz import timezone

# data_str_data = "2026-05-18 12:53:23"
# data_str_data_2 = "18/05/2026"
# data_str_fmt = "%Y-%m-%d %H:%M:%S"
# data_str_fmt_2 = "%d/%m/%Y"
# data = datetime(2026, 5, 18) # hora minuto segundo, microsegundo sao opcionais
# data = datetime(2026, 5, 18, 12)
# data = datetime(2026, 5, 18, 12, 50)
# data = datetime(2026, 5, 18, 12, 50, 20)
# data = datetime.strptime(data_str_data, data_str_fmt)
# data_2 = datetime.strptime(data_str_data_2, data_str_fmt_2)
# print(data)
# print(data_2)

# data_3 = datetime.now(timezone("America/Sao_Paulo"))
# data_3 = datetime.now(timezone("Asia/Tokyo"))
# print(data_3)

# data = datetime(2026, 5, 18, 12, 50, 20, tzinfo=timezone("Asia/Tokyo"))

data_4 = datetime.now()
print(data_4.timestamp())
print(datetime.fromtimestamp(1779120680))