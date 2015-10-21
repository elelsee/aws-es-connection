from setuptools import setup, find_packages


setup(name='aws-es-connection',
      version='0.2',
      description='Python Elasticsearch Client connection class for AWS Elasticsearch Service',
      author='Scott VanDenPlas',
      author_email='scott@elelsee.com',
      url='https://github.com/elelsee/aws-es-connection',
      packages=find_packages(),
      py_modules=['awses'],
      install_requires=['boto', 'elasticsearch'])
