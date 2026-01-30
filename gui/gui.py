import tkinter as tk

def create_gui():
    selected_name = None
    root = tk.Tk()

    def close_window(name):
        nonlocal selected_name  # <- This is key
        selected_name = name    # Now updates outer variable
        root.destroy()  

    root.title("My First Tkinter App")
    root.geometry("350x200")

    tk.Label(root, text="Choose Account").pack(pady=20)
    tk.Button(root, text="Chandler", command=lambda: close_window("Chandler")).pack(pady=5)
    tk.Button(root, text="Andy", command=lambda: close_window("Andy")).pack(pady=5)
    tk.Button(root, text="Jason", command=lambda: close_window("Jason")).pack(pady=5)

    root.mainloop()
    return selected_name
