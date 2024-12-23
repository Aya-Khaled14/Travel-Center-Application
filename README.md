# Travel Center App

## Project Description

### Purpose:
The **Travel Center App** is a comprehensive solution for managing travel bookings, customer feedback, and historical records. It aims to streamline the booking process, collect customer feedback, and maintain an accessible history of bookings and reviews.

---

### Features:

#### User Interface:
- **Modern Design**: Clean and visually appealing interface with well-structured tabs and a cohesive color scheme.
- **Tab-based Navigation**: Divided into distinct tabs for:
  - Booking
  - Feedback
  - Feedback History
  - Booking History

#### Booking System:
- Allows users to input personal details:
  - Name, contact information, national ID.
- Select travel preferences:
  - Date, time, destination, and payment method.
- Integrates a **date picker** for easy selection of travel dates.
- Ensures **validation** of all fields before confirming bookings.
- Stores booking data in an **SQLite database** for persistence.

#### Feedback Management:
- Users can submit feedback for their experience using their **national ID**.
- Feedback data is stored alongside booking information in the database.

#### Feedback History:
- Displays all feedback entries in a **tabular format** for administrative review.
- Offers a "Refresh" button to update the feedback history dynamically.

#### Booking History:
- Maintains a detailed record of all bookings, showing:
  - Name, contact information, date, destination, and payment method.
- Features a "Refresh" button for **real-time data updates**.

#### Database Integration:
- Utilizes an **SQLite database** to store and manage booking and feedback data.
- Automatically creates the necessary tables if they do not exist.

#### Visual Elements:
- Includes **icons and images** to enhance the user experience.
- Uses **combo boxes** for dropdown selections, ensuring ease of use.

#### Validation:
- Validates inputs for booking and feedback to prevent incomplete submissions.
- Displays **error or success messages** based on user actions.

---

### Technologies Used:
- **Python**: For application logic and GUI development.
- **Tkinter**: To create the graphical user interface.
- **SQLite**: For data storage and management.
- **TkCalendar**: For the date picker functionality.

---

### Potential Use Cases:
- A travel agency wanting to digitize its booking system.
- A customer-facing application for bus or train services.
- A feedback collection tool for travel service providers.

---

### Future Enhancements:
- Add a **search feature** to filter booking and feedback records.
- Implement **user authentication** for enhanced security.
- Add **export functionality** to download history and feedback in CSV format.
- Integrate **email or SMS notifications** for booking confirmations.

---

This application is user-friendly, well-organized, and suitable for small to medium-sized travel agencies to manage operations effectively.
