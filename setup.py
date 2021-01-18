import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="harmony-api-client-python",
    author="blockjoe, gretha",
    author_email="joehabel46@gmail.com",
    description="A python client for interacting with Harmony endpoints.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blockjoe/harmony-api-client-python",
    packages=setuptools.find_packages(),
    license="Apache License 2.0",
    python_requires=">=3.7",
    install_requires=[
        'pydantic',
        'requests',
        'rosetta-api-client-python @ git+https://github.com/blockjoe/rosetta-api-client-python#egg=rosetta-api-client-python',
        'typer[all]'
    ],
    extras_require = {
        'dev' : ['datamodel-code-generator', 'sphinx', 'sphinx-rtd-theme', 'm2r2', 'apispec', 'pytest']
    },
    entry_points = {
        'console_scripts' : ['harmony-cli=harmony.cli:main']
    }
)
