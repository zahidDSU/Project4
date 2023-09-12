from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements
setup(

    name = "Project-04",
    version = "0.0.1",
    description = "This is project 4",
    author= "Zahid Hussain",
    author_email= "Zahid.dsu@gmail.com",
    packages=find_packages(),
    install_require = get_requirements("Requirements.txt")
)