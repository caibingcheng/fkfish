from setuptools import setup, find_packages

setup(
    name='fkfish',
    version="0.1",
    author="bbing",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fkfish = fkfish.__main__:main'
        ]
    }
)
