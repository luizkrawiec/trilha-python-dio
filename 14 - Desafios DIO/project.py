from setuptools import setup, find_packages
python setup.py sdist bdist_wheel
pip install twine
twine upload dist/*



# meu_pacote/__init__.py
from .modulo import minha_funcao

# meu_pacote/modulo.py
def minha_funcao():
    print("Olá, este é o meu pacote!")


setup(
    name="meu_pacote",
    version="0.1.0",
    author="Seu Nome",
    author_email="seu.email@example.com",
    description="Um pacote simples em Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/seuusuario/meu_pacote",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


