import pandas as pd

teste = pd.read_excel('output.xlsx')

df = pd.DataFrame(teste)

s = pd.Series(df["nome_sgp"])

s = s.dropna()   

lista_dois_primeiros_nomes = list()

for x in s.index:
    nome_sgp = s.loc[x]    
    if nome_sgp != '':
       nomes_pessoa_sgp = nome_sgp.split(' ')
       dois_primeiros_nomes_sgp = nomes_pessoa_sgp[0] + ' ' + nomes_pessoa_sgp[1]
       if dois_primeiros_nomes_sgp not in lista_dois_primeiros_nomes:      
           lista_dois_primeiros_nomes.append(dois_primeiros_nomes_sgp)           
           df.loc[x,"nome_sgp"]=''
       else:
           df.loc[x,"nome_sgp"]=''           

for x in df.index:
    nome_rh = df.loc[x,"nome_rh"]
    if nome_rh != '':
        nomes_pessoa_rh = nome_rh.split(' ')
        dois_primeiros_nomes_rh = nomes_pessoa_rh[0] + ' ' + nomes_pessoa_rh[1] 
        if dois_primeiros_nomes_rh not in lista_dois_primeiros_nomes:
            df.drop(x, inplace = True) 
        else:
            for i in s.index:
                nome_sgp = s.loc[i]
                nomes_pessoa_sgp = nome_sgp.split(' ')
                dois_primeiros_nomes_sgp = nomes_pessoa_sgp[0] + ' ' + nomes_pessoa_sgp[1]
                if dois_primeiros_nomes_sgp == dois_primeiros_nomes_rh:
                    df.loc[x,"nome_sgp"] = nome_sgp  
                    break                

df.to_excel (r'regra2.xlsx',index = False)