import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel(r'C:\Users\diego.santos\Documents\diego-projetos\helpDiih\este.xlsx', skiprows=1)

engine = create_engine('postgresql://humboldt:humboldt_1234@127.0.0.1:1234/humboldt?sslmode=disable')
df.to_sql('testing_new_dados_humboldt', engine, if_exists='replace', index=False)