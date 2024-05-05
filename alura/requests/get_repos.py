import requests
import pandas as pd

class DadosRepositorios:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.url_base = 'https://api.github.com'
        self.token = ''
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': f'Bearer {self.token}'}

    def lista_repositorios(self):
        pages = []

        for page in range(1,20):
            try:
                url = f'{self.url_base}/users/{self.owner}/repos?page={page}'
                r = requests.get(url, headers=self.headers)
                pages.append(r.json())
            except:
                pages.append(None)

        return pages
    
    def nomes_repos(self, pages):
        repos_name = []
        
        for page in pages:
            for repo in page:
                repos_name.append(repo['name'])

        return repos_name
    
    def nomes_linguagens(self, pages):
        languages = []

        for page in pages:
            for repo in page:
                languages.append(repo['language'])
        return languages
    

    def cria_dataframe(self):
        repos = self.lista_repositorios()
        nomes = self.nomes_repos(repos)
        linguagens = self.nomes_linguagens(repos)

        df = pd.DataFrame()
        df['repository'] = nomes
        df['language'] = linguagens

        return df

amazon = DadosRepositorios('amzn')
df_amazon = amazon.cria_dataframe()
netflix = DadosRepositorios('netflix')
df_netflix = netflix.cria_dataframe()
spotify = DadosRepositorios('spotify')
df_spotify = spotify.cria_dataframe()

#Gerando csv
df_amazon.to_csv('dados/amazon.csv')
df_netflix.to_csv('dados/netflix.csv')
df_spotify.to_csv('dados/spotify.csv')

