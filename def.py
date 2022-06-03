def lista(x):
    x.sort()
    for i,n in enumerate(x):
        if x[i] % 2 ==0:
            par.append(x[i])
        else:
            impar.append(x[i])
par= []
impar=[]
lista([1,2,3,9,5,6,7,8,4])
