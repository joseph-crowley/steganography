from setuptools import setup, find_packages

setup(
    name='steganography',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'steganography = steganography.cli:cli',
        ],
    },
    author='Joseph Crowley',
    author_email='joe@fattailed.ai',
    description='A CLI tool for encoding and decoding messages in images using LSB steganography',
    url='https://github.com/joseph-crowley/steganography',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

