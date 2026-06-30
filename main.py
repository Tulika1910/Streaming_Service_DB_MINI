import mysql.connector
import tkinter as tk
from tkinter import ttk

def get_db_connection():
    return mysql.connector.connect(host="localhost", 
                                   user="root", 
                                   password="tulika", 
                                   database="streaming_db")

def update_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
    SELECT m.title, m.type, c.category_name, IFNULL(p.rating, 'N/A')
    FROM Movies m
    LEFT JOIN Categories c ON m.category_id = c.category_id
    LEFT JOIN Preferences p ON m.movie_id = p.movie_id
    WHERE c.category_name = %s AND m.type = %s AND (p.rating >= %s OR p.rating IS NULL)
    """
    cursor.execute(query, (genre_combo.get(), type_combo.get(), rating_entry.get() or 0))
    
    for i in tree.get_children(): tree.delete(i)
    for row in cursor.fetchall(): tree.insert('', 'end', values=row)
    conn.close()


root = tk.Tk()
root.title("Movie Library Explorer")
root.geometry("700x500")


frame = ttk.Frame(root, padding="20")
frame.pack(fill='x')

ttk.Label(frame, text="Genre:").grid(row=0, column=0, padx=5)
genre_combo = ttk.Combobox(frame, values=["Action", "Comedy", "Drama", "Sci-Fi", "Romance", "Thriller"])
genre_combo.grid(row=0, column=1, padx=5)

ttk.Label(frame, text="Type:").grid(row=0, column=2, padx=5)
type_combo = ttk.Combobox(frame, values=["Movie", "Series"])
type_combo.grid(row=0, column=3, padx=5)

ttk.Label(frame, text="Min Rating:").grid(row=0, column=4, padx=5)
rating_entry = ttk.Entry(frame, width=5)
rating_entry.grid(row=0, column=5, padx=5)

ttk.Button(frame, text="Search Library", command=update_table).grid(row=0, column=6, padx=10)

tree = ttk.Treeview(root, columns=('Title', 'Type', 'Genre', 'Rating'), show='headings')
for col in ('Title', 'Type', 'Genre', 'Rating'):
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(pady=20, fill='both', expand=True, padx=20)

root.mainloop()