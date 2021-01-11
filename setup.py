# load libs
from setuptools import setup
import contain

# read in README.md
with open("description.md", "r") as fh:
    long_description = fh.read()

# catch the version
current_version = contain.__version__

# define the setup
setup(name='contain',
      version=current_version,
      description='Containerization for Python APIs',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/till-io/contain',
      author='Lukas Jan Stroemsdoerfer',
      author_email='ljstroemsdoerfer@gmail.com',
      license='MIT',
      packages=['contain'],
      zip_safe=False)