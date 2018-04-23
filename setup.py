from setuptools import setup

setup(
    name='verbscounter',
    version='0.0.1',
    description='top verbs in project counter',
    license='MIT',
    packages=['verbscounter'],
    author='Roman Dze',
    author_email='ivastapas@gmail.com',
    keywords=['verbs'],
    install_requires=[
        'os', 'nltk', 'ast', 'ast', 'collections', 'logging'
    ],
    url='https://github.com/romandze/verbscounter'
)
