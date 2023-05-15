# Piup
import tkinter as tk
from tkinter import messagebox
import serial

def measure_pressure():
    try:
        # Connect to the serial port
        ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the appropriate port and baud rate

        # Send command to measure pressure
        ser.write(b'MEASURE\r\n')

        # Read response
        response = ser.readline().decode().strip()

        # Close the serial port
        ser.close()

        # Display the measured pressure
        messagebox.showinfo("Pressure Measurement", f"Pressure: {response} psi")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
window = tk.Tk()
window.title("Pressure Measurement")
window.geometry("200x100")

# Create the measure button
measure_button = tk.Button(window, text="Measure Pressure", command=measure_pressure)
measure_button.pack(pady=20)

# Start the application
window.mainloop()
