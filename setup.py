from setuptools import find_packages,setup 

setup(
    name='mcqgenratorf',
    version='0.0.1',
    author='prabha',
    author_email='prabhapuneet@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)

