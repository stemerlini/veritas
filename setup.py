from setuptools import setup, find_packages

setup(
    name="veritas",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click>=8.0",
        "pyyaml>=6.0",
        "gitpython>=3.1",
        "python-frontmatter=1.1.0",
        "fuzzywuzzy>=0.18",
        "pytest>=7.0",
        "pytest-cov>=3.0"
    ],
    entry_points={
        "console_scripts": [
            "ver = veritas.main:cli"
        ]
    },
)