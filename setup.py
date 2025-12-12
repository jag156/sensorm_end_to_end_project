from setuptools import find_packages,setup

def get_requirements()->list[str]:# list of string
    requirement_list=list[str]=[]
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="jagruti",
    author_email="jagrutiparmar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  #["pymongo"]

)

