from cmd import Cmd
import TreeGenerator

class Prompt(Cmd):
    def do_generate(self, inp):
        """Generates the attack tree based on the .json file in the working directory."""
        listdir()
        return

    def do_add(self, inp):
        """Adds two numbers together and provides the result. Example usage: add 2 4 (space is required between the numbers)"""
        num1 = int(inp[0])  # We typecast the input because the arguments are taken as strings.
        num2 = int(inp[2])  # inp[0] is the first number, inp[1] a space and inp[2] is the second number.
        result = num1 + num2
        print(f"Result: {result}")
        return

    def do_exit(self, inp):
        """Exists the shell"""
        print("Thanks for using the shell. Bye!")
        return True  # Returns true so that Cmd.postcmd() hook method can terminate the execution.

Prompt().cmdloop()