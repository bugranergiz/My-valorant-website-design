from setuptools import setup

setup(
    name="Valorant",
    version="1.0.0",
    maintainer="Buğra Nergiz",
    maintainer_email="bugranergiz198@hotmail.com",
    packages=['Valorant'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"]
)