from setuptools import setup, find_namespace_packages
setup(
    name="PhaseMotif",
    version="0.1",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        'torch>=2.0',
        'torchvision',
        'pandas',
        'numpy',
        'scikit-learn',
        'umap-learn',
        'matplotlib',
        'seaborn',
        'scipy',
    ],
    python_requires='>=3.6',

)
