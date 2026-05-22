from setuptools import find_packages,setup
from typing import List

def get_requriments()->List[str]:
    """
        This will return list of of requriments.txt 
    
    """
    requirement_list:List[str] = []

    try:
        with open('requirements.txt','r')as file:
            ## Read lines from file
            lines = file.readlines()
            for l in lines:
                requirement=l.strip()
                ## ignore empty line
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("File Not Found")
    
    return requirement_list

print(get_requriments())


setup(
    name = "Networksecurity",
    version="0.0.1",
    author="Aviral",
    author_email="gaviral172@gmail.com",
    packages=find_packages(),
    install_requires=get_requriments()
)
