# Member
軟體二 411177033 洪唯仁
軟體二 411177009 楊育丞
# Database Query Interface

This project is a GUI-based application for querying a database. It uses MariaDB for the database and Tkinter for the graphical user interface. The application allows users to execute SELECT queries and view the results in a table format.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Sample Data](#sample-data)
- [Acknowledgements](#acknowledgements)

## Features
- Connect to a MariaDB database
- Execute SELECT queries
- Display query results in a table format
- Initialize the database with sample data

## Installation
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
2. **Install required Python packages**:
    ```sh
    pip install mariadb tkinter
    ```
3. **Configure database connection settings**:
    - Edit the `user_setting` dictionary in the `main.py` file to match your MariaDB credentials.

## Usage
1. **Run the application**:
    ```sh
    python main.py
    ```
2. **Initialize the database**:
    - When the application starts, the `initialize_database()` function will create and populate the database tables with sample data.
3. **Execute a SELECT query**:
    - Enter a SELECT query in the input field and click the "Execute" button.
    - The results will be displayed in the table below.

## Database Schema
The database consists of the following tables:
- **Plant**: Information about manufacturing plants.
- **Brand**: Information about vehicle brands.
- **Model**: Information about vehicle models.
- **Supplier**: Information about suppliers.
- **Dealer**: Information about dealers.
- **Option**: Information about vehicle options.
- **Vehicle**: Information about vehicles.
- **Customer**: Information about customers.
- **Purchase**: Information about vehicle purchases.

### Table Definitions
- **Plant**:
    - `Plant_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Plant_Name` VARCHAR(255) NOT NULL
    - `Location` VARCHAR(255)
- **Brand**:
    - `Brand_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Brand_Name` VARCHAR(255) NOT NULL
    - `Plant_ID` INT, FOREIGN KEY REFERENCES Plant(Plant_ID)
- **Model**:
    - `Model_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Model_Name` VARCHAR(255) NOT NULL
    - `Brand_ID` INT, FOREIGN KEY REFERENCES Brand(Brand_ID)
- **Supplier**:
    - `Supplier_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Supplier_Name` VARCHAR(255) NOT NULL
    - `Phone` VARCHAR(255)
    - `Address` VARCHAR(255)
- **Dealer**:
    - `Dealer_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Dealer_Name` VARCHAR(255) NOT NULL
- **Option**:
    - `Option_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Option_Type` VARCHAR(255) NOT NULL
    - `Option_Value` VARCHAR(255)
- **Vehicle**:
    - `VIN` VARCHAR(255) PRIMARY KEY
    - `Color` VARCHAR(255)
    - `Brand_ID` INT, FOREIGN KEY REFERENCES Brand(Brand_ID)
    - `Model_ID` INT, FOREIGN KEY REFERENCES Model(Model_ID)
    - `Dealer_ID` INT, FOREIGN KEY REFERENCES Dealer(Dealer_ID)
    - `Option_ID` INT, FOREIGN KEY REFERENCES Option(Option_ID)
- **Customer**:
    - `Customer_ID` INT AUTO_INCREMENT PRIMARY KEY
    - `Name` VARCHAR(255) NOT NULL
    - `Address` VARCHAR(255)
    - `Phone` VARCHAR(255)
    - `Gender` VARCHAR(255)
- **Purchase**:
    - `Customer_ID` INT, FOREIGN KEY REFERENCES Customer(Customer_ID)
    - `VIN` VARCHAR(255), FOREIGN KEY REFERENCES Vehicle(VIN)
    - `Purchase_Date` DATE
    - PRIMARY KEY (Customer_ID, VIN)

## Sample Data
The database is populated with the following sample data:

### Plants
- Plant A, Location A
- Plant B, Location B

### Brands
- Louis (Plant A)
- Andy (Plant B)

### Models
- Polor (Louis)
- Tiga (Andy)

### Suppliers
- Tank (Phone: 123-456-7890, Address: Tainan)
- Clock (Phone: 098-765-4321, Address: Chiayi)

### Dealers
- Dealer One
- Dealer Two
- Dealer Three
- Dealer Four
- Dealer Five

### Options
- Red, 12 Cylinder
- Blue, 8 Cylinder
- White, 6 Cylinder
- Gray, 3 Cylinder

### Vehicles
- VIN: 1HGCM82633A123456, Color: Red, Brand: Louis, Model: Polor, Dealer: Dealer One, Option: Red, 12 Cylinder
- VIN: 1HGCM82633A123457, Color: Blue, Brand: Andy, Model: Tiga, Dealer: Dealer Two, Option: Blue, 8 Cylinder
- VIN: 1HGCM82633A123458, Color: White, Brand: Louis, Model: Polor, Dealer: Dealer Three, Option: White, 6 Cylinder
- VIN: 1HGCM82633A123459, Color: Red, Brand: Andy, Model: Tiga, Dealer: Dealer Four, Option: Red, 12 Cylinder
- VIN: 1HGCM82633A123460, Color: Gray, Brand: Louis, Model: Polor, Dealer: Dealer Five, Option: Gray, 3 Cylinder

### Customers
- John Smith (Address: 123 Main St, Phone: 555-1234, Gender: Male)
- Jane Doe (Address: 456 Elm St, Phone: 555-5678, Gender: Female)
- Michael Johnson (Address: 789 Oak St, Phone: 555-8765, Gender: Male)
- Emily Davis (Address: 321 Pine St, Phone: 555-4321, Gender: Female)
- William Brown (Address: 654 Maple St, Phone: 555-9876, Gender: Male)

### Purchases
- John Smith purchased VIN: 1HGCM82633A123456 on 2024-06-01
- Jane Doe purchased VIN: 1HGCM82633A123457 on 2024-06-02
- Michael Johnson purchased VIN: 1HGCM82633A123458 on 2024-06-03
- Emily Davis purchased VIN: 1HGCM82633A123459 on 2024-06-04
- William Brown purchased VIN: 1HGCM82633A123460 on 2024-06-05

## Acknowledgements
- [MariaDB](https://mariadb.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python](https://www.python.org/)

This project was created as a part of a database management course assignment. It demonstrates basic CRUD operations, database initialization, and GUI development using Python.

For any issues or contributions, please refer to the [repository](<repository-url>).
