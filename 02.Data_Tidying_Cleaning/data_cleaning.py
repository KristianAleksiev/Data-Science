"""
1. Messy and tidy data
Important rules when using datasets:
- Columns - attributes, variables
- Rows - observations
- Cells - values (one observation of one feature)
All other data is called messy

Empirical rule for testing whether a dataset is tidy:
- Adding one more observation should create one new row

Pandas workflow
- Columns same data type
- One value in cell
- Tidy data

NaN - missing data

2. Operations on datasets
Sub-setting rows:
- Selecting rows (selection)
- First / last n records (observation)
- Random N records - x.sample(n=10)
- Smallest / largest n records in each column - x.nsmallest(3, "tmax"), x.nlargest(3, "tmax")
- Sub-setting by a boolean expression (predicate) x[x.y > 20]

Sub-setting columns:
- x["column_name"] - One column
- x[["column1, column2]] - Multiple columns

3. Cleaning data
Validation:

Transformation:
- Dimensionality reduction - Reducing the number of variables (features)
-- feature selection - selecting only useful columns
-- feature extraction - non-structured to structured data

- Feature engineering - Creating meaningful features
Error correction:
Outliers - Wrong data entry, wrong assumptions
Features:

4. Data tidying and cleaning as a process
"""