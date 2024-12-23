import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkcalendar import Calendar
import sqlite3


class TravelCenterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Center")
        self.root.geometry("1200x800+50+0")
        icon = PhotoImage(file="travel.png")
        self.root.iconphoto(True, icon)

        # Define colors
        self.primary_color = "#86B6F6"  
        self.secondary_color = "#EEF5FF"  
        self.accent_color = "#176B87"  
        self.text_color = "#608BC1"  

        # Set background color for the root window
        self.root.configure(bg=self.secondary_color)

        # Initialize the database
        self.setup_database()

        # Application header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=100)
        header_frame.pack(fill="x")
        tk.Label(
            header_frame,
            text="Travel Center",
            font=("Lucida Handwriting", 36, "bold"),
            bg=self.primary_color,
            fg="white",
        ).pack(pady=25)

        # Tab control with larger tabs
        style = ttk.Style()
        #all tabs size font
        style.configure("TNotebook.Tab", font=("Arial", 16), padding=[10, 10])
        #all tabs postion
        style.configure("TNotebook", tabposition="n", background=self.secondary_color)
        #all tabs color
        style.configure("TFrame", background=self.secondary_color)  

        self.tab_control = ttk.Notebook(self.root, style="TNotebook")
        self.tab_control.pack(expand=1, fill="both")

        self.create_booking_tab(self.tab_control)
        self.create_feedback_tab(self.tab_control)
        self.create_feedback_history_tab(self.tab_control)
        self.create_history_tab(self.tab_control)

    def setup_database(self):
        
        #2 after import sqilt3
        self.conn = sqlite3.connect("travel_center.db")
        #3 create cursor
        self.cursor = self.conn.cursor()

        #create tabel
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                national_id TEXT NOT NULL,
                name TEXT NOT NULL,
                contact TEXT NOT NULL,
                travel_date TEXT NOT NULL,
                Passengers INTEGER NOT NULL,
                destination TEXT NOT NULL,
                travel_hour TEXT NOT NULL,
                payment TEXT NOT NULL,
                feedback TEXT,
                travel_from TEXT NOT NULL
            )
        ''')
       #5 save changes 
        self.conn.commit()

    def create_booking_tab(self, tab_control):
        booking_tab = tk.Frame(tab_control, bg=self.secondary_color)
        #add to nav bar
        tab_control.add(booking_tab, text="Booking")

        fields = [
            ("Full Name:", "name_entry"),
            ("National ID:", "national_id_entry"),
            ("Contact Number:", "contact_entry"),
            ("Travel Date:", "date_entry"),
            ("Number of Passengers:", "Passengers_entry"),
            ("Destination:", "destination_combobox"),
            ("Payment Method:", "payment_combobox"),
            ("From:", "from_entry")
        ]

        for i, (label_text, attr_name) in enumerate(fields):
            tk.Label(
                booking_tab,
                text=label_text,
                font=("Arial", 16),
                fg=self.text_color,
                bg=self.secondary_color
            ).grid(row=i, column=0, padx=20, pady=15, sticky="w")

            if attr_name == "destination_combobox":
                destination_options = [
                    "Cairo  135 EGP", "Alexandria 150 EGP", "Aswan 200 EGP", "Port Said 130 EGP",
                    "Ismailia 120 EGP", "Fayoum 250 EGP", "Tanta 170 EGP", "New Salhia City 100 EGP"
                ]
                setattr(self, attr_name, ttk.Combobox(booking_tab, font=("Arial", 16), values=destination_options,state='readonly' ,width=38))
                getattr(self, attr_name).grid(row=i, column=1, padx=20, pady=15)
                self.destination_combobox.set("select")

            elif attr_name == "payment_combobox":
                payment_options = ["Credit", "Cash", "InstaPay", "ApplePay"]
                setattr(self, attr_name, ttk.Combobox(booking_tab, font=("Arial", 16), values=payment_options,state='readonly' , width=38))
                getattr(self, attr_name).grid(row=i, column=1, padx=20, pady=15)
                self.payment_combobox.set("select")
            else:
                setattr(self, attr_name, tk.Entry(booking_tab, font=("Arial", 16), width=40))
                getattr(self, attr_name).grid(row=i, column=1, padx=20, pady=15)

        tk.Label(
            booking_tab,
            text="Travel Hour:",
            font=("Arial", 16),
            fg=self.text_color,
            bg=self.secondary_color
        ).grid(row=len(fields), column=0, padx=20, pady=15, sticky="w")

        self.hour_combobox = ttk.Combobox(booking_tab, font=("Arial", 16), values=[f"{i}:00" for i in range(24)],state='readonly' , width=38)
        self.hour_combobox.grid(row=len(fields), column=1, padx=20, pady=15)
        self.hour_combobox.set("select")
        tk.Button(
            booking_tab,
            text="Book Now",
            font=("Arial", 16, "bold"),
            command=self.book_now,
            bg=self.text_color,
            fg="white",
            height=1,
            width=18
        ).grid(row=len(fields) + 1, column=0, columnspan=2, pady=30)

        self.date_entry.bind("<Button-1>", self.open_date_picker)

        # Add image to the right of the form
        travel_image = PhotoImage(file="business-trip.png")  
        travel_image_resized = travel_image.subsample(2, 2)  
        
        image_label = tk.Label(booking_tab, image=travel_image_resized, bg=self.secondary_color)
        image_label.image = travel_image_resized  
        image_label.grid(row=0, column=2, rowspan=8, padx=20, pady=20)

    def create_feedback_tab(self, tab_control):
        feedback_tab = tk.Frame(tab_control, bg=self.secondary_color)
        tab_control.add(feedback_tab, text="Feedback")

        tk.Label(
            feedback_tab,
            text="Your Feedback",
            font=("Arial", 20, "bold"),
            fg=self.text_color,
            bg=self.secondary_color
        ).pack(pady=20)

        self.feedback_text = tk.Text(feedback_tab, font=("Arial", 16), height=10, width=70, bg=self.secondary_color, fg=self.text_color)
        self.feedback_text.pack(pady=20, padx=20)

        tk.Label(
            feedback_tab,
            text="National ID for Feedback:",
            font=("Arial", 16),
            fg=self.text_color,
            bg=self.secondary_color
        ).pack(pady=10)

        self.national_id_feedback_entry = tk.Entry(feedback_tab, font=("Arial", 16), width=40)
        self.national_id_feedback_entry.pack(pady=10)

        tk.Button(
            feedback_tab,
            text="Submit Feedback",
            font=("Arial", 16, "bold"),
            command=self.submit_feedback,
            bg=self.text_color,
            fg="white",
            height=2,
            width=20
        ).pack(pady=20)

    def create_feedback_history_tab(self, tab_control):
        feedback_history_tab = tk.Frame(tab_control, bg=self.secondary_color)
        tab_control.add(feedback_history_tab, text="Feedback History")

        columns = ("ID", "Name", "Feedback")
        self.feedback_history_tree = ttk.Treeview(feedback_history_tab, columns=columns, show="headings", height=15)

        for col in columns:
            self.feedback_history_tree.heading(col, text=col)
            self.feedback_history_tree.column(col, anchor="center", width=200)

        self.feedback_history_tree.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Button(
            feedback_history_tab,
            text="Refresh Feedback History",
            font=("Arial", 16, "bold"),
            command=self.load_feedback_history,
            bg=self.text_color,
            fg="white",
            height=2,
            width=20
        ).pack(pady=20)

    def create_history_tab(self, tab_control):
        history_tab = tk.Frame(tab_control, bg=self.secondary_color)
        tab_control.add(history_tab, text="History")

        columns = ("ID", "National ID", "Name", "Contact", "Date", "Passengers", "Destination", "Hour", "Payment", "From")
        self.history_tree = ttk.Treeview(history_tab, columns=columns, show="headings", height=15)

        for col in columns:
            self.history_tree.heading(col, text=col)
            self.history_tree.column(col, anchor="center", width=150)

        self.history_tree.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Button(
            history_tab,
            text="Refresh",
            font=("Arial", 16, "bold"),
            command=self.load_history,
            bg=self.text_color,
            fg="white",
            height=2,
            width=20
        ).pack(pady=20)

    def load_history(self):
        for row in self.history_tree.get_children():
            self.history_tree.delete(row)

        self.cursor.execute("SELECT * FROM bookings")
        rows = self.cursor.fetchall()
        for row in rows:
            self.history_tree.insert("", "end", values=row)

    def load_feedback_history(self):
        for row in self.feedback_history_tree.get_children():
            self.feedback_history_tree.delete(row)

        self.cursor.execute("SELECT id, name, feedback FROM bookings WHERE feedback IS NOT NULL")
        rows = self.cursor.fetchall()
        for row in rows:
            self.feedback_history_tree.insert("", "end", values=row)

    def book_now(self):
        name = self.name_entry.get()
        national_id = self.national_id_entry.get()
        contact = self.contact_entry.get()
        travel_date = self.date_entry.get()
        Passengers = self.Passengers_entry.get()
        destination = self.destination_combobox.get()
        travel_hour = self.hour_combobox.get()
        payment = self.payment_combobox.get()
        from_location = self.from_entry.get()

        if not all([name, national_id, contact, travel_date, Passengers, destination, travel_hour, payment, from_location]):
            messagebox.showerror("Error", "All fields are required.", icon="error")
            return

        self.cursor.execute(''' 
            INSERT INTO bookings (national_id, name, contact, travel_date, Passengers, destination, travel_hour, payment, travel_from)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (national_id, name, contact, travel_date, Passengers, destination, travel_hour, payment, from_location))
        self.conn.commit()

        messagebox.showinfo("Success", "Booking confirmed!", icon="info")
        self.clear_booking_form()
        self.load_history()

    def clear_booking_form(self):
        self.name_entry.delete(0, "end")
        self.national_id_entry.delete(0, "end")
        self.national_id_entry.set("")
        self.contact_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.Passengers_entry.delete(0, "end")
        self.destination_combobox.set("select")
        self.hour_combobox.set("select")
        self.payment_combobox.set("select")
        self.from_entry.delete(0, "end")

    def submit_feedback(self):
        feedback = self.feedback_text.get("1.0", tk.END).strip()
        national_id = self.national_id_feedback_entry.get().strip()

        if not feedback or not national_id:
            messagebox.showerror("Error", "Feedback and National ID are required.", icon="error")
            return

        self.cursor.execute(''' 
            UPDATE bookings
            SET feedback = ? 
            WHERE national_id = ? 
        ''', (feedback, national_id))
        self.conn.commit()

        messagebox.showinfo("Thank You", "Thank you for your feedback!", icon="info")
        self.feedback_text.delete("1.0", tk.END)
        self.national_id_feedback_entry.delete(0, "end")
        self.load_feedback_history()

    def open_date_picker(self, event=None):
        top = tk.Toplevel(self.root)
        top.title("Travel Date")
        icon = PhotoImage(file="travel.png")  
        top.iconphoto(True, icon)

        calendar = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
        calendar.pack(pady=20)

        def select_date():
            selected_date = calendar.get_date()
            self.date_entry.delete(0, "end")
            self.date_entry.insert(0, selected_date)
            top.destroy()

        tk.Button(top, text="Select Date", command=select_date).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = TravelCenterApp(root)
    root.mainloop()