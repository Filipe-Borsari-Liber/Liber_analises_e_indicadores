import pandas as pd
import json 
from querys import bd_sacados_portal, bd_sacados_analytics, bd_prospeccao_analytics

"""As variáveis devem vir do arquivo de conect com os bancos"""


df_sacados_analytics = bd_sacados_analytics
df_sacados_portal = bd_sacados_portal
df_prospeccao_analytics = bd_prospeccao_analytics


# Renomear colunas para CNPJ para facilitar visualização no merge
df_sacados_analytics = df_sacados_analytics.rename(columns={'buyer_cnpj': 'cnpj'})
df_sacados_portal = df_sacados_portal.rename(columns={'cnpj': 'cnpj'})
df_prospeccao_analytics = df_prospeccao_analytics.rename(columns={'cnpj_sacado': 'cnpj'})

# Criar um novo DataFrame combinando as informações com base no CNPJ
df_combined = pd.merge(df_sacados_analytics[['cnpj', 'buyer_trade_name', 'buyer_economic_group_name']],
                      df_prospeccao_analytics[['cnpj', 'razao_social_sacado_em_prospeccao']],
                      on='cnpj', how='left')

df_combined = pd.merge(df_combined,
                      df_sacados_portal[['cnpj', 'id', 'company', 'trade_name']],
                      on='cnpj', how='left')

# Reorganizar as colunas no DataFrame para colocar ID como segunda coluna
df_combined = df_combined[['cnpj', 'id', 'buyer_trade_name', 'buyer_economic_group_name', 'razao_social_sacado_em_prospeccao', 'company', 'trade_name']]

#renomeando alguns campos para facilitar visualização do df
df_combined = df_combined.rename(columns={
    'cnpj': 'CNPJ',
    'id': 'ID',
    'buyer_trade_name': 'buyer_trade_name_analytics',
    'buyer_economic_group_name': 'buyer_economic_group_name_analytics',
    'razao_social_sacado_em_prospeccao': 'razao_social_sacado_em_prospeccao',
    'company': 'company_portal',
    'trade_name': 'trade_name_portal'
})

# Crie uma nova coluna em branco chamada 'nova_coluna'
df_combined['Preenchimento Manual'] = ''

# Exibir o novo DataFrame
df_combined = df_combined.drop_duplicates()
df_combined.to_excel('testando_transcritora.xlsx', index=False)
