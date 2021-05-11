# This file relies on https://github.com/pypa/sampleproject
# as a draft implementation that is 'pretty good' to start with.

from setuptools import setup, find_packages

setup(
    # this will be the package name you will see, e.g. the output of 'conda list' in anaconda prompt
    name='pyfiri',

    # Versions should comply with PEP 440, https://www.python.org/dev/peps/pep-0440/
    version='0.0.1b1',
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
    install_requires=['xarray', 'scipy'],  # Optional

    # Automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
    packages=find_packages(),  # include/exclude arguments take * as wildcard, . for any sub-package names

    package_data={'pyfiri': [r'_ext/_data/firi2018ed2.nc']},
    include_package_data=True
)

# To generate wheel, a command for the terminal:
# python setup.py bdist_wheel
