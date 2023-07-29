import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

from hijri_converter import convert

def hijri_to_gregorian(h_year, h_month, h_day):
    # Convert the Hijri date to the AD date
    ad_date = convert.Hijri(h_year, h_month, h_day).to_gregorian()

    # Format the output date to a more readable format
    ad_date_str = ad_date.strftime("%Y-%m-%d")
    return ad_date_str

def convert_dates():
    try:
        # Get the selected Hijri date components from line edit fields
        day = int(entry_day.text())
        month = int(entry_month.text())
        year = int(entry_year.text())

        # Format the selected date to the Gregorian calendar
        ad_date_str = hijri_to_gregorian(year, month, day)
        label_output_ad.setText(f"The equivalent Gregorian (AD) date is: {ad_date_str}")

    except ValueError:
        label_output_ad.setText("Invalid input. Please enter valid Hijri date (YYYY MM DD).")

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Date Converter")

    # Create and configure the widgets
    label_hijri = QLabel("Enter a date in the Hijri calendar:")

    label_day = QLabel("Day:")
    label_month = QLabel("Month:")
    label_year = QLabel("Year:")

    # Date picker line edit widgets (Day, Month, Year)
    entry_day = QLineEdit()
    entry_month = QLineEdit()
    entry_year = QLineEdit()

    btn_convert = QPushButton("Convert")
    label_output_ad = QLabel()

    # Layout for the widgets
    layout = QGridLayout()
    layout.addWidget(label_hijri, 0, 0, 1, 3)

    layout.addWidget(label_day, 1, 0)
    layout.addWidget(entry_day, 1, 1)

    layout.addWidget(label_month, 1, 2)
    layout.addWidget(entry_month, 1, 3)

    layout.addWidget(label_year, 1, 4)
    layout.addWidget(entry_year, 1, 5)

    layout.addWidget(btn_convert, 2, 0, 1, 6)
    layout.addWidget(label_output_ad, 3, 0, 1, 6)

    # Set the layout for the main window
    window.setLayout(layout)

    # Connect the "Convert" button to the convert_dates function
    btn_convert.clicked.connect(convert_dates)

    # Show the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
