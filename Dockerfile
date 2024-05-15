FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

# Create the environment from the environment.yml file
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"] 

COPY . .
EXPOSE 8000
CMD ["conda", "run", "-n", "myenv", "gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
