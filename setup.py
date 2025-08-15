from setuptools import setup, find_packages

setup(
    name='randomprocesses',
    version='0.1.0',
    author='Carson Waites',
    author_email='carsonrwaites@gmail.com@example.com',
    description='A set of univariate random processes that can be visualized and utilized in a few lines of code, with options for number of simulations, discretization (for continuous processes), drift and volatility parameters, and more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/carsonrwaites/random-processes',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.06',
)