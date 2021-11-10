import time

inicio = time.time()
list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 3, ]

list_result = []

if len(list_a) > len(list_b):
    for n in range(len(list_b)):
        list_result.append(list_a[n] + list_b[n])
else:
    for n in range(len(list_a)):
        list_result.append(list_b[n] + list_a[n])

print(list_result)
fim = time.time()
print ('duracao: %f' % (fim - inicio))