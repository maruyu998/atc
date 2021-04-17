#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
	name="atc",
	version="1.0",
	description="atcoder auto run",
	url="https://github.com/maruyu998/atc",
	install_requires=["python-dotenv"],
	packages=find_packages(),
	entry_points={
		"console_scripts":[
			"atc = atc.atc:main"
		]
	},
	python_required=">3.8",
)