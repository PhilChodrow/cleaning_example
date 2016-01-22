# Sample data cleaning script

## Setup

Install Python if needed, version 2.7.* if possible. 
Install `pip`, Python's best package manager. Instructions [here](http://python-packaging-user-guide.readthedocs.org/en/latest/installing/#install-pip-setuptools-and-wheel).
Install pandas:

    pip install pandas

Note that this will probably install a bunch of other dependecies too. This is fine, but does hint at how we are using an oversized tool for the job. That's ok.

Clone this repo: 

    git clone https://github.com/PhilChodrow/cleaning_example.git

## Running the sample program

Open a terminal in the directory in which you cloned this repo and run
    
    python clean.py kern.csv

Currently, the program is structured so that you can add an arbitrary number of .csv files to read in, e.g. 

    python clean.py kern.csv fontana.csv

However, the specific cleaning function doesn't work with fontana.csv right now, so this will result in an error. The principle is there though. 
