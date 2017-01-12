from setuptools import setup, find_packages

setup(
    name='convert_zero_one_based',
    version='0.0.1',
    description='Convert between zero and one based coordinate systems and '
                'vice versa',
    url='https://github.com/bainscou/convert_zero_one_based',
    author='Ben Ainscough',
    author_email='b.ainscough@wustl.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning'
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python :: 3.5.2'
    ],
    packages=find_packages()
)
