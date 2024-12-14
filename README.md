Football Player Data Cleaning Project
Project Overview
This project involves cleaning a football player dataset to prepare it for detailed analysis. The dataset contains information about players, including their personal details, club affiliations, contract information, physical attributes, and performance statistics. The cleaning process ensures the dataset is accurate, consistent, and ready for further analysis using SQL or visualization tools.

Dataset Description
The dataset contains the following key information:

Player Details: Name, nationality, age, and player URLs.
Club Information: Club name, contract details, and player positions.
Attributes: Height, weight, preferred foot, and various performance statistics.
Financials: Market value, wage, and release clause information.
Data Cleaning Process
The data cleaning process was performed using Pandas in Python. Below are the key steps undertaken to clean the dataset:

Handling Missing Values

Identified columns with missing values, such as contract details, height, and market value.
Filled missing numerical values with appropriate statistics (e.g., mean or median) or domain-specific defaults.
For categorical columns, filled missing values with "Unknown" or the most frequent category.
Standardizing Columns

Converted height from different units to a standardized metric (centimeters).
Formatting the Dataset

Renamed columns to have clear and consistent naming conventions (e.g., "Player Name" instead of "Name").
Sorted the dataset by player ratings and club affiliations for easier querying.
Added Columns

Added a few columns from the existing dataset (i.e., Contract Start Year, Contract End Year, etc.).
Tools Used
Pandas: For handling missing values, removing duplicates, and standardizing the data.
Jupyter Notebook: For executing Python scripts and documenting the cleaning process.
Outcome
The cleaned dataset is now ready for exploratory data analysis (EDA), SQL-based querying, and visualization. This process ensures that all inconsistencies, missing values, and added features have been addressed, providing a high-quality dataset for deriving meaningful insights.
