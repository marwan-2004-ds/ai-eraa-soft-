# 28 Pandas Projects — Solutions

Solutions to the 28 pandas practice projects (EraaSoft AI 805, Lecture 24).
Each project is a Jupyter Notebook with every step solved and executed, so the outputs and charts are visible directly on GitHub.

## Tools
Python 3.13, pandas 2.3, NumPy, Matplotlib, Seaborn, yfinance.

## Repository structure

```
01_Getting_&_Knowing_Your_Data/
02_Filtering_&_Sorting/
03_Grouping/
04_Apply/
05_Merge/
06_Stats/
07_Visualization/
08_Creating_Series_and_DataFrames/
09_Time_Series/
10_Deleting/
11_Indexing/
```

Each topic folder contains one sub-folder per project with its `Exercises.ipynb` and any local data file.

## Completed projects

| # | Topic | Project | Skills practised |
|---|---|---|---|
| 1 | Getting & Knowing Your Data | Chipotle | shape, columns, value counts, type conversion with `apply` |
| 2 | Getting & Knowing Your Data | Occupation | `index_col`, `dtypes`, `describe`, frequencies |
| 3 | Getting & Knowing Your Data | World Food Facts | reading a large TSV, positional column access |
| 4 | Filtering & Sorting | Chipotle | boolean filters, `sort_values`, counting conditions |
| 5 | Filtering & Sorting | Euro 2012 | column selection, multi-column sort, `str.startswith`, `isin` |
| 6 | Filtering & Sorting | Fictional Army | `loc` / `iloc`, label and position slicing |
| 7 | Grouping | Alcohol Consumption | `groupby` with `mean`, `median`, `describe`, `agg` |
| 8 | Grouping | Occupation | group ratios, multi-key groups, `unstack` |
| 9 | Grouping | Regiment | hierarchical groups, `size`, iterating over groups |
| 10 | Apply | Students Alcohol Consumption | lambdas, `apply`, `map`, new columns from functions |
| 11 | Apply | US Crime Rates | datetime index, `resample` by decade |
| 12 | Merge | Auto MPG | `concat`, cleaning blank columns, random columns |
| 13 | Merge | Fictitious Names | `concat` by rows/columns, inner/outer `merge` |
| 14 | Merge | Housing Market | building DataFrames from Series, reindexing |
| 15 | Stats | US Baby Names | `groupby` + `sum`, `idxmax`, median, std, `describe` |
| 16 | Stats | Wind Stats | parsing dates, fixing centuries, missing values, weekly/monthly/yearly stats |
| 17 | Visualization | Chipotle | bar charts, scatter plots, bonus revenue chart |
| 18 | Visualization | Online Retail | data investigation, `FacetGrid`, price buckets with `pd.cut` |
| 19 | Visualization | Scores | sized and coloured scatter plots |
| 20 | Visualization | Tips | Seaborn `histplot`, `jointplot`, `pairplot`, `boxplot`, facets |
| 21 | Visualization | Titanic Disaster | pie chart, scatter by group, histograms |
| 22 | Creating Series & DataFrames | Pokemon | building DataFrames from dicts, column order |
| 23 | Time Series | Apple Stock | datetime index, `resample('BME')`, plotting |
| 24 | Time Series | Getting Financial Data | downloading stock data, MultiIndex, weekly aggregation |
| 25 | Time Series | Investor Flow of Funds US | frequency detection, monthly/yearly resampling |
| 26 | Deleting | Iris | setting and filling NaN, dropping columns/rows |
| 27 | Deleting | Wine | dropping columns by position, NaN handling, `reset_index` |
| 28 | Indexing | Chipotle | `loc`, `iloc`, `at`, `iat`, MultiIndex, `query` |

## Notes
- **World Food Facts** needs the Kaggle file `en.openfoodfacts.org.products.tsv` (about 1 GB, not included). Download it from <https://www.kaggle.com/openfoodfacts/world-food-facts> into the project folder and run the notebook.
- **Titanic Disaster** reads the bundled `train.csv` because the original online link now returns 404.
- **Investor Flow of Funds US** reads a pinned older version of the dataset, because the current file on the source repository is empty.
- **Getting Financial Data** uses `yfinance` instead of `pandas-datareader`, because the data-reader sources now require paid or registered API keys.
- **Indexing** came with empty step titles, so the indexing tasks in that notebook were defined as part of the solution.
- Random values (Auto MPG, Housing Market, Wine) use fixed seeds so results are reproducible.

## How to run
```bash
pip install pandas numpy matplotlib seaborn yfinance jupyter
jupyter notebook
```
