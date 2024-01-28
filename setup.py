import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_desc = f.read()
    
__version__ = "0.0.0"

repo_name = "Kidney-Disease-classification"
auther_name = "AnilKumar-06"
src_repo = "Kidney-Disease-classification-DVC-MLflow"
auther_email = "anilmt06@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=auther_name,
    author_email=auther_email,
    description="A small package for kidney disease classification",
    long_description=long_desc,
    long_description_content = "text/markdown",
    url = f"https://github.com/{auther_name}/{repo_name}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{auther_name}/{repo_name}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)