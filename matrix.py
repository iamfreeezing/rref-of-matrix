file = open("matrix.txt", "r")
l=[]
l+= [list(map(int,i.split())) for i in file] 
print()
print("Original matrix is:")
print(l)


def remove0(list): #replace 1.0 by 1
    for i in list:
        c=-1
        for j in i:
            c+=1
            if str(j)[-1] == "0":
                i[c] = int(j)



def solutions(list):
    vars=[]
    colmatrix=[]
    freevars = []
    pivots = []
    for i in range(len(list[0])):
        vars.append("x" + str(i+1))
    
    for j in range(len(list[0])):
        cols=[]
        for i in list:
            cols.append(i[j])
        colmatrix.append(cols)
    
    for i in colmatrix:
        if i.count(1) == 1 and i.count(0) == len(i) - 1:
            pivots.append(colmatrix.index(i))
    for i in colmatrix:
            if i.count(1) == 1 and i.count(0) == len(i) - 1:
                pass
            else:
                freevars.append(colmatrix.index(i))
    if True:

        const=[0 for i in range(len(vars))]
        bigfvmatrix=[]
        for i in freevars:
            fvmatrix=[]
            for j in colmatrix[i]:
                fvmatrix.append(-j)
            bigfvmatrix.append(fvmatrix)
        actualfreevars=[]
        for i in freevars:
            actualfreevars.append(vars[i])
        for i in range(len(actualfreevars)):
            for j in range(len(actualfreevars)-1):
                bigfvmatrix[i].insert(freevars[j],0)
            bigfvmatrix[i].insert(freevars[i], 1)
        for i in bigfvmatrix:
            if len(i) > len(vars):
                i.pop()
        print()
        print("The parametric solution is: ")
        print(vars, "=", end=" ")
        for i in range(len(actualfreevars)):
            print(str(actualfreevars[i]) + str(bigfvmatrix[i]), end=" + ")
        print(const)
        print()


def prosort(l):
    zeroes={}
    for i in range(len(l)):
        c=0
        for j in range(len(l[i])):
            if l[i].count(0) == len(l[i]):
                zeroes[i] = len(l[i])
            elif l[i][j] == 0:
                c+=1
            else:
                zeroes[i] = c
                break

    zeroessorted = {k: v for k, v in sorted(zeroes.items(), key = lambda v: v[1], reverse=True)}
    list = []
    for i in zeroessorted.keys():
        list.insert(0, l[i])
    return list

l1 = prosort(l)


    
def fnzz(row, baharlist):
    for i in range(len(baharlist)):
        if i == (row):
            for j in baharlist[i]:
                if j!=0:
                    a = j
                    break
                else:
                    a="DNE"
            break
    return a

for i in range(len(l1)):
    fnz = fnzz(i, l1)
    if fnz == "DNE":
        pass
    else:
        b = l1[i].index(fnz)
        for j in range(len(l1)):
            c = l1[j][b]
            if j == i:
                pass
            elif l1[j][b] == 0:
                pass
            else:
                for k in range(len(l1[j])):
                    l1[j][k] = l1[j][k] - (c/fnz)*l1[i][k]
                    if abs(l1[j][k]) < 10**(-7):
                        l1[j][k] = 0
l1 = prosort(l1)
for i in range(len(l1)):
    for j in range(len(l1[i])):
        l1[i][j] = round((l1[i][j]), 2)

for i in range(len(l1)):
    q = fnzz(i, l1)
    if q == "DNE":
        pass
    else:
        for j in range(len(l1[i])):
            l1[i][j] = round((l1[i][j]/q), 2)
        


z=[]
for i in l1:
    z.append(i)
    

for i in z:
    for j in i:
        if j!=0.0:
            a = j
            break
    for j in i:
        i[i.index(j)] = j/a


for i in z:
    for j in i:
        i[i.index(j)] = round(j, 2)
        
remove0(z)
z.sort(reverse=True)
print()
print("The RREF is:")
print(z)
print()
solutions(z)