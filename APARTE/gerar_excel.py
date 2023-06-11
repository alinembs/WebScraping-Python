import pandas as pd
import numpy as np

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
df.to_csv("/home/aline/Documentos/Projetos/teste.csv", index=False)