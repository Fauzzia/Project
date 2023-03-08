from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) ->List[str]:
    '''
    This function will return the requirement list
    '''
    hyphen = '-e .'
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace ("\n","") for req in requirements]
        
        if hyphen in requirements:
          requirements.remove(hyphen)
        
    return requirements
        
		

setup (
name = 'ML Project',
version ='0.0.1',
author = 'Fauzzia',
author_email='fauziakhan.mohamedabdulla@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)
