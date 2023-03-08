cryptoCurrencyPrices = {
    "bitcoin" : 40000,
    "etherium" : 7000,
    "litecoin": 10
}

print(cryptoCurrencyPrices.keys()) #op: dict_keys(['bitcoin', 'etherium', 'litecoin'])
print(type(cryptoCurrencyPrices.keys())) #op: <class 'dict_keys'>

print(cryptoCurrencyPrices.values()) #op: dict_values([40000, 7000, 10])
print(type(cryptoCurrencyPrices.values())) #op: <class 'dict_values'>

## note that both keys() and values() doesnt return list . they return a special
#type of objects dict_keys and dict_values respectively which are again iterable

for currency in cryptoCurrencyPrices.keys():
    print(currency)


for price in cryptoCurrencyPrices.values():
    print(price)


print("bitcoin" in cryptoCurrencyPrices.keys()) #op: True
print(7000 in cryptoCurrencyPrices.values()) #op: True
print(len(cryptoCurrencyPrices.keys())) #op: 3
print(len(cryptoCurrencyPrices.values())) #op: 3



