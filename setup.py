# This file relies on https://github.com/pypa/sampleproject
# as a draft implementation that is 'pretty good' to start with.

from setuptools import setup, find_packages

PROJECT_DESCRIPTION = "pyFIRI is a Python3 implementation of the FIRI-2018, \
a semi-empirical model of the non-auroral Earth's ionosphere D-Region."

PROJECT_DESCRIPTION_LONG = """
pyFIRI is a Python3 implementation of the FIRI-2018 (Faraday‐International
Reference Ionosphere), a semi-empirical D-Region model of the non-auroral 
Earth's ionosphere. Previous version of the FIRI (FT-2001) is incorporated
into a well-known mature International Reference Ionosphere (IRI, https://iri.gsfc.nasa.gov/ ) 
model.

If you use FIRI-2018 or pyFIRI directly or indirectly, please, cite in your research
the following paper:

Friedrich, M., Pock, C., & Torkar, K. (2018). FIRI‐2018, an updated empirical model 
of the lower ionosphere. Journal of Geophysical Research: Space Physics, 123, 6737– 6751. 
https://doi.org/10.1029/2018JA025437

pyFIRI provides a thin Python3 wrapper around the tabulated electron density Ne profiles supplied 
together with the research paper by Friedrich et al.(2018, https://doi.org/10.1029/2018JA025437 ). 
For internal data representation, selection, and interpolation pyFIRI relies on xarray.DataArray 
( https://xarray.pydata.org/ ) facilities.

"""

setup(
    # this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name='pyfiri',

    # Versions should comply with PEP 440, https://www.python.org/dev/peps/pep-0440/
    version='0.0.1b7',
    description=PROJECT_DESCRIPTION,
    long_description=PROJECT_DESCRIPTION_LONG,
    # long_description_content_type='text/markdown', - some bug with markdown - displayed not correctly
    url='https://gitlab.com/zolotov/pyfiri',  # homepage
    license='Apache Software License',  # to remove 'license: UNKNOWN' notice
    platform=['any'],
    author='Oleg Zolotov',
    author_email='zolotovo@gmail.com',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',

        # License
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='lower ionosphere of the Earth, D-region, D-layer, model, FIRI',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['scipy', 'xarray'],  # Optional

    # Automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
    packages=find_packages(),  # include/exclude arguments take * as wildcard, . for any sub-package names

    package_data={'pyfiri': [r'_ext/_data/firi2018ed2.nc']},
    include_package_data=True
)

# To generate wheel, a command for the terminal:
# python setup.py bdist_wheel
