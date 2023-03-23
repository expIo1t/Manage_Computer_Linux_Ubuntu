import os
import PySimpleGUI as sg

class ControlComputer:
    def __init__(self):
        self.commands = {
            '𝗙𝗜𝗥𝗘𝗙𝗢𝗫': self.open_firefox,
            '𝗗𝗜𝗦𝗖𝗢𝗥𝗗': self.open_discord,
            '𝗡𝗢𝗧𝗘𝗣𝗔𝗗 ': self.open_notepad,
            '𝗦𝗧𝗘𝗔𝗠': self.open_steam,
            '𝗥𝗘𝗦𝗧𝗔𝗥𝗧': self.restart_computer,
            '𝗧𝗨𝗥𝗡 𝗢𝗙𝗙': self.turn_off_computer,
            '𝗘𝗫𝗜𝗧': self.exit_program
        }

        sg.theme('Black') # set the theme to black

        layout = [[sg.Button(command, size=(10, 2), pad=(5,5)) for command in self.commands.keys()]]

        self.window = sg.Window('𝗖𝗼𝗻𝘁𝗿𝗼𝗹 𝗖𝗼𝗺𝗽𝘂𝘁𝗲𝗿 𝗣𝗮𝗻𝗲𝗹', layout)

    def start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            self.handle_command(event)

        self.window.close()

    def handle_command(self, command):
        if command in self.commands:
            self.commands[command]()
            sg.popup(f"𝗖𝗼𝗺𝗺𝗮𝗻𝗱 '{command}' 𝗲𝘅𝗲𝗰𝘂𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.", title='𝗦𝗨𝗖𝗖𝗘𝗦𝗦')
        else:
            sg.popup(f"𝗘𝗿𝗿𝗼𝗿: 𝗨𝗻𝗸𝗻𝗼𝘄𝗻 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 '{command}'.", title='𝗘𝗥𝗥𝗢𝗥')

    def open_firefox(self):
        os.system("firefox")

    def open_discord(self):
        os.system("discord")

    def open_notepad(self):
        os.system("gedit")

    def open_steam(self):
        os.system("steam")

    def restart_computer(self):
        os.system("sudo reboot")

    def turn_off_computer(self):
        os.system("sudo poweroff")

    def exit_program(self):
        self.window.close()

    def update_output(self, message):
        self.window['output'].update(value=message)

if __name__ == '__main__':
    nn = ControlComputer()
    nn.start()
