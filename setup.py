from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
	print("[Error] Please use python --version greater 3")
	exit(1)


setup(
	name="manager",
	version=open('manager/version.py').read(),
	description=('Simple process manager in python'),
	url='https://github.com/breath2live/manager',

	author='Sam Classix',
	author_email='infobreath2live@gmail.com',
	license=open('LICENSE').read(),

	long_description=open('README.md').read(),
	#packages=find_packages(),
	packages=['manager'],
	include_package_data=True,

	install_requires=['numpy', 'pandas']
)
