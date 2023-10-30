import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teslasdk",
    version="0.0.1",
    author="JSpiner",
    author_email="jspiner@naver.com",
    description="TeslaSdk",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JSpiner/TeslaSdk",
    project_urls={
        "Bug Tracker": "https://github.com/JSpiner/TeslaSdk",
    },
    keywords="tesla teslaapi tesla-api teslasdk tesla-sdk vehicles teslamotors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=["test_key.json"]
    ),
    python_requires=">=3.6",
    install_requires=["requests"]
)
