# setup.py

from setuptools import setup, find_packages

setup(
    name='PAADPred',
    version='1.0',
    description='Package for PAAD patient prediction using machine learning models',
    author='Rohit',
    author_email='rohit17145@iiitd.ac.in',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'PAADPred': ['models/*.pkl'],
    },
    install_requires=[
        'pandas',
        'joblib',
        'scikit-learn',
    ],
    license='MIT',
)

