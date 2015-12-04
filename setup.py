from setuptools import setup, find_packages


setup(
    name='normdatei',
    version='0.2',
    description="Reference data for the German parliament",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3'
    ],
    keywords='bundestag popolo reference data',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/bundestag/normdatei',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'six',
        'normality'
    ],
    tests_require=[],
    test_suite='test',
    entry_points={
    }
)
