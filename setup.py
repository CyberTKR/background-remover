from setuptools import setup, find_packages

setup(
    name='background-remover',
    version='0.1',
    description='A Python package for making the background of an image transparent',
    author='Tolga',
    author_email='tolg@cybertkr.com',
    url='https://github.com/CyberTKR/background-remover',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.2.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
