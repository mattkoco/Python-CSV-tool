import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_input():
    root = tk.Tk()
    root.withdraw()

    num_columns = simpledialog.askinteger("Input", "Enter the number of columns:")

    column_headers = []
    for i in range(num_columns):
        header = simpledialog.askstring("Input", f"Enter the header for column {i+1}:")
        column_headers.append(header)

    data = [column_headers]

    num_rows = simpledialog.askinteger("Input", "Enter the number of rows:")

    for i in range(num_rows):
        row = []
        for col in column_headers:
            value = simpledialog.askstring("Input", f"Enter value for {col} in row {i+1}:")
            row.append(value)
        data.append(row)

    return data

def write_to_csv(data):
    filename = simpledialog.askstring("Input", "Enter the filename to save as (e.g., data.csv):")
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    messagebox.showinfo("Success", f"Data has been written to {filename}")

def main():
    data = get_input()
    write_to_csv(data)

if __name__ == "__main__":
    main()
