### 1. main interface
![interface](images/interface.png)
this screen shows the main window where the user enter a password.



Password Analyzer & Generator

Overview

This is a Password Analyzer and Generator desktop application built with Python and Tkinter. The app helps users generate strong passwords, analyze password strength, and check if a password has been leaked in known data breaches using the Have I Been Pwned API.

The project is designed to improve user experience, reduce mistakes, and provide a clear understanding of password security.
 ________
Features
 • Password Strength Analysis
 • Scores passwords from 0 to 100
 • Categorizes passwords as Weak, Good, or Strong
 • Highlights missing elements (uppercase, lowercase, digits, symbols)
 • Color-coded feedback for visual clarity
 • Password Breach Check (API Integration)
 • Uses the Have I Been Pwned API
 • Detects if a password has appeared in known breaches
 • Password Generator
 • Generates strong random passwords with required complexity
 • Displays password directly in the interface
 • Buttons to Copy or Save the generated password
 • Clipboard & Paste Integration
 • Copy generated password with a single click
 • Paste directly into the analysis entry field for quick testing


 ________
 Usage
 1. Enter a password in the input field and click Analyze Password.
 2. The app will display:
 • Password strength score
 • Strength category (Weak, Good, Strong) with color
 • Recommendations for improvement
 • API breach check result
 3. Generate a strong password:
 • Click Generate to create a password
 • Click Copy to copy it to clipboard
 • Click Save to save it to passwords.txt
 4. Use Paste to insert a copied password into the analysis field.
 ________

Technologies Used
 • Python 3
 • Tkinter (GUI)
 • Requests (API requests)
