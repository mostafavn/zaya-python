import setuptools

setuptools.setup(
    name="zaya",
    packages = ['zaya'],
    version="1.0.5",
    license='MIT',
    description="zaya Library",
    author="Shabakeh Sazan Tousan LLC",
    author_email="info@zaya.io",
    url="https://zaya.io",
    download_url='https://github.com/tousanco/python-zaya.git',
    keywords=['zaya', 'zaya.io', 'tousanco'],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[''],
    platforms=['any'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    	'Environment :: Console',
    	'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
