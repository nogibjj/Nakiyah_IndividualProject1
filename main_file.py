from mylib.lib import (
    readData,
    cleanData,
    summaryStatistics,
    PiePlot,
    tripleBarPlot,
)

# Create Variables
Data = "FT Global Business School MBA Ranking 2024.csv"
ColumnsWantedForSummaryStats = [
    "Value for money rank",
    "Salary percentage increase",
    "Overall satisfaction **",
]
ColumnsForDataset = [
    "#",
    "School Name",
    "International students (%)",
    "International faculty (%)",
    "Value for money rank",
    "Career progress rank",
    "Careers service rank",
]
Rank = "#"  # Column for sorting
SchoolName = "School Name"
requiredrank = 10
PctIntlStudents = "International students (%)"
PctIntlFaculty = "International faculty (%)"
RankNames = "Value for money rank", "Career progress rank", "Careers service rank"
university_column = "School Name"

# Create Functions
Dataset = readData(Data)
SummaryStatistics = summaryStatistics(Dataset, ColumnsWantedForSummaryStats)
CleanData = cleanData(Dataset, Rank, ColumnsForDataset, requiredrank)
piePlotStudents = PiePlot(CleanData, PctIntlStudents, SchoolName)
piePlotFaculty = PiePlot(CleanData, PctIntlFaculty, SchoolName)
BarChart = tripleBarPlot(CleanData, SchoolName, RankNames)

print(SummaryStatistics)
