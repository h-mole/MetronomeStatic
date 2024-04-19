import setuptools

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setuptools.setup(
    name="PyBirdViewCode",
    version="0.1.0",
    description="A pure-python (Python>=3.8) static analysis library providing various interfaces.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hzyrc6011/PyBirdViewCode",
    author="hzyrc6011",
    author_email="1295752786@qq.com",
    license="MIT",
    # For classifiers, refer to:
    # https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Documentation": "https://hzyrc6011.github.io/PyBirdViewCode/",
    },
    packages=setuptools.find_namespace_packages(
        include=["PyBirdViewCode", "PyBirdViewCode.*"]
    ),
    install_requires=[
        "clang~=16.0",
        "libclang~=16.0",
        "six",
        "psutil",
        "flask",
        "flask-sock",
        "networkx",
        "tqdm",
        "MelodieFuncFlow",
        "ply",
        "dataclasses_json",
        "pydot",
        "strenum ; python_version<='3.11'",
        "websocket-client",
        "requests",
        "termcolor"
    ],
    python_requires=">=3.8",
    include_package_data=True,
)
