from setuptools import find_packages, setup

setup(
    name="dt",
    version="1.1.69",
    packages=find_packages(include=["dynatrace*"]),
    install_requires=["requests>=2.22"],
    tests_require=["pytest", "mock", "tox"],
    python_requires=">=3.6",
    author="David Lopes",
    author_email="davidribeirolopes@gmail.com",
    description="Dynatrace API Python client",
    long_description="Dynatrace API Python client",
    url="https://github.com/dlopes7/dynatrace-rest-python",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",  # 2.0
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Topic :: Software Development",
    ],
    project_urls={"Issue Tracker": "https://github.com/dlopes7/dynatrace-rest-python/issues"},
)
