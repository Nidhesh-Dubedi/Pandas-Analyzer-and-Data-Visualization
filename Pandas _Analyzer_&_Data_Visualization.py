import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    def __init__(self, data=None):
        self.data = data if data is not None else pd.DataFrame()

    def __del__(self):
        print("SalesDataAnalyzer object deleted.")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path, na_values=["", "NULL", "NA", "None"])
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except pd.errors.EmptyDataError:
            print("File is empty.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def explore_data(self):
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        while True:
            print("\n--- Data Exploration Menu ---")
            print("""
            1. Display the first 5 rows
            2. Display the last 5 rows
            3. Display the column names
            4. Display the data types 
            5. Display basic statistics
            6. Display shape of the dataset
            7. Return to main menu
            """)
            try:
                user_choice = int(input("Enter your choice (1-7): "))
                if user_choice == 1:
                    print(self.data.head())
                elif user_choice == 2:
                    print(self.data.tail())
                elif user_choice == 3:
                    print(list(self.data.columns))
                elif user_choice == 4:
                    print(self.data.dtypes)
                elif user_choice == 5:
                    print(self.data.describe())
                elif user_choice == 6:
                    print(self.data.shape)
                elif user_choice == 7:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def clean_data(self):
        """Clean the dataset by handling missing values and duplicates."""
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        while True:
            print("\n--- DATA CLEANING MENU ---")
            print("""
            1. Display rows with missing values
            2. Fill missing values with mean (numerical columns)
            3. Drop rows with missing values
            4. Show duplicate rows
            5. Drop duplicate rows
            6. Return to main menu
            """)
            try:
                user_choice = int(input("Enter your choice (1-7): "))
                if user_choice == 1:
                        missing_rows = self.data[self.data.isnull().any(axis=1)]
                        if not missing_rows.empty:
                            print("Rows with missing values:")
                            print(missing_rows)
                        else:
                            print("No rows with missing values found.")

                elif user_choice == 2:
                    before = self.data.isnull().sum().sum()
                    self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                    after = self.data.isnull().sum().sum()
                    if before > after:
                        print("Missing values filled with mean.")
                    else:
                        print("No numeric missing values to fill.")

                elif user_choice == 3:
                    before_rows = len(self.data)
                    self.data.dropna(inplace=True)
                    after_rows = len(self.data)
                    dropped = before_rows - after_rows
                    if dropped > 0:
                        print(f"{dropped} rows with missing values dropped.")
                    else:
                        print("No rows with missing values found. Nothing was dropped.")
                elif user_choice == 4:
                    duplicated = self.data[self.data.duplicated()]
                    if not duplicated.empty:
                            print("Rows with Duplicates values:")
                            print(duplicated)
                    else:
                            print("No rows with Dupliactes values found.")
                elif user_choice == 5:
                    before_rows = len(self.data)
                    self.data.drop_duplicates(inplace=True)
                    after_rows = len(self.data)
                    dropped = before_rows - after_rows
                    if dropped > 0:
                        print(f"{dropped} duplicate rows dropped.")
                    else:
                        print("No duplicate rows found. Nothing was dropped.")
                        print("Duplicate rows dropped.")
                elif user_choice == 6:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def Statistical_Maths_Analysis(self):
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        while True:
            print("\n--- STATISTICAL AND MATHEMATICAL ANALYSIS MENU ---")
            print("DataFrame Columns Names: ", ", ".join(self.data.columns))
            print("-----------------------------------------------------------")
            print("""
            1. Maximum Value of a Column
            2. Minimum Value of a Column
            3. Mean Value of a Column
            4. Median Value of a Column
            5. Mode Value of a Column
            6. Standard Deviation of a Column
            7. Variance of a Column
            8. Quantile
            9. Percentile
            10. Return to main menu
            """)
            try:
                user_choice = int(input("Enter your choice (1-10): "))
                if user_choice in range(1, 10):
                    col = input("Enter column name: ")
                    if col not in self.data.columns:
                        print(f"Column '{col}' does not exist.")
                        continue

                if user_choice == 1:
                    print(f"Maximum value in {col}: {self.data[col].max()}")
                elif user_choice == 2:
                    print(f"Minimum value in {col}: {self.data[col].min()}")
                elif user_choice == 3:
                    print(f"Mean value in {col}: {self.data[col].mean()}")
                elif user_choice == 4:
                    print(f"Median value in {col}: {self.data[col].median()}")
                elif user_choice == 5:
                    print(f"Mode value in {col}: {self.data[col].mode()[0]}")
                elif user_choice == 6:
                    print(f"Standard Deviation in {col}: {self.data[col].std()}")
                elif user_choice == 7:
                    print(f"Variance in {col}: {self.data[col].var()}")
                elif user_choice == 8:
                    q = float(input("Enter quantile (0–1): "))
                    print(f"Quantile {q} in {col}: {self.data[col].quantile(q)}")
                elif user_choice == 9:
                    p = float(input("Enter percentile (0–100): "))
                    print(f"Percentile {p} in {col}: {np.percentile(self.data[col].dropna(), p)}")
                elif user_choice == 10:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def Numpy_Analysis(self):
        """Perform Numpy analysis on the dataset."""
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        while True:
            print("\n--- Numpy Analysis Menu ---")
            print("""
            1. Convert DataFrame to Numpy Array
            2. Calculate Mean of Numpy Array
            3. Calculate Median of Numpy Array
            4. Calculate Standard Deviation of Numpy Array
            5. Indexing and Slicing of Numpy Array
            6. Splitting Array
            7. Return to main menu
            """)

            try:
                user_choice = int(input("Enter your choice (1-7): "))

                if user_choice == 1:
                    numpy_array = self.data.to_numpy()
                    print("DataFrame converted to Numpy Array:")
                    print(numpy_array)

                elif user_choice == 2:
                    numeric_data = self.data.select_dtypes(include=[np.number]).to_numpy()
                    print(f"Mean of Numpy Array: {np.mean(numeric_data)}")

                elif user_choice == 3:
                    numeric_data = self.data.select_dtypes(include=[np.number]).to_numpy()
                    print(f"Median of Numpy Array: {np.median(numeric_data)}")

                elif user_choice == 4:
                    numeric_data = self.data.select_dtypes(include=[np.number]).to_numpy()
                    print(f"Standard Deviation of Numpy Array: {np.std(numeric_data)}")

                elif user_choice == 5:
                    numpy_array = self.data.to_numpy()
                    print("Original Array Shape:", numpy_array.shape)
                    row_index = int(input("Enter row index: "))
                    col_index = int(input("Enter column index: "))
                    print(f"Sliced Value at ({row_index}, {col_index}): {numpy_array[row_index, col_index]}")

                elif user_choice == 6:
                    numpy_array = self.data.to_numpy()
                    print("Original Array Shape:", numpy_array.shape)
                    num_splits = int(input("Enter number of splits: "))
                    split_arrays = np.array_split(numpy_array, num_splits)
                    for i, arr in enumerate(split_arrays):
                        print(f"Split {i+1}:")
                        print(arr)

                elif user_choice == 7:
                    print("Returning to main menu...")
                    break

                else:
                    print("Invalid choice. Please try again.")

            except Exception as e:
                print(f"Error: {e}")

    def split_data(self, column_name, delimiter, new_names_str):
        """Split a column in the dataset based on a delimiter."""
        print("DataFrame Columns Names: ", list(self.data.columns))
        print("\n--- Split Column Data ---")
        column_name = input("Enter column name to split: ")
        delimiter = input("Enter delimiter: ")
        new_names_str = input("Enter new column names (separated by commas): ")
        if column_name in self.data.columns:
            split_df = self.data[column_name].astype(str).str.split(delimiter, expand=True)
            new_cols = [n.strip() for n in new_names_str.split(',')]
            
            if len(new_cols) == split_df.shape[1]:
                split_df.columns = new_cols
                self.data = self.data.join(split_df)
                print(f"Column '{column_name}' split successfully into {new_cols}.")
            else:
                print(f"Error: Expected {split_df.shape[1]} column names, but got {len(new_cols)}.")
        else:
            print(f"Column '{column_name}' does not exist in the dataset.")

    def search_sort_filter(self):
        """Search, sort, and filter the dataset."""
        while True:
            print("\n--- Search, Sort, and Filter Menu ---")
            print("DataFrame Columns Names: ", list(self.data.columns))
            print("""
            1. Search for a value in a column
            2. Sort the dataset by a column
            3. Filter the dataset based on a condition
            4. Return to main menu
            """)

            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if user_choice == 1:
                    column_name = input("Enter the column name to search in: ")
                    search_value = input("Enter the value to search for: ")
                    if column_name in self.data.columns:
                        result = self.data[self.data[column_name].astype(str) == search_value]
                        if not result.empty:
                            print(f"Search results for '{search_value}' in column '{column_name}':")
                            print(result)
                        else:
                            print(f"No matching rows found for '{search_value}' in column '{column_name}'.")
                    else:
                        print(f"Column '{column_name}' does not exist in the dataset.")
                elif user_choice == 2:
                    column_name = input("Enter the column name to sort by: ")
                    ascending_order = input("Sort in ascending order? (yes/no): ").strip().lower() == 'yes'
                    if column_name in self.data.columns:
                        sorted_data = self.data.sort_values(by=column_name, ascending=ascending_order)
                        print(f"Data sorted by '{column_name}' ({'ascending' if ascending_order else 'descending'}):")
                        print(sorted_data)
                    else:
                        print(f"Column '{column_name}' does not exist in the dataset.")
                elif user_choice == 3:
                    condition = input("Enter the filter condition (e.g., 'column_name > value'): ")
                    try:
                        filtered_data = self.data.query(condition)
                        print(f"Filtered data based on condition '{condition}':")
                        print(filtered_data)
                    except Exception as e:
                        print(f"Error applying filter condition: {e}")
                elif user_choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def _prompt_save_plot(self):
        """Helper method to prompt for saving before plt.show()."""
        save_choice = input("Do you want to save this plot? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            chart_name = input("Enter file name (e.g., 'chart.png', 'chart.pdf'): ").strip()
            try:
                plt.savefig(chart_name, dpi=300, bbox_inches='tight')
                print(f"Plot saved successfully as {chart_name}")
            except Exception as e:
                print(f"Error saving plot: {e}")

    def save_visualization(self):
        """Standalone prompt to save active plot figure."""
        self._prompt_save_plot()

    def visualize_matplotlib(self):
        """Visualize the dataset using Matplotlib."""
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        while True:
            print("DataFrame Columns Names: ", ", ".join(self.data.columns))
            print("-----------------------------------------------------------")
            print("\n--- Matplotlib Visualization Menu ---")
            print("""
            1. Line Plot
            2. Bar Plot
            3. Histogram
            4. Scatter Plot
            5. Pie Chart
            6. Stack Plot
            7. Return to main menu
            """)

            try:
                user_choice = int(input("Enter your choice (1-7): "))
                if user_choice == 1:
                    x_col = input("Enter the column name for x-axis: ")
                    y_col = input("Enter the column name for y-axis: ")
                    if x_col in self.data.columns and y_col in self.data.columns:
                        plt.figure(figsize=(10, 6))
                        sample_data = self.data.head(20)
                        plt.plot(sample_data[x_col], sample_data[y_col], marker='o')
                        plt.title(f'Line Plot of {y_col} vs {x_col}')
                        plt.xlabel(x_col)
                        plt.ylabel(y_col)
                        plt.grid(True)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("One or both column names do not exist in the dataset.")
                        
                elif user_choice == 2:
                    x_col = input("Enter the column name for x-axis: ")
                    y_col = input("Enter the column name for y-axis: ")
                    if x_col in self.data.columns and y_col in self.data.columns:
                        plt.figure(figsize=(10, 6))
                        sample_data = self.data.head(20)
                        plt.bar(sample_data[x_col].astype(str), sample_data[y_col])
                        plt.title(f'Bar Plot of {y_col} vs {x_col}')
                        plt.xlabel(x_col)
                        plt.ylabel(y_col)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("One or both column names do not exist in the dataset.")
                        
                elif user_choice == 3:
                    y_col = input("Enter the column name for histogram: ")
                    if y_col in self.data.columns:
                        plt.figure(figsize=(10, 6))
                        plt.hist(self.data[y_col].dropna(), bins=20, edgecolor='black')
                        plt.title(f'Histogram of {y_col}')
                        plt.xlabel(y_col)
                        plt.ylabel('Frequency')
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("Column name does not exist in the dataset.")
                        
                elif user_choice == 4:
                    x_col = input("Enter the column name for x-axis: ")
                    y_col = input("Enter the column name for y-axis: ")
                    if x_col in self.data.columns and y_col in self.data.columns:
                        plt.figure(figsize=(10, 6))
                        plt.scatter(self.data[x_col], self.data[y_col], alpha=0.7)
                        plt.title(f'Scatter Plot of {y_col} vs {x_col}')
                        plt.xlabel(x_col)
                        plt.ylabel(y_col)
                        plt.grid(True)
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("One or both column names do not exist in the dataset.")
                        
                elif user_choice == 5:
                    col = input("Enter the column name for the pie chart: ")
                    if col in self.data.columns:
                        plt.figure(figsize=(8, 8))
                        value_counts = self.data[col].value_counts().head(10)
                        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
                        plt.title(f'Pie Chart of {col}')
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("Column name does not exist in the dataset.")
                        
                elif user_choice == 6:
                    x_col = input("Enter the column name for x-axis: ")
                    y_cols = input("Enter the column names for y-axis (comma-separated): ").split(',')
                    y_cols = [col.strip() for col in y_cols]
                    if x_col in self.data.columns and all(col in self.data.columns for col in y_cols):
                        plt.figure(figsize=(10, 6))
                        sample_data = self.data.head(10)
                        plt.stackplot(sample_data[x_col].astype(str), [sample_data[col] for col in y_cols], labels=y_cols)
                        plt.title(f'Stack Plot of {y_cols} vs {x_col}')
                        plt.xlabel(x_col)
                        plt.ylabel('Values')
                        plt.legend(loc='upper left')
                        plt.grid(True)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("One or more column names do not exist in the dataset.")
                        
                elif user_choice == 7:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def visualize_seaborn(self):
        """Visualize the dataset using Seaborn."""
        if self.data.empty:
            print("Dataset is empty. Please load data first.")
            return

        print("DataFrame Columns Names: ", ", ".join(self.data.columns))
        print("-----------------------------------------------------------")
        while True:
            print("\n--- Seaborn Visualization Menu ---")
            print("""
            1. Pair Plot
            2. Heatmap
            3. Box Plot
            4. Violin Plot
            5. Count Plot
            6. Return to main menu
            """)

            try:
                user_choice = int(input("Enter your choice (1-6): "))
                if user_choice == 1:
                    sns.pairplot(self.data)
                    self._prompt_save_plot()
                    plt.show()
                elif user_choice == 2:
                    plt.figure(figsize=(10, 8))
                    sns.heatmap(self.data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
                    plt.title('Heatmap of Correlation Matrix')
                    plt.tight_layout()
                    self._prompt_save_plot()
                    plt.show()
                elif user_choice == 3:
                    col = input("Enter the column name for the box plot: ")
                    if col in self.data.columns:
                        plt.figure(figsize=(8, 6))
                        sns.boxplot(x=self.data[col])
                        plt.title(f'Box Plot of {col}')
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("Column name does not exist in the dataset.")
                elif user_choice == 4:
                    col = input("Enter the column name for the violin plot: ")
                    if col in self.data.columns:
                        plt.figure(figsize=(8, 6))
                        sns.violinplot(x=self.data[col])
                        plt.title(f'Violin Plot of {col}')
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("Column name does not exist in the dataset.")
                elif user_choice == 5:
                    col = input("Enter the column name for the count plot: ")
                    if col in self.data.columns:
                        plt.figure(figsize=(8, 6))
                        sns.countplot(x=self.data[col])
                        plt.title(f'Count Plot of {col}')
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        self._prompt_save_plot()
                        plt.show()
                    else:
                        print("Column name does not exist in the dataset.")
                elif user_choice == 6:
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")

    def pivot_table(self):
            """Create a pivot table from the dataset."""
            if self.data.empty:
                print("Dataset is empty. Please load data first.")
                return

            print("DataFrame Columns Names: ", ", ".join(self.data.columns))
            try:
                    index_col = input("Enter column name for index: ").strip()
                    values_col = input("Enter column name for values: ").strip()
                    agg_func = input("Enter aggregation function (mean, sum, count, max, min): ").strip().lower()

                    if index_col not in self.data.columns or values_col not in self.data.columns:
                        print("One or both column names do not exist in the dataset.")
                        return

                    if agg_func not in ["mean", "sum", "count", "max", "min"]:
                        print("Invalid aggregation function.")
                        return

                    pivot = pd.pivot_table(self.data, index=index_col, values=values_col, aggfunc=agg_func)
                    print("\n--- Pivot Table Result ---")
                    print(pivot)

            except Exception as e:
                    print(f"Error creating pivot table: {e}")



class AdvancedSalesAnalyzer(SalesDataAnalyzer):
    def __init__(self, data=None):
        super().__init__(data)
        print("AdvancedSalesAnalyzer initialized.")

    def explore_data(self):
        if self.data.empty or self.data.shape[1] == 0:
            print("Dataset is empty or has no columns. Please load data first.")
            return
        print("\n--- Advanced Data Exploration ---")
        print("Displaying additional insights:")
        print(self.data.describe(include='all').T)

        choice = input("\nDo you also want to open the standard Data Exploration Menu? (yes/no): ").strip().lower()
        if choice == "yes":
            super().explore_data()

    def __add__(self, other):
        """Combine two analyzers using '+' operator."""
        if other.data.empty:
            print("Other dataset is empty. Cannot combine.")
            return self
        combined_data = pd.concat([self.data, other.data], ignore_index=True)
        return AdvancedSalesAnalyzer(combined_data)


def menu():
    analyzer = SalesDataAnalyzer()
    ad_analyzer = AdvancedSalesAnalyzer()

    while True:
        print("\n==========================================================")
        print("Welcome to the Sales Data Analyzer & Visualization Tool")
        print("==========================================================")
        print("""
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
        """)

        try:
            choice = int(input("Enter your choice (1-12): "))

            if choice == 1:
                file_path = input("Enter the path to the CSV file: ")
                analyzer.load_data(file_path)
                ad_analyzer = AdvancedSalesAnalyzer(analyzer.data)

            elif choice == 2:
                analyzer.explore_data()
            elif choice == 3:
                analyzer.Statistical_Maths_Analysis()
            elif choice == 4:
                analyzer.clean_data()
            elif choice == 5:
                ad_analyzer.explore_data()
            elif choice == 6:
                analyzer.Numpy_Analysis()
            elif choice == 7:
                analyzer.split_data()
            elif choice == 8:
                analyzer.search_sort_filter()
            elif choice == 9:
                analyzer.visualize_matplotlib()
            elif choice == 10:
                analyzer.visualize_seaborn()
            elif choice == 11:
                analyzer.pivot_table()
            elif choice == 12:
                print("Exiting application...")
                break
            else:
                print("Please enter a valid choice (1-12).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    menu()