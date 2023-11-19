import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class BMICalculator:
    def __init__(self,master):
        self.master = master
        self.master.title("BMI Calculator")

        self.label_weight = tk.Label(master,text="Enter Weight (Kg):")
        self.label_height = tk.Label(master,text="Enter height (m):")

        self.entry_weight = tk.Entry(master)
        self.entry_height = tk.Entry(master)

        self. button_calculate = tk.Button(master,text="Calculate BMI",command=self.calculate_bmi )
        self. button_plot = tk.Button(master,text="Plot BMI History",command=self.plot_bmi_history )

        self.label_result= tk.Label(master, text ="")

        self.label_weight.grid(row=0, column=0, padx=10, pady=10)
        self.label_height.grid(row=1, column=0, padx=10, pady=10)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)
        self.button_calculate.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_plot.grid(row=3, column=0, columnspan=2, pady=10)
        self.label_result.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Invalid input. Please enter positive values for weight and height.")
                return

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            result_text = f"Your BMI is: {bmi:.2f}\nCategory: {category}"
            self.label_result.config(text=result_text)

            # Save BMI data to a file (for basic historical tracking)
            with open("bmi_history.txt", "a") as file:
                file.write(f"{bmi:.2f}\n")

            
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values for weight and height.")

    @staticmethod
    def classify_bmi(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal Weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def plot_bmi_history(self):
        try:
            with open("bmi_history.txt", "r") as file:
                bmi_data = [float(line.strip()) for line in file]

            if not bmi_data:
                messagebox.showinfo("Info", "No BMI data available for plotting.")
                return

            plt.plot(bmi_data,marker='0')
            plt.title("BMI History")
            plt.xlabel("Measurement")
            plt.ylabel("BMI")
            plt.show()

        except FileNotFoundError:
            messagebox.showinfo("Info","No BMI data available for plotting.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop() 