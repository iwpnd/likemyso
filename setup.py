from setuptools import setup

packages = ["likemygf"]

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="likemygf",
    version="0.0.1",
    description="like your girlfriends instagram pictures you scumbag",
    url="http://github.com/iwpnd/likemygf",
    author="Benjamin Ramser",
    author_email="ahoi@iwpnd.pw",
    license="MIT",
    include_package_data=True,
    install_requires=required,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Instahusbands",
    ],
    entry_points="""
        [console_scripts]
        likemygf=likemygf.main:cli
    """,
)
