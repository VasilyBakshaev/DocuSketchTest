# DocuSketch Test task
## Content

`plots` - a folder that stores graphics saved by the function

`venv` - virtual environment folder

`data_overview` - file with an overview of the example data

`func` - .py file containing the function

`Notebook` - file with an example of the function's operation

## Description

According to the task, a function was created that converts a JSON file link to a DataFrame, builds graphics based on this DataFrame, saves them in a separate folder, and returns a list of paths to these graphics.

I did not create a `class for drawing plots` because I did not consider it necessary (perhaps I did not understand why it was required). Just created a function.

Due to the lack of information about the required plots, the function outputs the first 15 rows by room names for each column with deviations. This behavior of the function can be easily changed when the requirements are clarified.

When writing the function, it was assumed that the appearance, format, column order, and other data would not differ from the example provided.