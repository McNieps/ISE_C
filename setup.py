from setuptools import setup, find_packages


setup(name='isec',
      version='0.1',
      description='Pygame based game engine',
      author='McNieps',
      author_email='mcnieps@gmail.com',
      install_requires=['pygame-ce', 'pymunk', 'numpy'],
      include_package_data=True,
      packages=[*find_packages()],
      package_data={'isec': ["assets/*", "assets/*/*", "assets/*/*/*"]},
      )
