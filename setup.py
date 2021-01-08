import setuptools


def readme():
  with open('README.md', 'r') as f:
    return f.read()

setuptools.setup(
	
	name='devicepool',
    version='1.0.0',
    author='Ding Yi',
    author_email='dvdface@gmail.com',
    description='the package used to manage resources in the resource pool.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/dvdface/devicepool',
    license='MIT',
    python_modules=['devicepool'],
    test_suite='test_devicepool',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0'
)