# Attack Tree Generator

## Description

Attack Tree Generator is a CLI-based Python application which generates a visual attack tree from the data provided by the user in .json format. 

The app provides the following features:

- Generate a CLI-based attack tree based on the data provided in a .json file
- Make a risk assessment based on automated calculation of risk values (likelyhood of occureence) 
- Perform an analysis of different sce by changing values 
- Generate a visual attack tree (in .png format) based on the values provided by the user and calculated by the application

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Dependencies and Libraries

The application relies on a number libraries and have a few dependencies to provide the intended functionalities.

### Libraries

The application uses the following external libraries:

- anytree (Anytree, N.D.): Provides the basic features for attack trees such as Node class and attack tree representation.
- cmd (Python.org, N.D.): A simple framework for command line-oriented applications.
- json (Python.org, N.D.): A basic .json encoder and decoder for python.
- copy (Python.org, N.D.): Provides deepcopy() function to create a new compound object by recursively cloning child objects of the original.
- time: (Python.org, N.D.): Provides a variety of time-related functions. In the app, only sleep() function is used to the interaction more human-friendly (i.e. by pausing for certain time to allow the user to read the messages displayed).

### Dependencies

Graphviz
Python 3.6

Please follow the links in the references to know more about these external libraries.

## Installation

What are the steps required to install your project? Provide a step-by-step description of how to get the development environment running.

## Usage

Provide instructions and examples for use. Include screenshots as needed.

To add a screenshot, create an `assets/images` folder in your repository and upload your screenshot to it. Then, using the relative filepath, add it to your README using the following syntax:

    ```md
    ![alt text](assets/images/screenshot.png)
    ```
## Features

If your project has a lot of features, list them here.

## How to Contribute

If you created an application or package and would like other developers to contribute it, you can include guidelines for how to do so. The [Contributor Covenant](https://www.contributor-covenant.org/) is an industry standard, but you can always write your own if you'd prefer.

## Tests

Go the extra mile and write tests for your application. Then provide examples on how to run them here.

## License

The last section of a high-quality README file is the license. This lets other developers know what they can and cannot do with your project. If you need help choosing a license, refer to [https://choosealicense.com/](https://choosealicense.com/).

## References

Anytree (N.D.) Any Python Tree Data. Available from: https://anytree.readthedocs.io/en/2.8.0/ [Accessed: 10 April 2023]
Python.org (N.D.) cmd — Support for line-oriented command interpreters. Available from: https://docs.python.org/3/library/cmd.html [Accessed: 10 April 2023]
Python.org (N.D.) copy — Shallow and deep copy operations. Available from: https://docs.python.org/3/library/copy.html [Accessed: 10 April 2023]
Python.org (N.D.) json — JSON encoder and decoder. Available from: https://docs.python.org/3/library/json.html [Accessed: 10 April 2023]
Python.org (N.D.) time — Time access and conversions. Available from: https://docs.python.org/3/library/time.html [Accessed: 10 April 2023]

List your collaborators, if any, with links to their GitHub profiles.

If you used any third-party assets that require attribution, list the creators with links to their primary web presence in this section.

If you followed tutorials, include links to those here as well.