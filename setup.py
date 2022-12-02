from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='scam_spotter',
      version="0.0.9",
      description="Scam Spotter",
      license="MIT",
      author="not Le Wagon",
      author_email="not contact@lewagon.org",
      url="https://github.com/Dimitrakis999/Scam_Spotter",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
