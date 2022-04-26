from setuptools import setup

VERSION = "1.1.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="aws_costs_cli",
    version=VERSION,
    description="Command line tool to facilitate fetches and analises the AWS costs",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="AWS cost cli",
    url="https://github.com/danilocgsilva/aws-costs-cli",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["aws_costs_cli"],
    entry_points={"console_scripts": ["awscosts=aws_costs_cli.__main__:main"],},
    include_package_data=True
)

