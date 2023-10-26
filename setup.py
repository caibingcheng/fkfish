from setuptools import setup, find_packages
import os
import time

current_timestamp = time.time()
version = os.environ.get('VERSION', '')
if version == '':
    raise Exception('VERSION environment variable not set')

# the original version is refs/tags/V0.6.2
# version must be PEP 440 compliant
version = version.replace('refs/tags/V', '')
print('Version: {}'.format(version))

setup(
    name='fkfish',
    version=version,
    author="caibingcheng",
    author_email="jack_cbc@163.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fkfish = fkfish.__main__:main'
        ]
    }
)
