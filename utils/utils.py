import pandas as pd

#classe para inicialização do objeto, onde vamos carregar o arquivo, processar e modificar. 
class DataPipeline:
    def __init__(self, file_path, delimiter=';'):
        self.file_path = file_path
        self.delimiter = delimiter
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path, delimiter=self.delimiter)
        return self.data

    def preprocess(self):
        self.data['data'] = pd.to_datetime(self.data['data'], format='%d/%m/%Y')
        self.data = self.data[['data', 'valor_da_cotacao']].rename(columns={'data': 'ds', 'valor_da_cotacao': 'y'})
        return self.data
