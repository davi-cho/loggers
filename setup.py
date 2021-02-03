from setuptools import setup, find_packages

setup(
    name='loggers',
    version='0.0.3',
    description='coleccion de logs usados en diferentes proyectos',
    url='git@https://github.com/davi-cho/logging_python.git',
    author='David Choque Llanos',
    author_email='davicho.llanos@gmail.com',
    license='...',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'loguru==0.5.3'
    ],
    zip_safe=False
)