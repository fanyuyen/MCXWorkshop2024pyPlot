from setuptools import setup, find_packages

setup(
    name='MCXWorkshop2024pyPlot', 
    version='0.1.0',  
    author='Fan-Yu Yen', 
    author_email='yen.f@northeastern.edu', 
    description='Plotting utilities for MCX Workshop 2024',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fanyuyen/MCXWorkshop2024pyPlot',
    packages=find_packages(),
    install_requires=[
        'numpy', 
        'matplotlib',
        'plotly'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
    keywords='plotting, 3D, matplotlib, plotly, workshop',
)

