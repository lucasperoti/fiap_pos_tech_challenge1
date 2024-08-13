# Usando uma imagem base do Python
FROM python:3.12

# Definindo o diretório de trabalho no container
WORKDIR /code

# Instalando o Poetry
RUN pip install poetry

# Copiando os arquivos de configuração do Poetry
COPY pyproject.toml poetry.lock /code/

# Instalando as dependências com o Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copiando o restante do código da aplicação
COPY . /code/

# Comando padrão para rodar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
