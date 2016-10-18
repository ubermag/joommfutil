from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='joommfutil',
    version='0.5.4.2',
    description='A JOOMMF utilities package.',
    long_description=readme,
    url='https://github.com/joommf/joommfutil',
    author='Computational Modelling Group',
    author_email='fangohr@soton.ac.uk',
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 'Topic :: Scientific/Engineering :: Physics',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3 :: Only']
)
