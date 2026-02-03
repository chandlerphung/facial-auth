import tkinter as tk

def create_gui():
    """
    Create a simple GUI to select an account.

    Returns:
        str: Name of the selected account
    """
    selected_name = None
    root = tk.Tk()

    def close_window(name):
        nonlocal selected_name
        selected_name = name
        root.destroy()

    root.title("Facial Authentication")
    root.geometry("350x200")

    tk.Label(root, text="Choose Account", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Chandler", width=20, command=lambda: close_window("Chandler")).pack(pady=5)
    tk.Button(root, text="Andy", width=20, command=lambda: close_window("Andy")).pack(pady=5)
    tk.Button(root, text="Jason", width=20, command=lambda: close_window("Jason")).pack(pady=5)

    root.mainloop()
    return selected_name
