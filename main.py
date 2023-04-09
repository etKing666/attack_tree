from cmd import Cmd
from TreeGenerator import generate, calculate, visualise, analyse, load_file


class Prompt(Cmd):

    def do_load(self,inp):
        """Loads the .json file in the working directory to memory."""
        load_file()
        return
    def do_generate(self, inp):
        """Generates the attack tree in the console."""
        generate()
        return

    def do_calculate(self, inp):
        """Calculates the overall risk rating based on the probability values of the leaves."""
        calculate()
        return

    def do_visualise(self, inp):
        """Produces a visual attack tree in .png format in the working directory."""
        visualise()
        return

    def do_analyse(self, inp):
        """Allows user to enter specific values to leaves/leaf nodes and conduct analysis of different scenarios."""
        analyse()
        return

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the shell. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.

    def main():
        print("""
        ===================================
        ATTACK TREE GENERATOR
        ===================================
        Commands:
        load -  (START HERE!) Loads a .json file. You can also reset the values by loading values from the file
        generate - Generates an attack tree in the console 
        calculate - Calculates the risk value based on the values given on the .json file for the leaves
        visualise - Produces a graphical attack tree in .png format
        analyse - Allows the user to enter probability values to leaves and make calculations for various scenarios
        help - Get help and review the documentation of a command (usage: help command)
        exit - Exits the program
                """)

    main()
Prompt().cmdloop()
