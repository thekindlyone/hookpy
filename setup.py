from setuptools import setup

setup(name='hookpy',
      version='0.1',
      description='x hook for keyboard and mouse',
      url='https://github.com/thekindlyone/hookpy',
      author='thekindlyone',
      author_email='dodo.dodder@gmail.com',
      license='GNU GPL v2',
      packages=['hookpy'],
      install_requires=[
          'python-xlib',
      ],
      zip_safe=False)