from os.path import dirname, join
from setuptools import setup

with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

def read(fname):
    return open(join(dirname(__file__), fname)).read()

setup(name='scraper',
      version='0.1.0',
      author="Chad Dotson",
      author_email="chad@cdotson.com",
      description="A collection of tools to scrap content from web pages.",
      license="GNUv3",
      keywords="scraping download images",
      url="https://github.com/chaddotson/scraper",
      packages=['web_scraper', 'bin'],
      long_description=read("README.md"),
      install_requires=install_reqs,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'scrape_cli = bin.scrape_cli:main',
          ],
          'gui_scripts': [
              'scrape_gui = bin.scrape_gui:main',
          ],
      },
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
)
