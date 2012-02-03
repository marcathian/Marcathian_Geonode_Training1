import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="marcathian",
    version="0.1",
    author="Marcathian Alexander",
    author_email="marcathian@gmail.com",
    description="Sample project",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: BSD',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/marcathian/Marcathian_Geonode_Training1',
    scripts = [
               'scripts/marcathian',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
