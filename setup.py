import setuptools

setuptools.setup(
    name="pythonhost",
    packages = ['pythonhost'],
    version="1.0.5",
    license='MIT',
    description="pythonhost Library",
    author="pythonhost Co",
    author_email="info@pythonhost.ir",
    url="https://pythonhost.ir",
    download_url='https://github.com/pythonhost/pythonhost.git',
    keywords=['pythonhost', 'pythonhost.ir', 'ftp', 'python', 'host'],
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
