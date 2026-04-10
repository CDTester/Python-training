import pandas as pd
import matplotlib.pyplot as plt

print("\nSeries:")
series_a = [1,7, 2]
print("series_a =", series_a)

my_series = pd.Series(series_a)
print("pd.Series(series_a) =\n", my_series)

print("\nLabels:")
print("Without labels, use the index to get value. my_series[1] =", my_series[1])
my_labeled_series = pd.Series(series_a, index = ["x", "y", "z"])
print("With labels, use the index to get value. my_labeled_series[y] =", my_labeled_series["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
print("calories =", calories)
my_series_keyvalue = pd.Series(calories)
print("pd.Series(calories) =\n", my_series_keyvalue)


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

mydataframe = pd.DataFrame(mydataset)

print("mydataset =", mydataset)
print("\nDataFrame:")
print("pd.DataFrame(mydataset) =\n", mydataframe)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
print("data =", data)
my_dataframe_cal = pd.DataFrame(data, index= ["day1", "day2", "day3"])

print("\npd.DataFrame(mydataset, index= [\"day1\", \"day2\", \"day3\"]) =\n", my_dataframe_cal)

print("\nlocate Row with default index, mydataframe.loc[1] =\n", mydataframe.loc[1])
print("\nlocate Row with custom index, my_dataframe_cal.loc[\"day2\"] =\n", my_dataframe_cal.loc["day2"])

print("\nlocate Rows with default index, mydataframe.loc[[1,2]] =\n", mydataframe.loc[[1,2]])
print("\nlocate Rows with custom index, my_dataframe_cal.loc[\"day1\",\"day3\"] =\n", my_dataframe_cal.loc[["day1", "day3"]])

print("\nLoad CSV file intoa a DataFrame:")
my_csv_df = pd.read_csv("../test_data/people.csv")
print("pd.read_csv(\"../test_data/people.csv\") =\n", my_csv_df)

print("\ndefault max_rows - pd.options.display.max_rows:", pd.options.display.max_rows)

my_large_csv_df = pd.read_csv("../test_data/health.csv")
print("\nmy_large_csv_df = pd.read_csv(\"../test_data/health.csv\") =\n", my_large_csv_df)

pd.options.display.max_rows = 200
print("\nset max_rows to 200, pd.options.display.max_rows:", pd.options.display.max_rows)
#my_large_csv_df = pd.read_csv("../test_data/health.csv")
print("\nmy_large_csv_df =\n", my_large_csv_df)

print("\nLoad JSON file into a DataFrame:")
my_json_df = pd.read_json("../test_data/health.json")
print("pd.read_json(\"../test_data/health.json\") =\n", my_json_df.to_string())


print("\nhead() - return the first n rows of the DataFrame, default n=5")
print("my_json_df.head(10) =\n", my_json_df.head(10))

print("\ntail() - return the last n rows of the DataFrame, default n=5")
print("my_json_df.tail(10) =\n", my_json_df.tail(10))

print("\ninfo() - return a concise summary of the DataFrame")
print("my_json_df.info() =\n", my_json_df.info())

print("\nDropna - remove rows with missing values")
new_json = my_json_df.dropna()
print("new_json = my_json_df.dropna() \n", new_json)

print("\nCorrelation - compute pairwise correlation of columns, excluding NA/null values")
new_json_corr = new_json.corr()
print("new_json.corr() =\n", new_json_corr)

print("\nPlotting - plot the data using matplotlib")
new_json.plot()
plt.show()