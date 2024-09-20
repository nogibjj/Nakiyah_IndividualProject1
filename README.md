# Nakiyah_MiniProject1

[![Install](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/install.yml)

[![Format](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/format.yml)

[![Lint](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/test.yml)

# Week 3

## Technologies Used
- **Python 3.x**
- **Jupyter Notebook**
- **Pandas**
- **Matplotlib**

## Installation
To run this project, ensure you have Python 3.x and the necessary libraries installed. 

You can install the required libraries using the following command:
```
pip install -r requirements.txt
```

## Usage
1. Clone this repository:
    ```bash
    git clone https://github.com/nogibjj/Nakiyah_MiniProject1.git
    ```
2. Navigate into the directory:
    ```bash
    cd Nakiyah_MiniProject1
    ```
3. Open the Jupyter notebook:
    ```bash
    jupyter notebook
    ```

The repository skeleton:
```
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
├── .github/workflows
│   ├── install.yml
│   ├── format.yml
│   ├── lint.yml
│   ├── test.yml
├── mylib/
│   ├── lib.py
├── .gitignore
├── FT Global Business School MBA Ranking 2024.csv
├── Makefile
├── README.md
├── Requirements.txt
├── main_file.ipynb
├── main_file.py
├── test_file.py
└── test_lib.py
```

## Overview
This repository analyzes the FT Global Business School MBA Ranking 2024 dataset. The project uses Python for data processing, visualization, and automated testing, with additional support for containerized development and a CI/CD pipeline.

## Functions inside the main.py
- readData(df): Reads a CSV file into a DataFrame.
- cleanData(df, Columns, Duplicate): Cleans the data by removing duplicates and selecting specified columns.
- summaryStatistics(df): Generates descriptive summary statistics, including median, for numeric columns in the DataFrame.
- stackPlot(df, xVal, StackVal): Creates a stacked bar plot based on two categorical variables.
- barPlot(df, xVal, yVal, Segregate): Produces a horizontal bar plot showing the average of one variable grouped by two others.


## Repository contents:
1. .devcontainer directory (a) devcontainer.json (b) Dockerfile
2. .github/worflows/cicd.yml --> this is configuration file that defines the steps necessary to build, test, and deploy an application.
3. .gitignore --> to ensure some cache files like "pychache" do not get pushed to the github repo.
4. Makefile --> which sets rules to manage the dependencies of the source files of the programs during the compilation and linking (build) phase.
5. Requirements.txt --> contains a list of packages/libraries needed to work on this project that can all be installed with the file.
6. main.py --> Reads a CSV file, generates descriptive summary statistics, and produces data visualizations.
7. test_main.py --> Tests the functionality of main.py by verifying the accuracy of the descriptive summary statistics and the correctness of the generated visualizations





The code and notebooks can be run locally for analysis. The notebooks provide detailed comments and insights into the data analysis process.


