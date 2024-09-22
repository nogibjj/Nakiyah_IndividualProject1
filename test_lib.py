import pandas as pd
from io import StringIO
from main_file import (
    cleanData,
    summaryStatistics,
    PiePlot,
    tripleBarPlot,
)  # Replace 'your_module' with the actual name of your module

"""
Test Functions for data processing and visualization functions
"""

# Test summaryStatistics
def test_summaryStatistics():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pd.read_csv(StringIO(csv_data))

    summary = summaryStatistics(
        df, ["Value for money rank", "Career progress rank", "Careers service rank"]
    )

    # Check if the summary statistics contain the required metrics
    assert (
        summary.loc["mean", "Value for money rank"] == 16.0
    ), "Mean of Value for money rank is incorrect"
    assert (
        summary.loc["median", "Value for money rank"] == 15.0
    ), "Median of Value for money rank is incorrect"
    assert (
        summary.loc["mean", "Career progress rank"] == 15.0
    ), "Mean of Career progress rank is incorrect"
    assert (
        summary.loc["median", "Career progress rank"] == 15.0
    ), "Median of Career progress rank is incorrect"
    assert (
        summary.loc["mean", "Careers service rank"] == 15.0
    ), "Mean of Careers service rank is incorrect"
    assert (
        summary.loc["median", "Careers service rank"] == 15.0
    ), "Median of Careers service rank is incorrect"


# Test cleanData
def test_cleanData():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pd.read_csv(StringIO(csv_data))

    Columns = [
        "#",
        "School Name",
        "International students (%)",
        "International faculty (%)",
        "Value for money rank",
        "Career progress rank",
        "Careers service rank",
    ]
    CleanedData = cleanData(df, "#", Columns, 3)

    # Check if the cleaned DataFrame has the correct number of rows
    assert CleanedData.shape[0] == 3, "Number of rows in cleaned data is incorrect"
    assert all(col in CleanedData.columns for col in Columns), "Column filtering failed"


# Test PiePlot
def test_PiePlot():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pd.read_csv(StringIO(csv_data))
    try:
        PiePlot(df, "International students (%)", "School Name")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Pie plot failed: {e}")

    assert plot_success, "Pie plot generation failed"


# Test tripleBarPlot
def test_tripleBarPlot():
    csv_data = """#,School Name,International students (%),International faculty (%),Value for money rank,Career progress rank,Careers service rank
                  1,School A,30,20,10,20,15
                  2,School B,25,30,20,15,10
                  3,School C,20,25,15,10,20
                  4,School D,15,20,30,25,25
                  5,School E,35,40,5,5,5"""

    df = pd.read_csv(StringIO(csv_data))
    try:
        tripleBarPlot(
            df,
            "School Name",
            ["Value for money rank", "Career progress rank", "Careers service rank"],
        )
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Bar plot failed: {e}")

    assert plot_success, "Triple bar plot generation failed"
