import pandas as pd

teste = pd.read_excel('output.xlsx')

teste = teste.fillna('')

df = pd.DataFrame(teste)

mylist = list()
mylist2 = list()

for x in df.index:
    a = df.loc[x,"nome_sgp"]
    if a != '':
       b = a.split(' ')
       c = b[0] + ' ' + b[1]
       if c not in mylist:      
           mylist.append(c)
           mylist2.append(a)
           df.loc[x,"nome_sgp"]=''
       else:
           df.loc[x,"nome_sgp"]=''   

"Regra 2 Se o primeiro nome for igual e o Segundo nome também = Nome RH e Nome spg = (50%)"
for x in df.index:
    a = df.loc[x,"nome_rh"]
    if a != '':
        b = a.split(' ')
        c = b[0] + ' ' + b[1] 
        if c not in mylist:
            df.loc[x,"nome_rh"] = ''
        else:
            for i in mylist2:
                y = i.split(' ')
                z = y[0] + ' ' + y[1]
                if c == z:
                    df.loc[x,"nome_sgp"] = i   

for x in df.index:
    a = df.loc[x, "nome_rh"]
    b = df.loc[x, "nome_sgp"]  
    if a is b:
        df.drop(x, inplace = True)    

df.to_excel (r'regra2.xlsx',index = False)
print(df)