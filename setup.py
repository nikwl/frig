import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="frig",
    version="0.0.1",
    author="Nikolas lamb",
    author_email="nikolas.lamb@gmail.com",
    description="Figure cReation Is God-awful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikwl/frig",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)