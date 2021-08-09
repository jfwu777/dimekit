import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='dimekit',
    version='0.0.1',
    author='Junfeng Wu',
    author_email='jfwu.ai@gmail.com',
    description='A lightweight toolkit package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jfwu777/dimekit",
    project_urls={
        "Bug Tracker": "https://github.com/jfwu777/dimekit/issues"
    },
    license="BSD",
    packages=["dimekit"]
    install_requires=[],
)