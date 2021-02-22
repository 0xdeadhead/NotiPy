from setuptools import find_packages
from setuptools import setup

def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()

setup(
    name="NotiPy",
    description="Telegram Notification cli utility",
    version="1.0.0",
    packages=find_packages(),
    install_requires=dependencies("requirements.txt"),
    entry_points={
        'console_scripts':[
            "NotiPy = NotiPy.Notify:main"
        ]
    }
)