from setuptools import setup, find_packages

setup(
    name="pysmartlogger",
    version="0.1.0",
    author="Carlos Oliveira",
    author_email="carlos.j.oliver18@gmail.com",
    description="Smart AI logger with notifications for Telegram/Discord.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CarlosOliveira-23/pysmartlogger",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
