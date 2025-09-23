import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

HYPEN_DOT_E = "-e ."
def get_requirements(file_path: str) -> List[str]:
    '''This function will return a list of requirements
    '''
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements

__version__ = "1.0.0"
Project_name = "ChickenDisease"
AUTHOR_USERNAME = "13-suraj"
SRC_REPO = "my-deep-learning-project-1"
AUTHOR_EMAIL = "surajkeshari260@gmail.com"

setuptools.setup(
    name=Project_name,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Chicken Disease Classifier using CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USERNAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements("requirements.txt")
)