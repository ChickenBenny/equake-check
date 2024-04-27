from setuptools import setup, find_packages

setup(
    name='earthquake-check',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'equake = equake.api:main'
        ],
    },
    author='ChickenBenny',
    author_email='zxc123benny14159@gmail.com',
    description='A package for checking earthquake information in Taiwan.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChickenBenny/equake-check',
    classifiers=[
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'pydantic'
    ],
)
