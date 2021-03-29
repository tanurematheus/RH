import pandas as pd

teste = pd.read_excel('data2.xlsx')

teste = teste.fillna('')

df = pd.DataFrame(teste)

"retirada de elementos iguais"
for x in df.index:
    a = df.loc[x, "nome_rh"] 
    for y in df.index:  
        b =  df.loc[y, "nome_sgp"]       
        if a is b:          
           df.loc[x, "nome_rh"] = ''
           df.loc[y, "nome_sgp"] = ''

"retirada de linhas sem nomes"
for x in df.index:
    a = df.loc[x, "nome_rh"]
    b = df.loc[x, "nome_sgp"]  
    if a is b:
        df.drop(x, inplace = True)

df.to_excel (r'd:\output.xlsx',index = False)