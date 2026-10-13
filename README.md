# Sales Data Analyzer & Visualization Tool

A menu-driven Python application for loading, exploring, cleaning, analyzing, and visualizing sales data using **Pandas, NumPy, Matplotlib, and Seaborn**. The project provides an interactive interface for performing common data analysis operations on CSV datasets, generating statistical insights, and creating visualizations directly from the command line.

## Overview

The Sales Data Analyzer is designed to simplify exploratory data analysis (EDA) and basic sales data processing. Users can load a CSV file, inspect its structure, handle missing values and duplicate records, calculate descriptive statistics, perform NumPy operations, search and filter records, generate visualizations, and create pivot tables.

The project also demonstrates object-oriented programming concepts in Python through inheritance, method overriding, and operator overloading.

## Features

### 1. Data Loading

* Load sales datasets from CSV files.
* Handle common missing-value representations, including empty strings, `NULL`, `NA`, and `None`.
* Handle file-not-found and empty-file errors.
* Store the loaded dataset in a Pandas DataFrame.

### 2. Data Exploration

* Display the first five rows of the dataset.
* Display the last five rows.
* View column names and data types.
* Generate basic descriptive statistics.
* Inspect the dataset's dimensions (rows and columns).

### 3. Data Cleaning

* Identify and display rows containing missing values.
* Fill missing numerical values using column means.
* Remove rows containing missing values.
* Identify duplicate rows.
* Remove duplicate records.

### 4. Statistical and Mathematical Analysis

Calculate statistical measures for selected columns:

* Maximum and minimum values.
* Mean, median, and mode.
* Standard deviation and variance.
* Quantiles using values between 0 and 1.
* Percentiles using values between 0 and 100.

These operations help users understand the distribution and characteristics of individual dataset columns.

### 5. NumPy Analysis

Perform numerical operations using NumPy:

* Convert a Pandas DataFrame into a NumPy array.
* Calculate the mean, median, and standard deviation of numerical data.
* Access array elements using row and column indices.
* Split arrays into multiple sections.

### 6. Column Splitting

* Split a selected column using a user-defined delimiter.
* Specify names for the resulting columns.
* Validate the number of new column names against the number of generated columns.
* Add the resulting columns to the existing dataset.

For example, a column containing `Ahmedabad-Gujarat` can be split using `-` into separate location and state columns.

### 7. Search, Sort, and Filter

* Search for exact matches in a selected column.
* Sort records by a specified column in ascending or descending order.
* Filter records using Pandas query expressions.

Examples of filter expressions:

```python
Sales > 1000
Quantity >= 5
Region == 'West'
```

Use column names and values that exist in your loaded dataset.

### 8. Matplotlib Visualizations

Generate the following charts interactively:

* Line plot
* Bar plot
* Histogram
* Scatter plot
* Pie chart
* Stack plot

The application allows users to save generated plots to image or document formats supported by Matplotlib, such as PNG and PDF.

### 9. Seaborn Visualizations

Create additional visualizations for exploratory analysis:

* Pair plot
* Correlation heatmap
* Box plot
* Violin plot
* Count plot

These charts help identify relationships between numerical variables, distributions, potential outliers, and category frequencies.

### 10. Pivot Table

Generate a pivot table by selecting:

* An index column.
* A values column.
* An aggregation function.

Supported aggregation functions:

* `mean`
* `sum`
* `count`
* `max`
* `min`

### 11. Advanced Sales Analyzer

The `AdvancedSalesAnalyzer` class extends `SalesDataAnalyzer` and introduces additional object-oriented functionality:

* **Inheritance:** Reuses the functionality of the base analyzer.
* **Method overriding:** Extends data exploration by displaying descriptive statistics for all columns.
* **Method reuse:** Allows users to access the standard exploration menu from the advanced analyzer.
* **Operator overloading:** Implements the `+` operator to combine two analyzer datasets through row-wise concatenation.

## Technologies Used

| Technology | Purpose                                                            |
| ---------- | ------------------------------------------------------------------ |
| Python     | Core programming language                                          |
| Pandas     | Data loading, cleaning, manipulation, statistics, and pivot tables |
| NumPy      | Numerical computations and array operations                        |
| Matplotlib | Data visualization and plot saving                                 |
| Seaborn    | Statistical visualization                                          |

## Project Structure

```text
Sales-Data-Analyzer/
│
├── main.py          # Main application and analyzer classes
├── sales_data.csv   # Example dataset (optional)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

The filenames above are suggested conventions. Adjust them to match the actual files in your repository.

## Installation

### Prerequisites

* Python 3.9 or later recommended.
* pip package manager.
* A CSV dataset for analysis.

### Step 1: Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Sales-Data-Analyzer
```

Replace `<YOUR_REPOSITORY_URL>` with your repository's Git URL.

### Step 2: Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Alternatively, create a `requirements.txt` file containing:

```text
numpy
pandas
matplotlib
seaborn
```

Then install the dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run

Execute the Python file containing the application:

```bash
python main.py
```

If your file has a different name, replace `main.py` with the correct filename.

The application displays the main menu:

```text
==========================================================
Welcome to the Sales Data Analyzer & Visualization Tool
==========================================================

1. Load Sales Data
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Values and Duplicates
5. Generate Descriptive Statistics
6. Numpy Analysis
7. Split Column Data
8. Search, Sort, and Filter
9. Visualize with Matplotlib
10. Visualize with Seaborn
11. Create Pivot Table
12. Exit
```

Enter the corresponding menu number to select an operation.

## Usage Guide

### Step 1: Load a dataset

Select option `1` and enter the path to your CSV file.

Example:

```text
Enter the path to the CSV file: sales_data.csv
```

You can also provide an absolute path to a dataset stored elsewhere on your computer.

### Step 2: Explore the data

Select option `2` to inspect the dataset's rows, columns, data types, shape, and basic statistics.

### Step 3: Clean the dataset

Select option `4` to review missing values, fill numerical missing values with means, remove incomplete rows, or remove duplicate records.

**Note:** Cleaning operations modify the analyzer's DataFrame directly. Save a copy of the original CSV if you need to preserve the source data.

### Step 4: Perform statistical analysis

Select option `3`, choose a statistical operation, and enter a valid column name.

For quantiles, enter a number between `0` and `1`. For percentiles, enter a number between `0` and `100`.

### Step 5: Generate visualizations

Choose option `9` for Matplotlib or option `10` for Seaborn. Follow the prompts to select columns and generate the desired chart.

When prompted, you can choose to save the plot before displaying it.

### Step 6: Create a pivot table

Select option `11`, enter the index and values column names, and choose an aggregation function.

### Step 7: Exit

Select option `12` to exit the application.

## Example Dataset

You can use a CSV file with columns such as the following to explore the application's capabilities:

```csv
OrderID,Product,Region,Quantity,Sales
1001,Laptop,West,2,1200
1002,Mouse,North,5,150
1003,Keyboard,South,3,240
1004,Monitor,East,2,500
1005,Headphones,West,4,320
```

Save this sample as `sales_data.csv` and load it through the main menu.

The example supports operations such as:

* Exploring product sales by region.
* Calculating mean, median, and maximum sales.
* Sorting records by sales amount.
* Filtering records with conditions such as `Sales > 300`.
* Plotting quantity against sales.
* Creating a pivot table using `Region` as the index and `Sales` as the values, aggregated by `sum`.

## Error Handling

The application includes exception handling for common runtime situations, including:

* Missing CSV files.
* Empty CSV files.
* Invalid menu selections.
* Incorrect column names.
* Invalid filter expressions.
* Errors encountered during plotting, data processing, and file saving.

Input validation is implemented in the interactive menus, although certain operations may require additional validation for unsupported data types or invalid numerical parameters.

## Important Implementation Notes

The following details are relevant when running the current version of the project:

1. **Column splitting:** The `split_data()` method currently accepts three parameters in its definition, but the main menu calls it without arguments. Update the method to collect input internally without required parameters, or pass the required arguments when calling it.

2. **NumPy calculations:** Mean, median, and standard deviation are calculated across all selected numerical columns together. The numerical results therefore represent the combined numerical array rather than a statistic for one specific column.

3. **Missing values:** Filling missing values with means affects numerical columns only. Missing values in non-numerical columns remain unchanged.

4. **Statistical operations:** Statistical calculations are most appropriate for numerical columns. Operations on non-numerical columns may return errors or unsuitable results, depending on the operation and data type.

5. **Plot saving:** The program asks whether to save a plot before calling `plt.show()`. Choose `yes` and provide a filename such as `sales_chart.png` to save it.

6. **Advanced analyzer:** Option `5` in the main menu displays the extended descriptive statistics provided by `AdvancedSalesAnalyzer`.

7. **Dataset combination:** The overloaded `+` operator combines two analyzer datasets by stacking their rows. It does not merge records based on matching keys.

8. **Data persistence:** The program does not currently provide an option to export a cleaned or transformed DataFrame back to CSV. Changes made during the session remain in memory unless explicitly saved by adding an export operation.

## Future Enhancements

Potential improvements for future versions include:

* Add CSV export functionality for cleaned and transformed datasets.
* Support Excel file imports and exports.
* Add interactive dashboards using Streamlit or another visualization framework.
* Provide grouped sales summaries by product, region, and date.
* Add time-series analysis and sales trend forecasting.
* Improve validation for numerical columns, quantiles, percentiles, and array dimensions.
* Add automated unit tests for data processing and statistical methods.
* Add logging and more informative error messages.
* Improve chart customization with additional styling and export options.

## Learning Objectives

This project demonstrates practical applications of:

* Object-oriented programming in Python.
* Data manipulation using Pandas.
* Numerical computing using NumPy.
* Statistical analysis and descriptive analytics.
* Data visualization using Matplotlib and Seaborn.
* Exception handling and interactive command-line menus.
* Inheritance, method overriding, and operator overloading.

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test the functionality.
5. Submit a pull request with a description of the improvements.

## License

No license has been specified for this project yet. If you plan to publish it publicly, consider adding a `LICENSE` file and selecting an appropriate open-source license.

## Author

**NIDHESH DUBEDI**


* Project: Sales Data Analyzer & Visualization Tool

Replace the author details with your own information before publishing the repository.
