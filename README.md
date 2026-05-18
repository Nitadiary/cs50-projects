PROJECT TITLE: Medication Reminder

Video Demo: <https://youtu.be/4pdOXuI7r0k?si=LVuT-02zz9b3auUQ>

Description: The Medication Reminder project is a Python-based app designed for Patients and Healthcare Professionals to manage their medication schedules.

Some Patients have difficulty keeping track of when to take their medications, which can lead to poor treatment results and negatively affect their overall health.

The Medication Reminder application provides an easy-to-use method for entering your medicine name, dosage, frequency (specified in hours and minutes), and how long you will take the medication.

After entering the information, the Medication Reminder application will automatically create a complete schedule with every time you should take your medication, and it will show you when your next dose will be due.

The logic behind this application uses the datetime and timedelta modules that are part of the Python programming language, allowing you to calculate the exact time for all of your scheduled doses and keep in sync with the real world.

The Medication Reminder application uses programming techniques to develop a clinical solution that merges medical knowledge with technology. This application can be very helpful to patients who are taking many prescriptions at once, to their caregivers who are monitoring the patients for compliance and adherence, and to clinical researchers who are developing and testing medication protocols. By having an organized way to input and store data and a time-based calculation of dosage times, it can be demonstrated that one simple coding idea could help to improve patient adherence, safety, and therapeutic outcomes.

##Files
-project.py
contains the main program logic, including:
main: handles user input and program flow
c_regimen: building a dictionary representing the prescription regimen
g_schedule: generates a list of schedule doses
show_next: display the next upcoming dose

-test_project.py
Consists of unit testing the verification of the program, using “pytest.”

-requierments.txt
External librraries used in this program(in this case no external library used)

-README.me
Detailed description of the project

##How to run:
For running the program:
```bash
python project.py

to run the test:
```bash
pytest test_project.py

