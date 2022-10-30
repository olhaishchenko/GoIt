from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='1',
    description='Very useful code',
    url='https://github.com/olhaishchenko/goit//modul7/clean_folder',
    author='Olha Ishchenko',
    author_email='olga.ua.olga@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sort']}
)