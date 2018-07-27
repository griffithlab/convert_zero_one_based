[![Build Status](https://travis-ci.org/griffithlab/convert_zero_one_based.svg?branch=master)](https://travis-ci.org/griffithlab/convert_zero_one_based)

# convert_zero_one_based
Python CLI to convert between zero and one based coordinate systems

# Installation

## Install Anaconda

1. You can find an installer to Anaconda [here](https://store.continuum.io/cshop/anaconda/) for your distribution (macOS, Linux, windows).
2. Download the installer and follow the instructions.

## Install from bioconda (easiest)

1. Add the bioconda channel
		
		conda config --add channels defaults
		conda config --add channels conda-forge
		conda config --add channels bioconda

2. Install
		
		conda install convert_zero_one_based
		
3. Verify the install

		convert_zero_one_based --help


## Build from source

1. Clone this repo

		git clone https://github.com/griffithlab/convert_zero_one_based.git
		
2. Add conda-forge channel to build dependencies

		conda config --add channels conda-forge 
		
3. Use Anaconda to build the tool

		cd convert_zero_one_based
		conda build meta.yaml
		
5. Install the tool locally

		conda install convert_zero_one_based --use-local
		
6. Verify the install

		convert_zero_one_based --help
