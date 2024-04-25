from setuptools import setup

__version__ = None
exec(open('socialNet_backend_protobuf/version.py').read())


setup(
    name='socialnet-backend-protobuf',
    version=__version__,
    description='Protobuf3 definitions for SERVICE_NAME Service',
    packages=['socialNet_backend_protobuf'],
    include_package_data=True,
    install_requires=[],

)
