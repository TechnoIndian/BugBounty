import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="BugBounty",
	version="2.0",
	author="RK_TECHNO_INDIA",
	author_email="TechnoIndia786@gmail.com",
	description="BugBounty for Internet Freedom (Domain Fronting, Server Name Indication, Etc)",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Technoindian/BugBounty",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.12',
	entry_points={
		'console_scripts': [
			'BugBounty=BugBounty.__main__:main',
		],
	},
)
