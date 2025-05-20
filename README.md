Coffee Shop Challenge


USE 
PYTHONPATH=".." pipenv run python debug.py

Project Overview

This is a Python-based implementation of the Coffee Shop Challenge, a simulation of an automatic coffee dispensing machine called the Barista-matic. The application manages an inventory of coffee ingredients, dispenses a fixed set of drinks, and updates the inventory based on sales. The system ensures drinks are only dispensed if sufficient ingredients are available and supports restocking to restore inventory levels.

Features

Inventory Management:
 Tracks ingredients like
 
  Cocoa, Coffee, Cream, Decaf Coffee, Espresso, Foamed Milk, Steamed Milk, Sugar, and Whipped Cream.



Drink Dispensing: Supports six drinks: Caffe Americano, Caffe Latte, Caffe Mocha, Cappuccino, Coffee, and Decaf Coffee, each with specific ingredient requirements and costs.



Dynamic Menu:

 Displays only drinks that can be made with the current inventory.



Restocking:

 Restores each ingredient to a maximum of 10 units upon restock command.



Command-Line Interface:

 Accepts user inputs to dispense drinks or restock inventory.

PREREQUISITES

Python 3.8 or higher

No external libraries are required

PROJECT STRUCTURE

Coffee.py: Contains the core classes (Ingredient, Drink, Inventory, BaristaMatic) for managing ingredients, drinks, and the coffee machine logic.

Implementation Details

Classes:

Ingredient: Represents an ingredient with a name and unit cost.

Drink: Represents a drink with a name, ingredients, and cost calculation.

Inventory: Manages ingredient quantities and checks availability.

BaristaMatic: Orchestrates the coffee machine, handling inventory, menu display, and drink dispensing.

Input Handling: Reads commands from standard input, ignoring blank lines.

Error Handling: Validates user input and checks ingredient availability before dispensing drinks.


License

This project is licensed under the MIT License. See the LICENSE file for details.



