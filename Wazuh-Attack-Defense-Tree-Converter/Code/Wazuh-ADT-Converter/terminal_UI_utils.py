
from colorama import Fore, Style
import sys

class PrintUtils:

    @staticmethod
    def get_white():
        return Style.RESET_ALL + '\n'

    @staticmethod
    def get_phase_prefix():
        return "] - "

    @staticmethod
    def print_in_purple(text, end = '\n'):
        print(Fore.MAGENTA+str(text)+PrintUtils.get_white(), end=end)
    
    @staticmethod
    def print_in_green(text, end="\n"):
        print(Fore.GREEN+str(text)+PrintUtils.get_white(), end=end)

    @staticmethod
    def print_in_red(text):
        print(Fore.RED+str(text)+PrintUtils.get_white())

    @staticmethod
    def print_in_orange(text, end="\n"):
        print(Fore.LIGHTRED_EX+str(text)+PrintUtils.get_white())       

    @staticmethod
    def print_phase_start(text):
        PrintUtils.print_in_purple("╔═════════════════════════════════════════════════════\n"+PrintUtils.get_phase_prefix()+str(text))

    @staticmethod
    def print_phase_end(text):
        PrintUtils.print_in_purple(PrintUtils.get_phase_prefix()+str(text)+"\n╚═════════════════════════════════════════════════════\n", end='')
        print('')
    
    @staticmethod
    def print_in_sky_blue(text):
        sky_blue = "\033[38;2;135;206;235m"
        print(sky_blue+str(text)+PrintUtils.get_white())

    @staticmethod
    def print_warning(text):
        PrintUtils.print_in_red(text)

    @staticmethod
    def print_equals_detatcher():
        PrintUtils.print_in_purple("============================================", end='')



class ExitUtils:

    @staticmethod
    def exit_with_message(message):
        PrintUtils.print_in_green(message)
        sys.exit()

    @staticmethod
    def exit_with_error(error):
        error = str(error)
        if "ERROR" not in error:
            error = "------------------------------\n\tERROR\n-------------------------------\n\n" + error
        PrintUtils.print_in_red(error)
        sys.exit()
