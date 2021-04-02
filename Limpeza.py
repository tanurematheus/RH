import pandas as pd

teste = pd.read_excel('data.xlsx')

teste = teste.fillna('')

df = pd.DataFrame(teste)

nomes_sgp = list()

for x in df.index:
    nome_sgp = df.loc[x,"nome_sgp"]
    if nome_sgp != '':
        if nome_sgp not in nomes_sgp:      
           nomes_sgp.append(nome_sgp)
           df.loc[x,"nome_sgp"] = ''  
        else:
            df.loc[x,"nome_sgp"] = ''             
      
for x in df.index:
    nome_rh = df.loc[x, "nome_rh"] 
    if nome_rh in nomes_sgp:
        df.loc[nome_rh, "nome_rh"] = ''
        nomes_sgp.remove(nome_rh)

for x in df.index:
    nome_rh = df.loc[x, "nome_rh"]
    nome_sgp = df.loc[x, "nome_sgp"]  
    if nome_rh == nome_sgp:
        df.drop(x, inplace = True)

i=0
for x in nomes_sgp:
    df.loc[i, "nome_sgp"] = x
    i+=1 

df.to_excel (r'output.xlsx',index = False)