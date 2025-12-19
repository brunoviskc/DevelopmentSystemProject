import pandas as pd
import os

caminho_arquivo = os.path.join("..", "data", "ExportWPS_1.TXT")

def carregar_dados():
    try:
        df = pd.read_csv(caminho_arquivo, sep='\t', encoding='latin1')
        nomes = {
            'NIVEL_WPS': 'Nivel',
            'CODIGO_WPS': 'Codigo',
            'QTDE_WPS': 'Quantidade',
            'DESCRICAO_WPS': 'Descricao',
            'LARG_WPS': 'Largura',
            'ALT_WPS': 'Altura',
            'PROF_WPS': 'Profundidade',
            'COMP_WPS': 'Comprimento',
            'MATERIAL_WPS': 'Material',
            'USINAGEM_1_WPS': 'Usinagem_1',
            'USINAGEM_2_WPS': 'Usinagem_2',
            'LARG_TOP': 'Largura_topo',
            'CATEGORIA': 'Categoria',
            'IMAGEN': 'Imagem',
            'Unnamed: 14': 'Desconhecido',
        }
        df = df.rename(columns=nomes)
        nivel_3 = df[df['Nivel'] == 3]

        print("✅ Arquivo Carregado com Sucesso!")
        print(f"Total de linhas encontradas: {len(df)}")
        print("-" * 40)

        print("PRIMEIRAS 5 LINHAS:")
        print(df.head())

        print("-" * 40)
        print("COLUNAS:")
        print(df.columns.tolist())

        print("-" * 40)
        print("COLUNA NIVEL 3:")
        print(nivel_3)

        return df
    except FileNotFoundError:
        print(f"❌ ERRO: Arquivo não encontrado em: {os.path.abspath(caminho_arquivo)}")
        print("Dica: Verifique se o arquivo 'ExportWPS_1.TXT' está dentro da pasta 'data'.")
        return None

if __name__ == "__main__":
    dados = carregar_dados()        
    