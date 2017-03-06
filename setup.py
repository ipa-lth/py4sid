from setuptools import setup

setup(
    name = "py4sid",
    version = "0.0.1",

    description = "subspace identification for linear systems.",

    # Project site
    url = "https://github.com/mattjj/py4sid",

    # Author details
    author = "Matthew Johnson",
    author_email = "mattjj@csail.mit.edu",

    # License info
    license = "new BSD",

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "Programming Language :: Python :: 3 :: Only",
    ],

    keywords = ["subspace identification"],
    
    packages = ['py4sid']
)

