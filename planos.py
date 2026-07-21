# import pandas as pd

# anos = (2026, 2027, 2028, 2029, 2030, 2031)

# REAJUSTE_ANUAL = 1.2
# REAJUSTE_ISA = 1.22
# REAJUSTE_PEPE = 1.2

# pepeplano1 = 721.07
# pepeplano2 = 637.75
# pepeplano3 = 561.47
# isaplano1 = 600.88
# isaplano2 = 531.46
# isaplano3 = 467.89

# # prepare a dict to collect rows (each row is a plan)
# data = {
#     "Pepe - Plano 1": [],
#     "Isa  - Plano 1": [],
#     "Total - Plano 1": [],
#     "Pepe - Plano 2": [],
#     "Isa  - Plano 2": [],
#     "Total - Plano 2": [],
#     "Pepe - Plano 3": [],
#     "Isa  - Plano 3": [],
#     "Total - Plano 3": [],
# }

# # make copies of base values to mutate year-to-year
# p1, p2, p3 = pepeplano1, pepeplano2, pepeplano3
# i1, i2, i3 = isaplano1, isaplano2, isaplano3

# for ano in anos:
#     # apply age-based changes at start of year
#     if ano == 2029:
#         i1 *= REAJUSTE_ISA
#         i2 *= REAJUSTE_ISA
#         i3 *= REAJUSTE_ISA
#     if ano == 2031:
#         p1 *= REAJUSTE_PEPE
#         p2 *= REAJUSTE_PEPE
#         p3 *= REAJUSTE_PEPE

#     # compute totals for each plan
#     t1 = p1 + i1
#     t2 = p2 + i2
#     t3 = p3 + i3

#     # append (raw numeric values) for this year to each plan row
#     data["Pepe - Plano 1"].append(p1)
#     data["Isa  - Plano 1"].append(i1)
#     data["Total - Plano 1"].append(t1)
#     data["Pepe - Plano 2"].append(p2)
#     data["Isa  - Plano 2"].append(i2)
#     data["Total - Plano 2"].append(t2)
#     data["Pepe - Plano 3"].append(p3)
#     data["Isa  - Plano 3"].append(i3)
#     data["Total - Plano 3"].append(t3)

#     # apply annual reajuste for next year
#     p1 *= REAJUSTE_ANUAL
#     i1 *= REAJUSTE_ANUAL
#     p2 *= REAJUSTE_ANUAL
#     i2 *= REAJUSTE_ANUAL
#     p3 *= REAJUSTE_ANUAL
#     i3 *= REAJUSTE_ANUAL

# # build DataFrame with plans as rows and years as columns
# df = pd.DataFrame(data, index=anos).T
# df.columns = [str(c) for c in df.columns]  # years as strings for Excel headers

# # write to Excel with Reais currency format
# output_file = "planos_por_ano.xlsx"
# with pd.ExcelWriter(output_file, engine="openpyxl", datetime_format=None) as writer:
#     df.to_excel(writer, sheet_name="Valores", index=True)

#     # apply number format to value cells (skip header row and the index column)
#     workbook = writer.book
#     worksheet = writer.sheets["Valores"]

#     # Excel currency format for Brazilian Real: R$ with two decimals, thousands separator.
#     # openpyxl uses format codes like 'R$ #,##0.00' — adjust if your locale requires different symbol spacing.
#     currency_fmt = 'R$ #,##0.00'

#     # columns start at 2 in Excel file because col 1 is index (plans)
#     for col_idx in range(2, 2 + len(df.columns)):
#         col_letter = worksheet.cell(row=1, column=col_idx).column_letter
#         for row_idx in range(2, 2 + len(df.index)):
#             worksheet[f"{col_letter}{row_idx}"].number_format = currency_fmt

# print(f"Wrote {output_file}")


# import pandas as pd

# anos = (2026, 2027, 2028, 2029, 2030, 2031)

# REAJUSTE_ANUAL = 1.2
# REAJUSTE_ISA = 1.22
# REAJUSTE_PEPE = 1.2

# pepeplano1 = 721.07
# pepeplano2 = 637.75
# pepeplano3 = 561.47
# isaplano1 = 600.88
# isaplano2 = 531.46
# isaplano3 = 467.89

# rows = []

# for ano in anos:
#     # apply age-based changes at the start of the year where appropriate
#     if ano == 2029:
#         isaplano1 *= REAJUSTE_ISA
#         isaplano2 *= REAJUSTE_ISA
#         isaplano3 *= REAJUSTE_ISA
#     if ano == 2031:
#         pepeplano1 *= REAJUSTE_PEPE
#         pepeplano2 *= REAJUSTE_PEPE
#         pepeplano3 *= REAJUSTE_PEPE

#     valorplano1 = pepeplano1 + isaplano1
#     valorplano2 = pepeplano2 + isaplano2
#     valorplano3 = pepeplano3 + isaplano3
#     soma_total = valorplano1 + valorplano2 + valorplano3

#     rows.append({
#         "Ano": ano,
#         "Pepe Plano 1": round(pepeplano1, 2),
#         "Isa Plano 1": round(isaplano1, 2),
#         "Total Plano 1": round(valorplano1, 2),
#         "Pepe Plano 2": round(pepeplano2, 2),
#         "Isa Plano 2": round(isaplano2, 2),
#         "Total Plano 2": round(valorplano2, 2),
#         "Pepe Plano 3": round(pepeplano3, 2),
#         "Isa Plano 3": round(isaplano3, 2),
#         "Total Plano 3": round(valorplano3, 2),
#         "Soma dos 3 Planos": round(soma_total, 2),
#     })

#     # apply annual reajuste for next year
#     pepeplano1 *= REAJUSTE_ANUAL
#     isaplano1 *= REAJUSTE_ANUAL
#     pepeplano2 *= REAJUSTE_ANUAL
#     isaplano2 *= REAJUSTE_ANUAL
#     pepeplano3 *= REAJUSTE_ANUAL
#     isaplano3 *= REAJUSTE_ANUAL

# df = pd.DataFrame(rows)

# # write to Excel
# output_file = "planos_valores_anos.xlsx"
# df.to_excel(output_file, index=False)
# print(f"Wrote {len(df)} rows to {output_file}")


anos = (2026, 2027, 2028, 2029, 2030, 2031)

REAJUSTE_ANUAL = 1.2
REAJUSTE_ISA = 1.22
REAJUSTE_PEPE = 1.2

pepeplano1 = 516.27
pepeplano2 = 613.21
pepeplano3 = 734.35
isaplano1 = 467.19
isaplano2 = 554.91
isaplano3 = 664.54


valorplano1 = pepeplano1 + isaplano1
valorplano2 = pepeplano2 + isaplano2
valorplano3 = pepeplano3 + isaplano3

for ano in anos:
    if ano == 2029:
        isaplano1 = isaplano1 * REAJUSTE_ISA
        isaplano2 = isaplano2 * REAJUSTE_ISA
        isaplano3 = isaplano3 * REAJUSTE_ISA
    elif ano == 2031:
        pepeplano1 = pepeplano1 * REAJUSTE_PEPE
        pepeplano2 = pepeplano2 * REAJUSTE_PEPE
        pepeplano3 = pepeplano3 * REAJUSTE_PEPE
    print("-----Ano", ano,"-----")
    print("-Cenário 1-")
    print(f"Valor para Pepe: R${pepeplano1:.2f}")
    print(f"Valor Isa: R${isaplano1:.2f}")
    print(f"Preço total: R${valorplano1:.2f}")
    print("")
    print("-Cenário 2-")
    print(f"Valor para Pepe: R${pepeplano2:.2f}")
    print(f"Valor Isa: R${isaplano2:.2f}")
    print(f"Preço total: R${valorplano2:.2f}")
    print("")
    print("-Cenário 3-")
    print(f"Valor para Pepe: R${pepeplano3:.2f}")
    print(f"Valor Isa: R${isaplano3:.2f}")
    print(f"Preço total: R${valorplano3:.2f}")
    print("")
    pepeplano1 = pepeplano1 * REAJUSTE_ANUAL
    isaplano1 = isaplano1 * REAJUSTE_ANUAL
    pepeplano2 = pepeplano2 * REAJUSTE_ANUAL
    isaplano2 = isaplano2 * REAJUSTE_ANUAL
    pepeplano3 = pepeplano3 * REAJUSTE_ANUAL
    isaplano3 = isaplano3 * REAJUSTE_ANUAL
    valorplano1 = pepeplano1 + isaplano1
    valorplano2 = pepeplano2 + isaplano2
    valorplano3 = pepeplano3 + isaplano3