from cmd import Cmd
from TreeGenerator import generate, calculate


class Prompt(Cmd):

    def do_generate(self, inp):
        """Generates the attack tree based on the .json file in the working directory."""
        generate()
        return

    def do_calculate(self, inp):
        """Calculates the overall risk rating based on the probability values of the leaves."""
        calculate()
        return

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the shell. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.


Prompt().cmdloop()
