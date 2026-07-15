# troubleshooter.py

"""
Advanced Rule-Based Computer Troubleshooting Assistant

This program demonstrates how rule-based artificial intelligence works.
It does not use machine learning. Instead, it uses predefined keywords,
IF/ELIF/ELSE statements, follow-up questions, and troubleshooting rules
to respond to the user's computer problem.

Requirements:
- Python 3
- No external packages are required
"""


# ---------------------------------------------------------
# KEYWORD GROUPS
# ---------------------------------------------------------

INTERNET_KEYWORDS = [
    "internet",
    "wifi",
    "wi-fi",
    "wireless",
    "router",
    "modem",
    "offline",
    "connection",
    "connect",
    "network",
    "ethernet",
    "website",
    "web page",
]

FROZEN_KEYWORDS = [
    "frozen",
    "freeze",
    "freezing",
    "stuck",
    "unresponsive",
    "not responding",
    "locked up",
    "hanging",
    "screen stuck",
]

APPLICATION_KEYWORDS = [
    "app",
    "application",
    "program",
    "software",
    "crash",
    "crashed",
    "crashing",
    "error",
    "will not open",
    "not opening",
    "keeps closing",
]

SLOW_KEYWORDS = [
    "slow",
    "slower",
    "lag",
    "lagging",
    "laggy",
    "takes forever",
    "poor performance",
    "low memory",
    "high cpu",
    "high memory",
]

AUDIO_KEYWORDS = [
    "sound",
    "audio",
    "speaker",
    "speakers",
    "headphones",
    "headset",
    "microphone",
    "mic",
    "volume",
    "mute",
    "cannot hear",
]

PRINTER_KEYWORDS = [
    "printer",
    "printing",
    "print",
    "paper jam",
    "ink",
    "toner",
    "print queue",
]

LOGIN_KEYWORDS = [
    "password",
    "login",
    "log in",
    "sign in",
    "username",
    "account",
    "locked out",
    "forgot password",
]

POWER_KEYWORDS = [
    "power",
    "turn on",
    "will not turn on",
    "not starting",
    "dead",
    "black screen",
    "no lights",
    "no power",
    "boot",
    "startup",
]

STORAGE_KEYWORDS = [
    "storage",
    "disk",
    "drive",
    "space",
    "full",
    "low space",
    "out of space",
    "hard drive",
    "ssd",
]

KEYBOARD_MOUSE_KEYWORDS = [
    "keyboard",
    "mouse",
    "touchpad",
    "trackpad",
    "cursor",
    "keys",
    "typing",
    "click",
]

DISPLAY_KEYWORDS = [
    "screen",
    "display",
    "monitor",
    "resolution",
    "flicker",
    "flickering",
    "blurry",
    "blank screen",
    "second monitor",
]

USB_KEYWORDS = [
    "usb",
    "flash drive",
    "external drive",
    "device not recognized",
    "not detected",
    "usb port",
]

UPDATE_KEYWORDS = [
    "update",
    "windows update",
    "driver",
    "installing update",
    "update failed",
    "stuck update",
]

VIRUS_KEYWORDS = [
    "virus",
    "malware",
    "popup",
    "pop up",
    "hacked",
    "suspicious",
    "redirect",
    "strange ads",
]

EMAIL_KEYWORDS = [
    "email",
    "mail",
    "outlook",
    "gmail",
    "send email",
    "receive email",
    "attachment",
]

OVERHEAT_KEYWORDS = [
    "overheating",
    "overheated",
    "very hot",
    "fan loud",
    "loud fan",
    "burning smell",
    "smoke",
    "spark",
    "sparking",
    "swollen battery",
    "battery swelling",
]


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def normalize_text(text):
    """
    Cleans the user's input so keyword matching is more reliable.
    """

    text = text.lower().strip()
    text = text.replace("’", "'")

    replacements = {
        "doesn't": "does not",
        "doesnt": "does not",
        "isn't": "is not",
        "isnt": "is not",
        "can't": "cannot",
        "cant": "cannot",
        "won't": "will not",
        "wont": "will not",
        "didn't": "did not",
        "didnt": "did not",
    }

    for old_text, new_text in replacements.items():
        text = text.replace(old_text, new_text)

    return text


def contains_keyword(text, keywords):
    """
    Returns True if any keyword from a list appears in the user's input.
    """

    return any(keyword in text for keyword in keywords)


def print_steps(title, steps):
    """
    Prints a diagnosis and a numbered list of troubleshooting steps.
    """

    print(f"\nDiagnosis: {title}")
    print("\nRecommended Steps:")

    for number, step in enumerate(steps, start=1):
        print(f"  {number}. {step}")


# ---------------------------------------------------------
# HELP MENU
# ---------------------------------------------------------

def display_help():
    """
    Displays the problems the assistant can help troubleshoot.
    """

    print("\nThis program can help with the following problems:\n")

    print("  1. Internet or Wi-Fi problems")
    print("  2. Frozen or unresponsive computer")
    print("  3. Applications that crash or will not open")
    print("  4. Slow computer performance")
    print("  5. Sound, speaker, headphone, or microphone problems")
    print("  6. Printer problems")
    print("  7. Login or password problems")
    print("  8. Computer will not turn on")
    print("  9. Storage or disk-space problems")
    print(" 10. Keyboard, mouse, or touchpad problems")
    print(" 11. Screen or monitor problems")
    print(" 12. USB or external-device problems")
    print(" 13. Windows or driver-update problems")
    print(" 14. Virus, malware, or suspicious activity")
    print(" 15. Email problems")
    print(" 16. Overheating or electrical hazards")

    print("\nYou may enter a number or describe the problem in your own words.")


# ---------------------------------------------------------
# FOLLOW-UP QUESTIONS
# ---------------------------------------------------------

def ask_follow_up(user_input):
    """
    Asks a follow-up question when the user's description is very short.
    """

    text = normalize_text(user_input)

    if len(text.split()) <= 2:
        print("\nYour description is short, so I need a little more information.")

        if contains_keyword(text, INTERNET_KEYWORDS):
            answer = input(
                "Is there no connection, a slow connection, "
                "or does the connection keep disconnecting? "
            )

        elif contains_keyword(text, DISPLAY_KEYWORDS):
            answer = input(
                "Is the screen black, frozen, flickering, blurry, "
                "or not detected? "
            )

        elif contains_keyword(text, AUDIO_KEYWORDS):
            answer = input(
                "Is there no sound, low sound, a microphone problem, "
                "or the wrong audio device? "
            )

        elif contains_keyword(text, PRINTER_KEYWORDS):
            answer = input(
                "Is the printer offline, not printing, jammed, "
                "or showing an error? "
            )

        elif contains_keyword(text, SLOW_KEYWORDS):
            answer = input(
                "Is the entire computer slow, or is only one application slow? "
            )

        elif contains_keyword(text, LOGIN_KEYWORDS):
            answer = input(
                "Did you forget the password, get locked out, "
                "or receive an error message? "
            )

        elif contains_keyword(text, POWER_KEYWORDS):
            answer = input(
                "Does the computer show lights, make sounds, "
                "or display a black screen? "
            )

        else:
            answer = input(
                "Please describe what is not working and what happens "
                "when you try to use it: "
            )

        return user_input + " " + answer

    return user_input


# ---------------------------------------------------------
# RULE-BASED TROUBLESHOOTING SYSTEM
# ---------------------------------------------------------

def troubleshoot_system(user_input):
    """
    Uses IF/ELIF/ELSE rules to identify the problem and provide advice.
    """

    user_input = ask_follow_up(user_input)
    text = normalize_text(user_input)

    print(f'\n[Rule-Based Diagnostics] Analyzing: "{user_input}"')

    # RULE 1: Safety and overheating issues
    if contains_keyword(text, OVERHEAT_KEYWORDS):
        print_steps(
            "Possible overheating or electrical hazard",
            [
                "Shut down the computer immediately.",
                "Disconnect the charger and all connected devices.",
                "Do not continue using the device if you see smoke, sparks, "
                "battery swelling, or smell burning.",
                "Move the device away from flammable materials.",
                "Contact a qualified repair technician.",
            ],
        )

    # RULE 2: Internet or Wi-Fi issues
    elif contains_keyword(text, INTERNET_KEYWORDS):
        print_steps(
            "Internet or network connection problem",
            [
                "Make sure Wi-Fi is turned on and airplane mode is off.",
                "Confirm that the correct Wi-Fi network is selected.",
                "Check whether another device can connect to the same network.",
                "Restart the computer.",
                "Restart the modem and router by unplugging them for 60 seconds.",
                "Try opening several different websites.",
                "If using Ethernet, check both ends of the cable.",
                "Use the operating system's network troubleshooter.",
                "Forget the Wi-Fi network and reconnect using the password.",
                "Contact the internet provider if every device is offline.",
            ],
        )

    # RULE 3: Frozen computer
    elif contains_keyword(text, FROZEN_KEYWORDS):
        print_steps(
            "Frozen or unresponsive computer",
            [
                "Wait at least 30 seconds because the computer may still be processing.",
                "Try moving the mouse or pressing the Caps Lock key.",
                "Press Ctrl+Shift+Esc to open Task Manager on Windows.",
                "Close the application marked as not responding.",
                "Save any work that is still accessible.",
                "Restart the computer if the system remains frozen.",
                "Check for system and application updates.",
                "Reduce the number of programs running at the same time.",
            ],
        )

    # RULE 4: Application problem
    elif contains_keyword(text, APPLICATION_KEYWORDS):
        print_steps(
            "Application or software problem",
            [
                "Close the application completely.",
                "Open the application again.",
                "Restart the computer.",
                "Check for an update to the application.",
                "Check for operating-system updates.",
                "Verify that the computer meets the application's requirements.",
                "Repair or reset the application if that option is available.",
                "Reinstall the application if the problem continues.",
                "Write down any error message for further troubleshooting.",
            ],
        )

    # RULE 5: Slow computer
    elif contains_keyword(text, SLOW_KEYWORDS):
        print_steps(
            "Slow computer or poor performance",
            [
                "Close unused applications and browser tabs.",
                "Restart the computer.",
                "Check the amount of available storage space.",
                "Open Task Manager and check CPU, memory, and disk usage.",
                "Disable unnecessary startup programs.",
                "Install operating-system updates.",
                "Run a trusted antivirus or malware scan.",
                "Remove unused applications.",
                "Check whether the computer is overheating.",
                "Consider adding memory or replacing an older hard drive.",
            ],
        )

    # RULE 6: Audio problem
    elif contains_keyword(text, AUDIO_KEYWORDS):
        print_steps(
            "Sound, speaker, headphone, or microphone problem",
            [
                "Make sure the computer is not muted.",
                "Increase the system volume.",
                "Check the volume inside the application.",
                "Confirm that the correct input or output device is selected.",
                "Disconnect and reconnect the headphones or speakers.",
                "Try a different USB or audio port.",
                "Restart the application.",
                "Restart the computer.",
                "Check for audio-driver updates.",
                "Test the device in another application.",
            ],
        )

    # RULE 7: Printer problem
    elif contains_keyword(text, PRINTER_KEYWORDS):
        print_steps(
            "Printer or printing problem",
            [
                "Make sure the printer is powered on.",
                "Check the USB, Wi-Fi, or Ethernet connection.",
                "Confirm that the correct printer is selected.",
                "Check for paper and ink or toner.",
                "Remove any paper jams.",
                "Clear stuck print jobs from the print queue.",
                "Restart the printer.",
                "Restart the computer.",
                "Remove and reinstall the printer if necessary.",
                "Check the manufacturer's website for driver updates.",
            ],
        )

    # RULE 8: Login problem
    elif contains_keyword(text, LOGIN_KEYWORDS):
        print_steps(
            "Login, password, or account problem",
            [
                "Confirm that Caps Lock and Num Lock are set correctly.",
                "Check that the username or email address is correct.",
                "Retype the password carefully.",
                "Use the official password-reset option.",
                "Check email or text messages for a verification code.",
                "Wait briefly if too many attempts caused a temporary lock.",
                "Try signing in from another browser or device.",
                "Contact the school, workplace, or service administrator if needed.",
            ],
        )

    # RULE 9: Power or startup problem
    elif contains_keyword(text, POWER_KEYWORDS):
        print_steps(
            "Power, startup, or boot problem",
            [
                "Make sure the power cable or charger is connected.",
                "Try a different wall outlet.",
                "Check whether the charging light turns on.",
                "Disconnect all unnecessary USB devices.",
                "Hold the power button for 10 to 15 seconds.",
                "Wait 30 seconds and try turning the computer on again.",
                "For a laptop, allow it to charge for at least 20 minutes.",
                "Try connecting an external monitor if the screen is black.",
                "Listen for fans, beeps, or startup sounds.",
                "Contact a technician if there are no signs of power.",
            ],
        )

    # RULE 10: Storage problem
    elif contains_keyword(text, STORAGE_KEYWORDS):
        print_steps(
            "Storage or disk-space problem",
            [
                "Check how much free space is available.",
                "Empty the Recycle Bin or Trash.",
                "Delete files that are no longer needed.",
                "Remove duplicate downloads.",
                "Uninstall unused applications.",
                "Move large files to an external drive.",
                "Use cloud storage for older files.",
                "Run the operating system's disk-cleanup tool.",
                "Restart the computer after freeing space.",
            ],
        )

    # RULE 11: Keyboard or mouse problem
    elif contains_keyword(text, KEYBOARD_MOUSE_KEYWORDS):
        print_steps(
            "Keyboard, mouse, touchpad, or cursor problem",
            [
                "Disconnect and reconnect the device.",
                "Try a different USB port.",
                "Replace or recharge the batteries if the device is wireless.",
                "Make sure Bluetooth is turned on if using Bluetooth.",
                "Restart the computer.",
                "Clean around stuck keys or sensor areas carefully.",
                "Test another keyboard or mouse.",
                "Check for driver updates.",
                "Make sure the touchpad was not disabled with a function key.",
            ],
        )

    # RULE 12: Display problem
    elif contains_keyword(text, DISPLAY_KEYWORDS):
        print_steps(
            "Display, monitor, or screen problem",
            [
                "Check that the monitor is powered on.",
                "Check the HDMI, DisplayPort, or other video cable.",
                "Try another cable or port.",
                "Press Windows+P to check the display mode on Windows.",
                "Restart the computer.",
                "Adjust the screen resolution and refresh rate.",
                "Update the graphics driver.",
                "Test with another monitor if available.",
                "Adjust the brightness if the display appears dim.",
            ],
        )

    # RULE 13: USB problem
    elif contains_keyword(text, USB_KEYWORDS):
        print_steps(
            "USB device or external-drive problem",
            [
                "Disconnect and reconnect the device.",
                "Try a different USB port.",
                "Restart the computer.",
                "Test the device on another computer.",
                "Check Device Manager for errors.",
                "Update the USB or device drivers.",
                "Avoid using an unpowered USB hub.",
                "Check whether the device appears in Disk Management.",
            ],
        )

    # RULE 14: Update problem
    elif contains_keyword(text, UPDATE_KEYWORDS):
        print_steps(
            "Operating-system or driver-update problem",
            [
                "Restart the computer.",
                "Check the internet connection.",
                "Make sure there is enough free storage space.",
                "Run the operating system's update troubleshooter.",
                "Pause and resume updates.",
                "Install updates one at a time if possible.",
                "Check for manufacturer driver updates.",
                "Write down any update error code.",
            ],
        )

    # RULE 15: Virus or malware problem
    elif contains_keyword(text, VIRUS_KEYWORDS):
        print_steps(
            "Possible malware or security problem",
            [
                "Disconnect from the internet if suspicious activity is occurring.",
                "Do not click suspicious pop-ups or links.",
                "Run a full scan with trusted security software.",
                "Remove unfamiliar browser extensions.",
                "Change important passwords from a safe device.",
                "Install operating-system and browser updates.",
                "Back up important files.",
                "Contact a trusted technician if the problem continues.",
            ],
        )

    # RULE 16: Email problem
    elif contains_keyword(text, EMAIL_KEYWORDS):
        print_steps(
            "Email problem",
            [
                "Check the internet connection.",
                "Confirm that the email address is typed correctly.",
                "Check the Spam or Junk folder.",
                "Restart the email application or browser.",
                "Sign out and sign back in.",
                "Check whether the mailbox is full.",
                "Try sending a message to yourself.",
                "Check attachment-size limits.",
                "Reset the password if sign-in fails.",
            ],
        )

    # DEFAULT RULE
    else:
        print("\nI could not confidently identify the problem.")
        print("Please choose the category that is closest to your issue:\n")

        display_help()

        choice = input("\nEnter a number from 1 to 16: ").strip()

        fallback_inputs = {
            "1": "internet not working",
            "2": "computer frozen",
            "3": "application crashed",
            "4": "computer slow",
            "5": "sound not working",
            "6": "printer not working",
            "7": "cannot log in",
            "8": "computer will not turn on",
            "9": "storage full",
            "10": "keyboard not working",
            "11": "screen problem",
            "12": "usb device not detected",
            "13": "update failed",
            "14": "possible virus",
            "15": "email not working",
            "16": "computer overheating",
        }

        if choice in fallback_inputs:
            troubleshoot_system(fallback_inputs[choice])
        else:
            print("\nThat selection was not recognized.")
            print("Please try again and enter a number from 1 to 16.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():
    """
    Runs the troubleshooting assistant in an interactive loop.
    """

    menu_choices = {
        "1": "internet not working",
        "2": "computer frozen",
        "3": "application crashed",
        "4": "computer slow",
        "5": "sound not working",
        "6": "printer not working",
        "7": "cannot log in",
        "8": "computer will not turn on",
        "9": "storage full",
        "10": "keyboard not working",
        "11": "screen problem",
        "12": "usb device not detected",
        "13": "update failed",
        "14": "possible virus",
        "15": "email not working",
        "16": "computer overheating",
    }

    print("=" * 68)
    print("Advanced Rule-Based Computer Troubleshooting Assistant")
    print("=" * 68)

    display_help()

    print("\nExamples of descriptions you can enter:")
    print("  wifi")
    print("  my screen is black")
    print("  the computer is running slowly")
    print("  my printer will not print")
    print("  I forgot my password")

    print("\nType 'help' to show the menu again.")
    print("Type 'quit' or 'exit' to close the program.")

    while True:
        try:
            user_input = input(
                "\nEnter a problem description or menu number: "
            ).strip()

            if not user_input:
                print("Please enter a problem description or menu number.")
                continue

            command = user_input.lower()

            if command in ["quit", "exit", "q"]:
                print("\nThank you for using the troubleshooting assistant.")
                break

            if command in ["help", "menu", "options"]:
                display_help()
                continue

            if user_input in menu_choices:
                user_input = menu_choices[user_input]
                print(f"\nYou selected: {user_input}")

            troubleshoot_system(user_input)

        except KeyboardInterrupt:
            print("\n\nProgram stopped by the user.")
            break

        except EOFError:
            print("\nProgram ended.")
            break

        except Exception as error:
            print("\nAn unexpected error occurred.")
            print(f"Technical details: {error}")
            print("Please try again with another description.")


# Run the program.
if __name__ == "__main__":
    main()