### 1. Main interface
![interface](https://github.com/daliaali243/password_generator_and_analyzer/blob/48a82b60487ea9227f7bb53ed77dda2e65d3e121/interface.png)

this screen shows the main window where the user enter a password.

---

### 2. Week password result
![week password](https://github.com/daliaali243/password_generator_and_analyzer/blob/24b3a8945d177af36e690c625651027d537dd64e/week_password%20(2).png)

when the password is week, the result is dispayed in the red to clearly warn the user.

---

### 3. Strong password result


![strong password](https://github.com/daliaali243/password_generator_and_analyzer/blob/fd4426969575693537e36833694cf910ba86b7e5/strong_password%20(2).png)
---

### 4. Generate strong password
![generate password](https://github.com/daliaali243/password_generator_and_analyzer/blob/4eb1818a13000a2984cf42ffe4b70764eb13ea76/generate_password.png)


If the pssword is week, the application allows the user to generate a strong password automatically.
Password Analyzer & Generator

---


🔐 Password Analyzer and Generator

Overview

This is a Password Analyzer and Generator built using Python and Tkinter, following Object-Oriented Programming (OOP) principles.

The project helps users evaluate password strength, understand common security weaknesses, and generate strong passwords using real-world cybersecurity practices.
---

### Key Features
 • Analyze password strength based on:
 • Length
 • Uppercase and lowercase letters
 • Numbers
 • Special characters
 • Score passwords from 0 to 100 and classify them as Weak, Good, or Strong
 • Visual feedback using color indicators
 • Check passwords against known data breaches using Have I Been Pwned
 • Secure password generation with letters, numbers, and symbols
 • Copy, paste, and save generated passwords
 
---

### Security Design

Before being checked online, the password is hashed using SHA-1, and only a partial hash is sent to the Have I Been Pwned API.
This ensures the real password is never shared, following international security standards.

---

### Technical Design

The project is implemented using Python classes, applying Object-Oriented Programming to separate responsibilities such as:
 • Password analysis
 • Password generation
 • API communication
 • User interface handling

This design improves code clarity, scalability, and maintainability.

---

### Future Improvements
 • Integrate the system as a reusable security service across different applications
 • Add intelligent risk prediction using machine learning
 • Extend the project to web and mobile platforms



Technologies
 • Python
 • Tkinter
 • Object-Oriented Programming
 • Have I Been Pwned API
 • SHA-1 hashing
