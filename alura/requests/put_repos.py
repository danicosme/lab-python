import requests
import base64

class ManipulaRepositorios:
    def __init__(self, username) -> None:
        self.username = username
        self.url_base = 'https://api.github.com'
        self.token = ''
        self.headers = {'X-GitHub-Api-Version': '2022-11-28', 'Authorization': f'Bearer {self.token}'}

    def cria_repo(self, name):
        url = f'{self.url_base}/user/repos'
        
        data = {
        'name': name,
        'description': 'Repositório com linguagens de programação da Amazon.',
        'private': False
        }

        r = requests.post(url, headers = self.headers, json=data)
        
        print(f'Status da criação do repositório: {r.status_code}')
    
    def add_arquivo(self, repo, arquivo, path):
        with open(arquivo, 'rb') as f:
            file = f.read()
        
        enconded = base64.b64encode(file)
        username = self.username
        repo = repo
        path = path


        url = f'{self.url_base}/repos/{username}/{repo}/contents/{path}'

        data = {
            'message': 'Adicionando um novo arquivo',
            'content': enconded.decode('utf-8')
        }

        response = requests.put(url, json=data, headers=self.headers)
        response.status_code

repo = ManipulaRepositorios('danicosme')

repo.add_arquivo('alura-requests-linguagens', 'dados/amazon.csv', 'amazon.csv')
repo.add_arquivo('alura-requests-linguagens', 'dados/spotify.csv', 'spotify.csv')
repo.add_arquivo('alura-requests-linguagens', 'dados/netflix.csv', 'netflix.csv')