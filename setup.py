from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="auto_parts_manager",
    version="1.0.0",
    description="ERPNext app for selling auto parts with VIN search",
    author="ERPBox",
    author_email="support@erpbox.online",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)