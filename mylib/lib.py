import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Functions library
"""

def readData(df):
    return pd.read_csv(df, encoding="ISO-8859-1")

def summaryStatistics(df, Col):
    df = df[Col]
    SumStats = df.describe(exclude=["O"]).reset_index()
    Median = df.median(numeric_only=True)
    Median_df = pd.DataFrame(Median).T  # Transpose to match the structure of SumStats
    SumStats = pd.concat([SumStats, Median_df], ignore_index=True)
    SumStats.fillna("median", inplace=True)
    SumStats.set_index("index", inplace=True)
    return SumStats

def cleanData(df, ColToSort, Columns, RanksRequired):
    # Convert sorting column to numeric (ignoring errors) and sort by that column
    df[ColToSort] = pd.to_numeric(df[ColToSort], errors="coerce")
    df1 = df.sort_values(by=ColToSort).dropna()
    df1 = df1[Columns].head(RanksRequired)
    return df1


def PiePlot(df, col, labels_col, name):
    data = df[[col, labels_col]].dropna().sort_values(by=col, ascending=False)
    values = data[col]
    labels = data[labels_col]
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"Breakdown of {col} by School", pad=40)
    plt.axis("equal")
    plt.savefig(name, bbox_inches='tight')
    return "Pie Chart displayed"


def tripleBarPlot(df, Col, RankCols, name):
    num_ranks = len(RankCols)
    universities = df[Col]  # No of Universities
    barWidth = 1 / (num_ranks + 1)
    r = np.arange(len(universities))
    plt.figure(figsize=(16,16))

    for i, rank_col in enumerate(RankCols):
        plt.bar(
            r + i * barWidth,
            df[rank_col],
            width=barWidth,
            edgecolor="grey",
            label=rank_col,
        )


    plt.xlabel("Universities", fontweight="bold")
    plt.ylabel("Rank")
    plt.title("University Rank Comparison")
    plt.xticks(
        r + (num_ranks / 2 - 0.5) * barWidth, universities, rotation=45, ha="right"
    )
    plt.legend(loc="upper right", bbox_to_anchor=(1, 1))
    plt.savefig(name, bbox_inches='tight')
    return "Bar Chart Displayed"