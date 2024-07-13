from setuptools import find_packages, setup

LINT_REQUIREMENTS = []
SRC_REQUIREMENTS = []
TEST_REQUIREMENTS = []

with open("requirements/requirements-lint.txt", "r", encoding="utf-8") as f:
    LINT_REQUIREMENTS = f.read().splitlines()

with open("requirements/requirements-src.txt", "r", encoding="utf-8") as f:
    SRC_REQUIREMENTS = f.read().splitlines()

with open("requirements/requirements-tests.txt", "r", encoding="utf-8") as f:
    TEST_REQUIREMENTS = f.read().splitlines()

setup(
    name="watcher-scanner-service",
    use_scm_version=True,
    description="Tool to automate the launch of various security scans",
    install_requires=SRC_REQUIREMENTS,
    extras_require={
        "lint": LINT_REQUIREMENTS,
        "tests": TEST_REQUIREMENTS
    },
    packages=find_packages(
        include=[
            "src.*"
        ]
    )
)
