# convert_zero_one_based
Python CLI to convert between zero and one based coordinate systems

## Install Anaconda

1. You can find an installer to Anaconda [here](https://store.continuum.io/cshop/anaconda/) for your distribution (macOS, Linux, windows).
2. Download the installer and follow the instructions.

## Install convert_zero_one_based

1. Clone this repo

		git clone https://github.com/griffithlab/convert_zero_one_based.git
2. Add conda-forge channel to build dependencies

		conda config --add channels conda-forge 
3. Use Anaconda to build the tool

		cd convert_zero_one_based
		conda build .
4. Copy the filepath of the built package from the `conda build .` command. `/Users/<YOUR_USERNAME>/anaconda/conda-bld/osx-64/convert_zero_one_based-0.0.1-py35_0.tar.bz2` in the example below.

		# If you want to upload this package to anaconda.org later, type:
		#
		# $ anaconda upload /Users/<YOUR_USERNAME>/anaconda/conda-bld/osx-64/convert_zero_one_based-0.0.1-py35_0.tar.bz2
		#
		# To have conda build upload to anaconda.org automatically, use
		# $ conda config --set anaconda_upload yes
5. Install the tool locally

		conda install /Users/<YOUR_USERNAME>/anaconda/conda-bld/osx-64/convert_zero_one_based-0.0.1-py35_0.tar.bz2
		
6. Verify the install

		convert_zero_one_based --help
