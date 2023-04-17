"""
The command prompt which is the backbone of the application.

Imports:
    from cmd: Cmd
    from helpers (app module): generate, calculate, visualise, analyse, load_file

Classes:
    Prompt

Functions:
    main()
    generate()
    calculate()
    visualise()
    analyse()
    load_file()
"""

from cmd import Cmd
from helpers import generate, calculate, visualise, analyse, load_file

class Prompt(Cmd):
    """A class for command prompt.

    Functions
    _________
    do_function (self, inp): Function that corresponds to a CLI command, which is
    "function" in this case.
    'help' is a  built-in function of Prompt() class which displays the documentation of a function.

    Note
    ____
    The CLI continues to run until a function returns True.

    """
    def do_load(self,inp):
        """Loads the .json file in the working directory to memory."""
        load_file()
        main()

    def do_generate(self, inp):
        """Generates the attack tree in the console."""
        generate()
        main()

    def do_calculate(self, inp):
        """Calculates the overall risk rating based on the probability values of the leaves."""
        calculate()
        main()

    def do_visualise(self, inp):
        """Produces a visual attack tree in .png format in the working directory."""
        visualise()
        main()

    def do_analyse(self, inp):
        """Allows user to enter specific values to leaves/leaf nodes and conduct analysis of
        different scenarios."""
        analyse()
        main()

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the Attack Tree Generator. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.


def main():
    """Provides a CLI menu explaining the available commands"""
    print("\n" + 104 * "=" + "\n" + 41 * " " + "ATTACK TREE GENERATOR\n" + 104 * "=")
    print("""Commands:
load -  (START HERE!) Loads a .json file. You can also reset the values by loading values from the file
generate - Generates an attack tree in the console (without any calculation)
calculate - Calculates the risk value based on the values given on the .json file for the leaves
visualise - Produces a graphical attack tree in .png format
analyse - Allows the user to modify/enter values to leaves and make calculations for various scenarios
help - Get help and review the documentation of a command (usage: help command)
exit - Exits the application
""")

main()
Prompt().cmdloop()
