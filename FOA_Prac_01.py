import random as r
import tkinter as tk

def is_fibonacci(n):
    """ Check if a number is a Fibonacci number """
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

List_of_Random_No = [r.randint(1,100) for i in range(1,100)]
List_of_Fibonacci = list(filter(is_fibonacci,List_of_Random_No))
List_of_Fibonacci.sort()

def traverse_forward():
    global current_index
    if current_index < len(List_of_Fibonacci) - 1:
        current_index += 1
        display_fibonacci()

def traverse_backward():
    global current_index
    if current_index > 0:
        current_index -= 1
        display_fibonacci()

def display_fibonacci():
    fibonacci_label.config(text=f"Fibonacci Number: {List_of_Fibonacci[current_index]}")

current_index = 0

# GUI setup
root = tk.Tk()
root.title("Fibonacci Number Traversal")

fibonacci_label = tk.Label(root, text=f"Fibonacci Number: {List_of_Fibonacci[current_index]}")
fibonacci_label.pack(pady=10)

forward_button = tk.Button(root, text="Next", command=traverse_forward)
forward_button.pack(side=tk.LEFT, padx=10)

backward_button = tk.Button(root, text="Previous", command=traverse_backward)
backward_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
