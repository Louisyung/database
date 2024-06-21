import mariadb
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Database connection settings
user_setting = {
    "user": "411177009",
    "password": "411177009",
    "host": "0.tcp.jp.ngrok.io",
    "port": 11051,
    "database": "411177009"
}

# Function to execute a query and display results
def execute_query():
    try:
        query = query_entry.get()
        if not query.lower().startswith("select"):
            messagebox.showerror("Error", "Only SELECT queries are allowed.")
            return
        
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Clear previous treeview data
        for item in tree.get_children():
            tree.delete(item)
        
        # Display column headers
        columns = [desc[0] for desc in cursor.description]
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        # Display query results
        for row in rows:
            tree.insert("", "end", values=row)
    
    except mariadb.Error as e:
        messagebox.showerror("Error", f"Error executing query: {e}")

# Function to initialize the database and insert data
def initialize_database():
    try:
        # Create and initialize database tables
        connection = mariadb.connect(**user_setting)
        global cursor
        cursor = connection.cursor()

        tables = ['Purchase', 'Customer', 'Vehicle', 'Option', 'Dealer', 'Supplier', 'Model', 'Brand', 'Plant']
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Plant (
            Plant_ID INT AUTO_INCREMENT PRIMARY KEY,
            Plant_Name VARCHAR(255) NOT NULL,
            Location VARCHAR(255)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Brand (
            Brand_ID INT AUTO_INCREMENT PRIMARY KEY,
            Brand_Name VARCHAR(255) NOT NULL,
            Plant_ID INT,
            FOREIGN KEY (Plant_ID) REFERENCES Plant(Plant_ID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Model (
            Model_ID INT AUTO_INCREMENT PRIMARY KEY,
            Model_Name VARCHAR(255) NOT NULL,
            Brand_ID INT,
            FOREIGN KEY (Brand_ID) REFERENCES Brand(Brand_ID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Supplier (
            Supplier_ID INT AUTO_INCREMENT PRIMARY KEY,
            Supplier_Name VARCHAR(255) NOT NULL,
            Phone VARCHAR(255),
            Address VARCHAR(255)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Dealer (
            Dealer_ID INT AUTO_INCREMENT PRIMARY KEY,
            Dealer_Name VARCHAR(255) NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Option (
            Option_ID INT AUTO_INCREMENT PRIMARY KEY,
            Option_Type VARCHAR(255) NOT NULL,
            Option_Value VARCHAR(255)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vehicle (
            VIN VARCHAR(255) PRIMARY KEY,
            Color VARCHAR(255),
            Brand_ID INT,
            Model_ID INT,
            Dealer_ID INT,
            Option_ID INT,
            FOREIGN KEY (Brand_ID) REFERENCES Brand(Brand_ID),
            FOREIGN KEY (Model_ID) REFERENCES Model(Model_ID),
            FOREIGN KEY (Dealer_ID) REFERENCES Dealer(Dealer_ID),
            FOREIGN KEY (Option_ID) REFERENCES Option(Option_ID)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Address VARCHAR(255),
            Phone VARCHAR(255),
            Gender VARCHAR(255)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Purchase (
            Customer_ID INT,
            VIN VARCHAR(255),
            Purchase_Date DATE,
            FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
            FOREIGN KEY (VIN) REFERENCES Vehicle(VIN),
            PRIMARY KEY (Customer_ID, VIN)
        )
        """)

        # Insert sample data
        plants = [('Plant A', 'Location A'), ('Plant B', 'Location B')]
        for plant in plants:
            cursor.execute("INSERT IGNORE INTO Plant (Plant_Name, Location) VALUES (%s, %s)", plant)
        connection.commit()

        brands = [('Louis', 1), ('Andy', 2)]
        for brand in brands:
            cursor.execute("INSERT IGNORE INTO Brand (Brand_Name, Plant_ID) VALUES (%s, %s)", brand)
        connection.commit()

        models = [('Polor', 1), ('Tiga', 2)]
        for model in models:
            cursor.execute("INSERT IGNORE INTO Model (Model_Name, Brand_ID) VALUES (%s, %s)", model)
        connection.commit()

        suppliers = [
            ('Tank', '123-456-7890', 'Tainan'),
            ('Clock', '098-765-4321', 'Chiayi')
        ]
        for supplier in suppliers:
            cursor.execute("INSERT IGNORE INTO Supplier (Supplier_Name, Phone, Address) VALUES (%s, %s, %s)", supplier)
        connection.commit()

        dealers = ['Dealer One', 'Dealer Two', 'Dealer Three', 'Dealer Four', 'Dealer Five']
        for dealer in dealers:
            cursor.execute("INSERT IGNORE INTO Dealer (Dealer_Name) VALUES (%s)", (dealer,))
        connection.commit()

        options = [('Red', '12 Cylinder'), ('Blue', '8 Cylinder'), ('White', '6 Cylinder'), ('Gray', '3 Cylinder')]
        for option in options:
            cursor.execute("INSERT IGNORE INTO Option (Option_Type, Option_Value) VALUES (%s, %s)", option)
        connection.commit()

        vehicles = [
            ('1HGCM82633A123456', 'Red', 1, 1, 1, 1),
            ('1HGCM82633A123457', 'Blue', 2, 2, 2, 2),
            ('1HGCM82633A123458', 'White', 1, 1, 3, 3),
            ('1HGCM82633A123459', 'Red', 2, 2, 4, 1),
            ('1HGCM82633A123460', 'Gray', 1, 1, 5, 2)
        ]
        for vehicle in vehicles:
            cursor.execute("INSERT IGNORE INTO Vehicle (VIN, Color, Brand_ID, Model_ID, Dealer_ID, Option_ID) VALUES (%s, %s, %s, %s, %s, %s)", vehicle)
        connection.commit()

        customers = [
            ('John Smith', '123 Main St', '555-1234', 'Male'),
            ('Jane Doe', '456 Elm St', '555-5678', 'Female'),
            ('Michael Johnson', '789 Oak St', '555-8765', 'Male'),
            ('Emily Davis', '321 Pine St', '555-4321', 'Female'),
            ('William Brown', '654 Maple St', '555-9876', 'Male')
        ]
        for customer in customers:
            cursor.execute("INSERT IGNORE INTO Customer (Name, Address, Phone, Gender) VALUES (%s, %s, %s, %s)", customer)
        connection.commit()

        purchases = [
            (1, '1HGCM82633A123456', datetime.strptime('2024-06-01', '%Y-%m-%d')),
            (2, '1HGCM82633A123457', datetime.strptime('2024-06-02', '%Y-%m-%d')),
            (3, '1HGCM82633A123458', datetime.strptime('2024-06-03', '%Y-%m-%d')),
            (4, '1HGCM82633A123459', datetime.strptime('2024-06-04', '%Y-%m-%d')),
            (5, '1HGCM82633A123460', datetime.strptime('2024-06-05', '%Y-%m-%d'))
        ]
        for purchase in purchases:
            cursor.execute("INSERT IGNORE INTO Purchase (Customer_ID, VIN, Purchase_Date) VALUES (%s, %s, %s)", purchase)
        connection.commit()

    except mariadb.Error as e:
        messagebox.showerror("Error", f"Error connecting to the database: {e}")

# Create main application window
root = tk.Tk()
root.title("Database Query Interface")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=20)

query_label = tk.Label(frame, text="Enter SELECT query:")
query_label.pack(side=tk.LEFT, padx=5)

query_entry = tk.Entry(frame, width=50)
query_entry.pack(side=tk.LEFT, padx=5)

query_button = tk.Button(frame, text="Execute", command=execute_query)
query_button.pack(side=tk.LEFT, padx=5)

tree = ttk.Treeview(root)
tree.pack(pady=20)

# Initialize database
initialize_database()

# Run the application
root.mainloop()

