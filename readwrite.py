import csv
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

def get_input():
    root = tk.Tk()
    root.withdraw()

    num_columns = simpledialog.askinteger("Input", "Enter the number of columns:")
    num_rows = simpledialog.askinteger("Input", "Enter the number of rows:")

    data = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    return data

def write_to_csv(data):
    def save_data():
        filename = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filename:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([[cell.get() for cell in row] for row in data])
            messagebox.showinfo("Success", f"Data has been written to {filename}")
            save_window.destroy()

    save_window = tk.Tk()
    save_window.title("Enter Data")

    for i, row in enumerate(data):
        for j, value in enumerate(row):
            entry = tk.Entry(save_window, width=15)
            entry.grid(row=i, column=j)
            data[i][j] = entry

    save_button = tk.Button(save_window, text="Save", command=save_data)
    save_button.grid(row=len(data), column=0, columnspan=len(data[0]))

    save_window.mainloop()

def read_csv():
    def open_file():
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filename:
            with open(filename, newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
                display_data(data)
            open_window.destroy()

    def display_data(data):
        read_window = tk.Tk()
        read_window.title("CSV Data")

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                entry = tk.Entry(read_window, width=15)
                entry.grid(row=i, column=j)
                entry.insert(0, value)

        read_window.mainloop()

    open_window = tk.Tk()
    open_button = tk.Button(open_window, text="Open CSV File", command=open_file)
    open_button.pack(pady=20)

    open_window.mainloop()

def main():
    root = tk.Tk()
    root.withdraw()

    action = simpledialog.askstring("Action", "Do you want to read or write CSV data? (read/write):")

    if action == "write":
        data = get_input()
        write_to_csv(data)
    elif action == "read":
        read_csv()
    else:
        messagebox.showerror("Error", "Invalid action. Please choose 'read' or 'write'.")

if __name__ == "__main__":
    main()
