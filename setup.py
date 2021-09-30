from setuptools import setup

setup(
    name='Homework-2b-Group-23',
    version='0.1',
    description='Homework to create a good repository',
    author='Parth Vijaykumar Patel',
    author_email='pvpatel2#ncsu.edu',
    packages=['code'],
        long_description="""\
            Hands on for the standard github repo files.
            .gitignore
            .travis.yml
            CITATION.md : fill on once you've got your ZENODO DOI going
            CODE-OF-CONDUCT.md
            CONTRIBUTING.md
            LICENSE.md
            README.md
            setup.py
            requirements.txt
            data/
              README.md
            test/
              README.md
            code/
              __init__.py
        """,
        classifiers=[
            "License :: MIT License",
            "Programming Language :: Python",
            "Development Status :: Initial",
            "Intended Audience :: Developers",
            "Topic :: Software Engineering",
        ],
        keywords='python requirements license gitignore',
        license='MIT',
        install_requires=[
            'numpy',
            'pytest',
            'configparser',
        ],
        )
