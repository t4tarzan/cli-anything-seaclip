"""Setup for cli-anything-seaclip — CLI harness for SeaClip-Lite."""

from setuptools import setup, find_packages

setup(
    name="cli-anything-seaclip",
    version="1.0.0",
    description="CLI-Anything harness for SeaClip-Lite project management",
    author="Vinayak",
    author_email="vinayak@whitenoiseacademy.com",
    python_requires=">=3.10",
    packages=find_packages(),
    install_requires=[
        "click",
        "prompt-toolkit",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "cli-anything-seaclip=cli_anything.seaclip.seaclip_cli:main",
        ],
    },
)
