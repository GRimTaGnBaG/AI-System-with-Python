# Building a Rule-Based AI System in Python

## Project Title

**Rule-Based Computer Troubleshooting Assistant**

## Project Overview

This project is a rule-based artificial intelligence system written in Python. The program helps users troubleshoot common computer problems by checking their input for predefined keywords and then applying logical rules.

The system does not use machine learning. Instead, it uses keyword groups, `if`, `elif`, and `else` statements, follow-up questions, and predefined troubleshooting steps.

---

# Part 1: Initial Project Ideas

## 1. Computer Troubleshooting Assistant

### Description

A system that helps users solve common computer problems, such as internet connection issues, frozen screens, application crashes, slow performance, sound problems, printer problems, and login issues.

### Rule-Based Approach

The system checks the user's input for predefined keywords. For example, if the user enters words such as "wifi," "internet," or "router," the program identifies the problem as an internet connection issue and provides troubleshooting steps.

## 2. Recipe Recommendation System

### Description

A system that recommends meals based on the ingredients the user has available.

### Rule-Based Approach

The system checks the ingredients entered by the user and compares them with predefined ingredient combinations. For example, if the user enters "eggs" and "cheese," the program recommends an omelet.

## 3. Study Recommendation Assistant

### Description

A system that recommends study strategies based on the subject, available study time, and the user's confidence level.

### Rule-Based Approach

The system uses predefined conditions. For example, if the user has less than 30 minutes and feels unprepared, the program recommends reviewing notes and completing a short practice quiz.

## Chosen Idea: Computer Troubleshooting Assistant

### Justification

I chose the Computer Troubleshooting Assistant because it is practical and relates to common problems that computer users experience. I am interested in technology, and this project allowed me to learn how a rule-based AI system can use user input, keywords, and logical conditions to recommend solutions. It also gave me many different rules to test and improve.

---

# Part 2: Rules and Logic for the Chosen System

The Computer Troubleshooting Assistant follows these rules:

## Safety and Overheating Rule

IF the user enters words such as "overheating," "smoke," "sparking," "burning smell," or "swollen battery," THEN the system tells the user to shut down the computer, disconnect the charger, and contact a technician.

## Internet Connection Rule

IF the user enters words such as "internet," "wifi," "router," "modem," "offline," or "network," THEN the system provides internet and network troubleshooting steps.

## Frozen Computer Rule

IF the user enters words such as "frozen," "stuck," "unresponsive," or "not responding," THEN the system provides steps for closing frozen applications and restarting the computer.

## Application Problem Rule

IF the user enters words such as "application," "program," "software," "crashed," "error," or "will not open," THEN the system provides software troubleshooting steps.

## Slow Computer Rule

IF the user enters words such as "slow," "lagging," "low memory," or "poor performance," THEN the system provides performance troubleshooting steps.

## Audio Rule

IF the user enters words such as "sound," "audio," "speaker," "headphones," "microphone," or "volume," THEN the system provides audio troubleshooting steps.

## Printer Rule

IF the user enters words such as "printer," "printing," "paper jam," "ink," or "toner," THEN the system provides printer troubleshooting steps.

## Login Rule

IF the user enters words such as "password," "login," "sign in," "account," or "locked out," THEN the system provides password and account troubleshooting steps.

## Power Rule

IF the user enters words such as "power," "will not turn on," "black screen," "no lights," or "startup," THEN the system provides power and startup troubleshooting steps.

## Storage Rule

IF the user enters words such as "storage," "disk," "space," "hard drive," or "out of space," THEN the system provides storage troubleshooting steps.

## Keyboard and Mouse Rule

IF the user enters words such as "keyboard," "mouse," "touchpad," "cursor," or "typing," THEN the system provides input-device troubleshooting steps.

## Display Rule

IF the user enters words such as "screen," "display," "monitor," "flickering," or "blurry," THEN the system provides display troubleshooting steps.

## USB Rule

IF the user enters words such as "USB," "flash drive," "external drive," or "not detected," THEN the system provides USB troubleshooting steps.

## Update Rule

IF the user enters words such as "update," "driver," "update failed," or "stuck update," THEN the system provides update troubleshooting steps.

## Virus and Malware Rule

IF the user enters words such as "virus," "malware," "popup," "hacked," or "suspicious," THEN the system provides security troubleshooting steps.

## Email Rule

IF the user enters words such as "email," "Outlook," "Gmail," or "attachment," THEN the system provides email troubleshooting steps.

## Short Input Rule

IF the user enters a very short description, THEN the system asks a follow-up question to collect more information.

## No Match Rule

IF the user's input does not match any keyword group, THEN the system displays a numbered menu and asks the user to select the closest problem category.

---

# Part 3: Sample Inputs and Outputs

## Test Case 1

### Input

```text
wifi
```

### Follow-Up Response

```text
no connection
```

### Output

```text
Diagnosis: Internet or network connection problem

Recommended Steps:
1. Make sure Wi-Fi is turned on and airplane mode is off.
2. Confirm that the correct Wi-Fi network is selected.
3. Check whether another device can connect to the same network.
4. Restart the computer.
5. Restart the modem and router by unplugging them for 60 seconds.
6. Try opening several different websites.
7. If using Ethernet, check both ends of the cable.
8. Use the operating system's network troubleshooter.
9. Forget the Wi-Fi network and reconnect using the password.
10. Contact the internet provider if every device is offline.
```

## Test Case 2

### Input

```text
my computer is running slowly
```

### Output

```text
Diagnosis: Slow computer or poor performance

Recommended Steps:
1. Close unused applications and browser tabs.
2. Restart the computer.
3. Check the amount of available storage space.
4. Open Task Manager and check CPU, memory, and disk usage.
5. Disable unnecessary startup programs.
6. Install operating-system updates.
7. Run a trusted antivirus or malware scan.
8. Remove unused applications.
9. Check whether the computer is overheating.
10. Consider adding memory or replacing an older hard drive.
```

## Test Case 3

### Input

```text
I forgot my password
```

### Output

```text
Diagnosis: Login, password, or account problem

Recommended Steps:
1. Confirm that Caps Lock and Num Lock are set correctly.
2. Check that the username or email address is correct.
3. Retype the password carefully.
4. Use the official password-reset option.
5. Check email or text messages for a verification code.
6. Wait briefly if too many attempts caused a temporary lock.
7. Try signing in from another browser or device.
8. Contact the school, workplace, or service administrator if needed.
```

---

# Part 4: Reflection

This project involved creating a rule-based Computer Troubleshooting Assistant in Python. The system asks the user to describe a computer problem or choose a category from a numbered menu. It converts the user's input to lowercase, checks the text for predefined keywords, and uses `if`, `elif`, and `else` statements to decide which troubleshooting advice to display. For example, if the user enters words such as "wifi," "internet," or "router," the system identifies an internet connection problem and provides a list of recommended steps. The program also asks follow-up questions when the user enters a short description.

One challenge I encountered was making the system recognize different ways that users may describe the same problem. The first version only recognized exact phrases such as "wifi not working." It did not recognize shorter descriptions such as "wifi," "wifi broken," or "internet doesnt work." To improve the program, I added larger keyword groups and text normalization. The normalization function converts common phrases such as "cant" into "cannot" and "wont" into "will not." This makes the keyword matching more reliable.

Another challenge was preventing the program from failing when the user provides very little information. I solved this by adding follow-up questions and a numbered help menu. The user can either describe the issue or select one of 16 supported categories. The program also runs inside a loop, allowing the user to troubleshoot multiple problems without restarting it.

This project helped me understand how rule-based AI differs from machine learning. A rule-based system follows instructions written by the programmer and cannot learn automatically. Its decisions are predictable and easy to explain, but it is limited to the rules and keywords included in the code. A machine-learning system can learn patterns from data, but its decisions may be less transparent.

---

# Program Requirements

- Python 3
- No external Python packages
- No machine-learning libraries

---

# How to Run the Program

Open a terminal in the folder containing the file and run:

```bash
python3 troubleshooter.py
```

On some Windows systems, use:

```powershell
python troubleshooter.py
```

---

# Repository Files

This repository contains:

```text
troubleshooter.py
requirements.txt
README.md
```

The `troubleshooter.py` file contains the complete rule-based system.

The `requirements.txt` file explains that the program does not require external packages.

The `README.md` file contains the project ideas, rules, test cases, reflection, and instructions for running the program.
