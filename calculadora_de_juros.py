def calcular_juros_compostos(principal, taxa_anual, anos):
    taxa_mensal = taxa_anual / 12 / 100
    meses = anos * 12
    montante = principal * (1 + taxa_mensal) ** meses
    return montante 

print("***CALCULADORA DE JUROS COMPOSTOS***")

principal = float(input("Digite o valor principal: "))
taxa_anual = float(input("Digite a taxa anual de juros (em %): "))
anos = int(input("Digite o número de anos: "))

montante_final = calcular_juros_compostos(principal, taxa_anual, anos)

print(f"O montante final após {anos} anos é: R${montante_final:.2f}")