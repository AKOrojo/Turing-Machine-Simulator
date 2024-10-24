from setuptools import setup, find_packages

setup(
    name="turing_machine",
    version="0.1",
    packages=find_packages(include=['turing_machine', 'turing_machine.*']),
    python_requires=">=3.6",
)