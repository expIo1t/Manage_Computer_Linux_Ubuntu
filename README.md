# control_computer.py

This is a Python script that creates a simple graphical user interface (GUI) using the PySimpleGUI library to allow the user to control various computer functions via button clicks.

Operating system - "Linux Ubuntu 22.04.2" 🐧. 
The available commands include opening Firefox, Discord, Notepad, and Steam, as well as restarting or turning off the computer. 

Here is a breakdown of the code:

    - The "import" statements at the beginning of the script import the necessary libraries: os and "PySimpleGUI".

    - The "ControlComputer" class is defined, which contains the main logic of the program. The "__init__" method initializes the "commands" dictionary, which maps each command (e.g., "Firefox") to a corresponding function that will be called when the command is executed. The GUI is also set up in this method using the "sg.Button" method to create buttons for each command.

    - The "start" method is called to start the GUI loop, which waits for user input until the user closes the window or clicks the "Exit" button.

    - The "handle_command" method takes a command as input, checks if it is in the commands dictionary, and if it is, executes the corresponding function and displays a success message using the "sg.popup" method. If the command is not recognized, an error message is displayed.

    - The remaining methods are each associated with a command and perform the corresponding action. For example, "open_firefox" opens the Firefox browser using the "os.system" method.

    - The "update_output" method is not used in this script and can be ignored.

    - Finally, the "__name__ == '__main__'" block creates an instance of the "ControlComputer" class and calls the "start" method to run the program.

    - The "sg.theme" method sets the theme of the GUI, and the "sg.Window" method creates the main window. The "sg.Button" method is used to create buttons for each command, and the "window.read" method waits for user input and returns the event and values associated with that input.

    - The "os" library is used to execute system commands, such as opening programs or shutting down the computer.

The authors of the "PySimpleGUI" library are MikeTheWatchGuy and PySimpleGUI contributors.
The "os" library is part of the Python standard library.
