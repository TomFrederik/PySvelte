from setuptools import setup, find_packages

setup(
    name='pysvelte',
    version="1.0.0",
    packages=find_packages(),
    python_requires='>=3.6.0',
    install_requires=[
        'torch',
        'einops>=0.3.2',
        'numpy',
        "typeguard",    
    ]
)
