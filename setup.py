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


setup(
    name='MushroomBinaryClassifier',
    version='0.0.1',
    description='A Python package for binary classification of mushrooms, helping to determine their edibility.',
    author='Albert Agzamov',
    author_email='agzamov.albert.1998@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
