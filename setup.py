from setuptools import setup, find_packages

setup(
    name='gpt4all-tone',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        "argparse",
        "gpt4all",
    ],
    author='Evgenii Evstafev',
    author_email='chigwel@gmail.com',
    description='A comprehensive tool for sentiment analysis and tone review, empowered by GPT4ALL.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/gpt4all-tone',
    entry_points={
        'console_scripts': [
            'gpt4all_tone = gpt4all_tone.gpt4all_tone:main',
        ],
    },
)
