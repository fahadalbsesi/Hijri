Description:
This repository contains a simple Python application for converting dates from the Hijri calendar to the Gregorian calendar. The program utilizes the hijri_converter library to perform the conversion. The graphical user interface (GUI) is built using the PyQt5 library, allowing users to easily input a date in the Hijri calendar (year, month, and day) and obtain the corresponding date in the Gregorian calendar. The application was developed to offer users a convenient tool for converting dates between two widely used calendars, particularly useful for individuals who regularly work with both Hijri and Gregorian dates. The project is open-source and encourages contributions from the community to enhance its functionality or improve the user experience.

Code Usage:
The Python script within the repository (hijri_to_gregorian_converter.py) contains the main application logic. It imports the tkinter or PyQt5 library for GUI development, depending on the chosen version. The hijri_converter library is used for converting Hijri dates to Gregorian dates. Users interact with the GUI by entering the desired Hijri date into separate entry fields for day, month, and year. Upon clicking the "Convert" button, the program handles the conversion using the hijri_to_gregorian function, and the equivalent Gregorian date is displayed on the screen. The application ensures input validation to handle any potential errors gracefully. Users can easily build a standalone executable (.exe) file using PyInstaller, as explained in the project's documentation, to run the converter without the need for a Python environment. The project aims to be user-friendly and expandable, providing a helpful resource for anyone needing to convert dates between the Hijri and Gregorian calendars.


 to install just pip install -r requirements.txt
 Explanation:

PyQt5==5.15.4: This line specifies the required version of the PyQt5 library. Replace 5.15.4 with the version you have installed. If you don't have PyQt5 installed, you can install it using pip install PyQt5.

hijri-converter==2.1.1: This line specifies the required version of the hijri_converter library. Replace 2.1.1 with the version you have installed. If you don't have hijri_converter installed, you can install it using pip install hijri-converter.

To use this requirements.txt file, you can follow these steps:

Create a new folder for your project (if you haven't already) and place your Python script (hijri_to_gregorian_converter.py) in it.

Create a new file in the same folder and name it requirements.txt.

Copy the content provided above into the requirements.txt file.

Open a terminal or command prompt, navigate to your project folder, and run the following command to install the required packages:
