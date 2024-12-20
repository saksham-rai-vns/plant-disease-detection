import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.1'

REPO_NAME = 'plantDiseaseDetection'
AUTHOR_USER_NAME = 'saksham-rai-vns'
SRC_REPO = 'plant-disease-detection'
AUTHOR_EMAIL = 'sakshamrai1252.sr@gmail.com'


setuptools.setup(

    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Plant disease detection application',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')

)