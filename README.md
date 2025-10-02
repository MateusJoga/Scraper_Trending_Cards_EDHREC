## Título do Projeto

Coletor de Cartas em Tendência no EDHREC

## Descrição

Este projeto é um coletor de dados web (web scraper) desenvolvido em Python que extrai a lista de **cartas em tendência** do EDHREC, um recurso popular para o formato Commander de Magic: The Gathering. Ao monitorar essas cartas em alta, jogadores e colecionadores podem obter insights antecipados sobre quais cartas estão ganhando popularidade, potencialmente indicando futuros aumentos de preço no mercado secundário.

O script busca automaticamente a lista atual de cartas em tendência na página inicial do EDHREC e as salva em um arquivo de texto para facilitar a análise e exportação no devido formato para o LigaMagic.

## Começando

### Pré-requisitos

- **Python 3**: Certifique-se de ter o Python instalado em sua máquina.
- **Bibliotecas Python**: Este script requer os seguintes pacotes Python:
  - `requests` - Usado para buscar o conteúdo HTML do site EDHREC.
  - `beautifulsoup4` - Usado para analisar o HTML e extrair os dados relevantes.

### Instalação

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/MateusJoga/Scrapper_Trending_Cards.git
   ```
3. **Instale as Bibliotecas Necessárias usando o `requirements.txt`**
  ```bash
   pip install -r requirements.txt
   ```
### Executando o Programa

1. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.
2. Execute o script usando o interpretador Python.
   ```bash
   python Cartas.py
   ```
4. Após uma execução bem-sucedida, o script criará um novo arquivo chamado `trending_cards.txt` no mesmo diretório. Este arquivo conterá a lista de cartas atualmente em tendência no EDHREC.

## Visão Geral do Código

O script fornecido funciona da seguinte maneira:

1. **Busca a Página Web**: Usa a biblioteca `requests` para recuperar o conteúdo HTML da página inicial do EDHREC (`https://edhrec.com/`).
2. **Analisa o HTML**: O conteúdo recuperado é analisado usando BeautifulSoup com o `html.parser` integrado do Python.
3. **Extrai as Cartas em Tendência**: O script navega pela estrutura HTML analisada para localizar a seção específica que contém a lista de cartas em tendência.
4. **Salva os Dados**: Ele grava os nomes das cartas em tendência em um arquivo `trending_cards.txt`, com cada carta em uma nova linha.

## Notas Importantes

- **Ética na Coleta de Dados Web**: Esta ferramenta é destinada para uso pessoal e educacional. Por favor, respeite os servidores do EDHREC não executando o coletor excessivamente. Sempre revise o arquivo `robots.txt` e os Termos de Serviço de um site antes de coletar dados.
- **Mudanças na Estrutura do Site**: Esteja ciente de que se o EDHREC atualizar a estrutura do seu site, o coletor pode precisar ser ajustado para continuar funcionando corretamente.

## Autor

- Desenvolvido por Mateus Grandel/MateusJoga

## Histórico de Versões

- 1.0
- Versão inicial
