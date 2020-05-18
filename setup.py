from setuptools import setup

packages = ["likemyso"]

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="likemyso",
    version="0.0.1",
    description="like your significant others instagram pictures, you scumbag",
    url="http://github.com/iwpnd/likemyso",
    author="Benjamin Ramser",
    author_email="ahoi@iwpnd.pw",
    license="MIT",
    include_package_data=True,
    install_requires=required,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: InstaSOs",
    ],
    entry_points="""
        [console_scripts]
        likemyso=likemyso.main:app
    """,
)
