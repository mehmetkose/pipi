from setuptools import setup

try:
    with open('README.rst') as f:
        long_description = f.read()
except IOError:
    long_description = ''

setup(
    name="pipi",
    version="0.0.5",
    description="shortcut install & freeze pip packages",
    long_description=long_description,
    author="Mehmet Kose",
    author_email="mehmet.py@gmail.com",
    url="https://github.com/mehmetkose/pipi",
    license="MIT",
    packages=['pipi'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    provides=['pipi'],
    entry_points = {
        'console_scripts': [
            'pipi = pipi.__init__:main'
        ],
    },
    test_suite = "tests"
)
