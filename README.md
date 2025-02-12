# Dynamic MySQL Table Creation with Python

This repository demonstrates Python script for dynamically creating MySQL tables based on year and month.  Uses object-oriented programming for maintainability and includes robust connection management and error handling.

## Program Description

* **Functionality:** Easily create monthly MySQL tables with this Python tool. Python script for dynamically creating MySQL tables based on year and month.
* **Programmer:** Suman Gangopadhyay
* **Email ID:** linuxgurusuman@gmail.com
* **Date:** 12-Feb-2025
* **Version:** 1.0
* **Prerequisites:** Python, Selenium, ChromeDriver
* **Caveats:** None
  
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Database Configuration](#database-configuration)
- [Error Handling](#error-handling)
- [Extending the Code](#extending-the-code)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project addresses the need for creating time-based tables in a MySQL database.  Instead of manually creating tables for each month, this Python script automates the process.  It uses the `pymysql` library for database interaction and the `calendar` module for date calculations. The code is structured using object-oriented principles, making it modular, reusable, and easy to maintain.

## Features

- **Dynamic Table Naming:** Tables are named dynamically based on the year and month (e.g., `table_2025_01`).
- **Date-Based Columns:** Columns are created for each day of the specified month, using the date as the column name.
- **Object-Oriented Design:** The code is organized into classes (`DatabaseManager` and `TableManager`) for better structure and maintainability.
- **Connection Management:** Database connections are handled efficiently, ensuring they are opened only when needed and closed promptly.
- **Error Handling:** The code includes error handling to catch potential MySQL exceptions and prevent application crashes.
- **Clear Separation of Concerns:** The `DatabaseManager` handles database interactions, while the `TableManager` handles table-specific logic.
- **Rollback on Error:** Transactions are rolled back if an error occurs during table creation, ensuring data consistency.
- **Clear Example Usage:** The provided example demonstrates how to use the classes to create tables.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```

2.  **Install required Python packages:**

    ```bash
    pip install pymysql
    ```

3.  **Install MySQL Server:** If you don't have MySQL Server installed, download and install it from the official MySQL website.

## Usage

1.  **Configure Database Connection:** Open the Python script and modify the database connection parameters (host, user, password, database) in the example usage section.

2.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

3.  **Check the Database:** Verify that the table has been created successfully in your MySQL database.

## Code Structure

-   `DatabaseManager`: This class handles database connections (opening, closing) and basic database operations.
-   `TableManager`: This class contains the logic for creating tables, utilizing the `DatabaseManager` for database interaction.
-   `your_script_name.py`: The main script that demonstrates how to use the `DatabaseManager` and `TableManager` classes.

## Database Configuration

The database connection parameters are configured within the main script.  Make sure to replace the placeholder values with your actual database credentials.

```python
db_manager = DatabaseManager(host="localhost", user="root", password="suman", database="office")

## License

This project is licensed under the MIT License.
