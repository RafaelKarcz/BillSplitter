===========================
Bill Splitter Project
===========================

This document provides instructions for setting up the Python environment on a Linux system using Anaconda and Conda. The project involves a bill-splitting tool that calculates each friend's share of a bill, with an optional feature to designate one lucky friend who gets to skip paying. This project demonstrates basic Python skills such as working with dictionaries, handling user input, error checking, and using control flow statements.

Environment Setup
-----------------

1. **Creating a New Conda Environment:**

   To create a new isolated environment for the project:

   .. code-block:: bash

      conda create --name billsplitter python=3.12

   This command creates a new environment named ``billsplitter`` with Python 3.12.

2. **Activating the Environment:**

   Activate the created environment with the following command:

   .. code-block:: bash

      conda activate billsplitter

   This ensures that any Python operations or package installations are confined to this environment.

3. **Installing Necessary Packages:**

   Install any necessary packages (if applicable):

   .. code-block:: bash

      conda install random

Project Overview
----------------

This project allows users to split a bill equally between a group of friends and optionally pick one "lucky" person who gets to avoid paying their share. The program asks for user input to gather the number of participants, their names, and the total bill amount. It then calculates the amount each person should pay, accounting for the lucky feature.

**Core Skills Demonstrated:**

- **User Input Handling**: Collects names of participants and bill amount using `input()`.
- **Error Checking**: Validates that inputs (number of participants and bill amount) are integers.
- **Data Structures**: Uses dictionaries to map friend names to their respective share.
- **Control Flow**: Implements decision-making with `if-else` statements for splitting and the lucky feature.
- **Randomization**: Uses Python’s `random.choice()` to select a lucky friend.

Project Execution
-----------------

1. **Running the Bill Splitter:**

   To run the project, navigate to the directory containing `bill_splitter.py` and execute the script:

   .. code-block:: bash

      python bill_splitter.py

2. **Functionality:**

   - **Get Friend Count**: Prompts the user for the number of friends joining.
   - **Get Friend Names**: Collects the names of each participant.
   - **Get Total Bill**: Asks for the total bill value.
   - **Bill Splitting**: Divides the bill evenly among friends and allows the optional "lucky friend" feature, where one participant is randomly exempted from paying.

Example Execution
-----------------

The program will prompt the user step-by-step to gather necessary information. Here's an example session:

.. code-block:: text

   Enter the number of friends joining (including you): 4
   Enter the name of every friend (including you), each on a new line:
   John
   Mary
   Sarah
   You
   Enter the total bill value:
   1000
   Do you want to use the "Who is lucky?" feature? Write Yes/No:
   Yes
   Mary is the lucky one!

   Output:
   {'John': 333.33, 'Mary': 0, 'Sarah': 333.33, 'You': 333.33}

Project Features
----------------

- **Lucky Friend Feature**: Optionally exempts one friend from paying, redistributing the bill among the remaining participants.
- **Rounded Bill Splitting**: Ensures fair distribution, rounding the amount each friend pays to two decimal places if necessary.

Contributing
------------

Contributions to this project are welcome. Please ensure to maintain the environment specifications and follow the coding standards used in this project.

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file for details.
