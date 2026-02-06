saldo = 0
ledger = [{'producto': 'Lavadora', 'precio': 13},{'producto': 'PC', 'precio': 10*-1}]

# for precio in ledger:
#     print(precio['precio'])
#     saldo += precio['precio']

saldo = sum(precio['precio'] for precio in ledger)

print(saldo)