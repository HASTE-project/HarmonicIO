from setuptools import setup

setup(name='harmonicIO',
      description='Lightweight stream processing engine for scientific data',
      version='0.3.0',
      install_requires=['falcon', # Web Framework
                        'urllib3>=1.22',
                        'docker'],
      packages=['harmonicIO',
                'harmonicIO.stream_connector',
                'harmonicIO.master',
                'harmonicIO.worker'],
      entry_points={
          'console_scripts': [
              'stream_connector = harmonicIO.stream_connector.__main__:main',
              'master = harmonicIO.master.__main__:main',
              'worker = harmonicIO.worker.__main__:main',
              'play = harmonicIO.play.__main__:main'
          ]
      },
      test_requires=[
          'pytest'
      ],
      project_urls={
          'source': 'https://github.com/HASTE-project/HarmonicIO',
          'homepage': 'http://haste.research.it.uu.se/',
      },
      )
