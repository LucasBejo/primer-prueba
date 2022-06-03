nro_valido = 0
nro_invalido = 0

try:
 n = int(input("cant nro: "))
 for i in range(n):
    l = int(input(" nro: "))
    if (l % 2) == 0 and l >= 10:
        nro_valido +=1
    else:
        nro_invalido +=1
except Exception as e:
    print("tipo error",type(e).__name__)
print(f"nro valido: {nro_valido}")
print(f"nro invalido: {nro_invalido}")   
