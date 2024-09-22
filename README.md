# Week 3
# Nakiyah_MiniProject1

[![Install](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/install.yml)  [![Format](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/format.yml)  [![Lint](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/lint.yml)  [![Test](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Nakiyah_MiniProject1/actions/workflows/test.yml)


## File Structure 
```
Nakiyah_Assignment3/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   ├── workflows/format.yml
│   ├── workflows/install.yml
│   ├── workflows/lint.yml
│   ├── workflows/test.yml
├── mylib/
│   ├── lib.py
├── .gitignore
├── Makefile
├── main_file.py                                         
├── main_file.ipynb                                      
├── test_file.py                                    
├── test_lib.py                                     
├── requirements.txt                                
├── FT Global Business School MBA Ranking 2024.csv                  
├── International Students (%).png                              
├── International Faculty (%).png
├── University Rank Comparison.png
├── SummaryStats.png                             
```


## Overview
This repository analyzes the FT Global Business School MBA Ranking 2024 dataset. The project uses Python and jupyter notebook for data processing, visualization, and automated testing, with additional support for containerized development and a CI/CD pipeline.


## Functions Overview
- **`readData(df)`**: Reads a CSV file into a Polars DataFrame with specified encoding.

- **`summaryStatistics(df, Col)`**: Generates summary statistics, median, and mean for a specified column.

- **`cleanData(df, ColToSort, Columns, RanksRequired)`**: Sorts a DataFrame by a column and selects the top N rows for specified columns.

- **`PiePlot(df, col, labels_col)`**: Creates a pie chart showing the breakdown of a specified column by labels.

- **`tripleBarPlot(df, Col, RankCols)`** The tripleBarPlot function creates a grouped bar chart comparing the ranks of universities across multiple ranking columns


## Summary stats showing the results for inputed dataset:

![summaryStats](SummaryStats.png)


## Data Visualisation 

![piePlotFaculty](International Faculty (%).png)

![piePlotStudents](International Students (%).png)

![barChartUniversityRankings](University Rank Comparison.png)

The code and notebooks can be run locally for analysis. The notebooks provide detailed comments and insights into the data analysis process.


