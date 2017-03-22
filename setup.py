from setuptools import setup

setup(
    name='myqueue',
    version='0.0.1',
    long_description=__doc__,
    packages=['myqueue'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['python_dotenv', 'pyqs']
)