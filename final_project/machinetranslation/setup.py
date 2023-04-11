from setuptools import setup, find_packages

setup(
    name='mytranslator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ibm-watson>=5.2.2',
        'flask>=2.0.2',
        'flask-restful>=0.3.9'
    ],
    url='https://github.com/shazadladha/mytranslator',
    license='MIT',
    author='Shazad Ladha',
    author_email='shazadladha@gmail.com',
    description='A package for translating text using IBM Watson Language Translator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
