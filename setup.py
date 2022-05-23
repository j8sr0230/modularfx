from setuptools import setup

setup(
    name='modularfx',
    version='0.1',
    packages=['modularfx'],
    package_data={
        'modularfx': [
            'icons/*',
            'examples/*',
        ],
    },
    entry_points={
        'console_scripts': [
            'modularfx=modularfx.gui:main',
        ]
    },
    install_requires=['gensound', 'pygame', 'nodeeditor', 'QtPy', 'PyQt5'],
    url='https://github.com/ali1234/modularfx',
    license='GPL',
    author='Alistair Buxton',
    author_email='a.j.buxton@gmail.com',
    description='Modular synthesizer.'
)
