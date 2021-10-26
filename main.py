import statistics

lista = list()

for i in range(3):
    lista.append(float(input('Introduzca un valor: '    )))

media = statistics.fmean(lista)
mediana = statistics.median(lista)
varianza = statistics.variance(lista)

print('Lista: ', lista)
print('media: ', media)
print('mediana: ', mediana)
print('varianza: ', varianza)