from setuptools import setup

with open("requirements.txt", "r'") as f:
    install_reqs = f.readlines()

setup(name='Scraper',
      version='1.0',
      packages=['web_scraper', 'bin'],
      install_requires=install_reqs,
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'scrape_cli = bin.scrape_cli:main',
          ],
          'gui_scripts': [
              'scrape_gui = bin.scrape_gui:main',
          ],
      }
)
