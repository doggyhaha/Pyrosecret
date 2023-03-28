import re
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open('pyrogram_secret_chat/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE)[1]


setup(
    name='pyrogram_secret_chat',
    packages=find_packages(),
    version=version,
    license='MIT',
    description='Pyrogram secret chat plugin',
    author='doggy',
    long_description=long_description,
    url='https://github.com/doggyhaha/pyrogram-secret-chat',
    download_url='https://github.com/doggyhaha/pyrogram-secret-chat/releases',
    keywords=['Telegram', 'Pyrogram', 'SecretChats', 'Plugin'],
    install_requires=[
        'pyrogram', 
        'tgcrypto',
    ],

    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
)
