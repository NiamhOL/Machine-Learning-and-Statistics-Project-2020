# Machine-Learning-and-Statistics-Project-2020

## Student: Niamh O'Leary
## ID: G00376339

## Contents of Github Repository
1. README file
2. MLSProject.ipynb - Jupyter Notebook containing research, overview of data, models and references
3. Assessment.pdf - pdf document outlining the project
4  Powerproduction.csv - data used in analysis and running the models
5. Images -  images used in the tasks
6. Requirements.txt
7. Dockerfile
8. server.py 
9. wind_speed- wind model
10. Images included in the project

## Overview of Project

In this project focuses on creating a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to
produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with
predicted power values based on speed values sent as HTTP requests. 

## Getting started
Download and install Python and Anaconda, all files associated with this project are available at https://github.com/NiamhOL/Machine-Learning-and-Statistics-Project-2020

## Packages used in this project

The following packages were used to run statistical analysis and draw grpahs for this project.

* Python https://www.python.org/downloads/
* Anaconda https://www.anaconda.com/distribution/ - is the easiest way to perfrom Python data science machine learning on Linux, Windows and Mac OS.
* iPython https://ipython.org/ - it an interactive command-line terminal for Python.
* Numpy http://www.numpy.org/ - is the fundamental package for scientific computing within Python.
* Jupyter Notebook https://jupyter.org/ - is an open-source web application that allows the creation and sharing of documents that contains live code, equations, visualisations    and narriative text
* import pandas as pd https://pandas.pydata.org/
* import scipy.stats as stats https://docs.scipy.org/doc/scipy/reference/stats.html
* import matplotlib.pylab as plt https://matplotlib.org/
* from sklearn.model_selection import ....https://scikit-learn.org/stable/
* from from tensorflow.keras.models import ......https://keras.io/about/#keras-amp-tensorflow-20
* from tensorflow.keras.layers import......https://keras.io/about/#keras-amp-tensorflow-20

## Running the web service

In Cmdr navigate to the project folder and run the following commands to create a FLASK enviornment.

#### Virtual environment
Conda was used to create a localhost Virtual Environment (venvMLP) for running the server. The following Windows command line python commands can be to create venvMLP, install and save packages for venvMLP, set the flask_app server and server mode, run the server, stop the server and finally deactivate venvMLP.

* λ conda create --name venvMLP python=3.8
* λ conda activate venvMLP
* (venvMLP)λ pip install flask
* (venvMLP)λ pip install tensorflow
* (venvMLP)λ pip install silence-tensorflow
* (venvMLP)λ pip install numpy==1.19.2
* (venvMLP)λ pip freeze > requirements.txt
* (venvMLP)λ set FLASK_APP=web-server.py
* (venvMLP)λ set FLASK_ENV=development
* (venvMLP)λ python -m flask run
Running on http://127.0.0.1:5000/

![image](https://raw.githubusercontent.com/NiamhOL/Machine-Learning-and-Statistics-Project-2020/main/Capture.PNG)
![image](https://raw.githubusercontent.com/NiamhOL/Machine-Learning-and-Statistics-Project-2020/main/tensorflow.png)
![image](https://raw.githubusercontent.com/NiamhOL/Machine-Learning-and-Statistics-Project-2020/main/flask2.png)

Copy the URL and open a web browser. 

## Author
Niamh O'Leary for HDip in Data Analytics 2019/2020.

## Licence
This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.

