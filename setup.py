from setuptools import setup, find_packages
import os
import time

current_timestamp = time.time()
version = os.environ.get('VERSION', 'UNKNOWN-{}'.format(current_timestamp))
print('Version: {}'.format(version))

setup(
    name='fkfish',
    version=version,
    author="bbing",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fkfish = fkfish.__main__:main'
        ]
    }
)
