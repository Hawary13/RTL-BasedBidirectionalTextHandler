import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BidiHandler",
    version="0.0.1",
    author="Hawary",
    author_email="hawary.1311@email.com",
    description="A Python clpackage handling the Arabic base bidirectional text.",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/Hawary13/RTL-BasedBidirectionalTextHandler",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=(
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ),
)