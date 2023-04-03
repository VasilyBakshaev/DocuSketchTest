# DocuSketch Test task
## Content

`plots` - a folder that stores graphics saved by the function

`data_overview` - file with an overview of the example data

`func` - .py file containing the function

`Notebook` - file with an example of the function's operation

`test.py` - a Unit-test file

## Description

According to the task, a function was created that converts a JSON file link to a DataFrame, builds plots based on this DataFrame, saves them in a separate folder, and returns a list of paths to these graphics.

Due to the lack of information about the required plots, the function outputs the first 15 rows by room names for each column with deviations. This behavior of the function can be easily changed when the requirements are clarified.

When writing the function, it was assumed that the appearance, format, column order, and other data would not differ from the example provided.

## Installation

1. Clone this repository.
2. Open new terminal at project folder.
3. Create a virtual environment by entering `python3 -m venv venv` in the terminal.
4. Activate virtual environment by entering `source ./venv/bin/activate`.
5. Install requirements by entering `python3 -m pip install -r requirements.txt`

## Usage of the Script

1. Open new terminal at project folder.
2. Enter in Python Console by typing `python3`.
3. Import function by typing `from func import plot_drawer`
4. Create an instance of the plot_drawer class `drawer = plot_drawer()`
5. Run function by typing `drawer.draw_plots('YOUR-JSON-URL')` (Replace `YOUR-JSON-URL` with a link to the JSON file.)

...or import the function to a Jupyter notebook and use it there.

## Running Unit Test

1. Open new terminal at project folder.
2. Run Unit-test by typing `python3 test.py` in the terminal.