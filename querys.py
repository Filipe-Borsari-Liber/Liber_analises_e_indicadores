from Conect_portal import cnn, cnn1
import pandas as pd

query_sacados_analytics = f"""
           SELECT buyer_cnpj_root, buyer_trade_name, buyer_economic_group_name, buyer_size, entry_date, buyer_cnpj, buyer_economic_group_segment
            FROM rs_buyer   """

query_prospeccao_analytics = f"""
           SELECT cnpj_sacado, razao_social_sacado_em_prospeccao
           from pipefy_seller_prospecting_all_cards;  """



query_sacados_portal = f"""
           select distinct
            id,
            company,
            cnpj,
            cnpj_root,
            trade_name
            from Sacados
            order by 5"""

bd_prospeccao_analytics = pd.read_sql(query_prospeccao_analytics, cnn, coerce_float=True)
bd_sacados_analytics = pd.read_sql(query_sacados_analytics, cnn, coerce_float=True)
bd_sacados_portal = pd.read_sql(query_sacados_portal, cnn1, coerce_float=True)

