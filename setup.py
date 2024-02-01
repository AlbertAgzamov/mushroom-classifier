from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
     Returns the list of requirements
    """

    with open(file_path, 'r') as file_obj:
        requirements = [req.replace('\n', '') for req in file_obj.readlines()]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements



with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'mushroom-classifier'
AUTHOR_USER_NAME = 'AlbertAgzamov'
SRC_REPO = 'MushroomBinaryClassifier'
AUTHOR_EMAIL = 'agzamov.albert.1998@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A Python package for binary classification of mushrooms, helping to determine their edibility.',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    packages=find_packages(),
    # package_dir={'': 'src'}
    install_requires=get_requirements('requirements.txt')
)
