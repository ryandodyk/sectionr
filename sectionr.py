"""
Start point for command line application
"""
import math
from PyInquirer import prompt, style_from_dict, Token
from PyInquirer import Validator, ValidationError

from examples import custom_style_2

import os

#import steel.py
#import concrete.py
#import wood.py


# Validator for all number inputs, moves cursor to end of document after running
class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                    message='Please enter a number',
                    cursor_position=len(document.text))


# Just return material type for main function
def ask_material():
    material_prompt = [
        {
            'type': 'list',
            'name': 'material',
            'message': 'What Material?',
            'choices': ['Steel', 'Concrete', 'Wood'],
            'filter': lambda val: val.lower()
        }
    ]
    answers = prompt(material_prompt)
    return answers['material']


# Get member length and applied loads and returns as type dict
def member_info():
    loads_prompt = [ 
        {
            'type': 'input',
            'name': 'length',
            'message': 'Length of member (mm)',
            'validate': NumberValidator,
            'filter': lambda val: float(val)
        },
        {
            'type': 'confirm',
            'name': 'end_moment',
            'message': 'Moment connected member?'
        },
        {
            'type': 'input',
            'name': 'mf',
            'message': 'Maximum factored moment (kN*m)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
        },
        {
            'type': 'input',
            'name': 'vf',
            'message': 'Maximum factored shear (kN)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
        },
        {
            'type': 'input',
            'name': 'cr',
            'message': 'Factored Compression (kN)',
            'validate': NumberValidator,
            'filter': lambda val: float(val)
        },
        {
            'type': 'input',
            'name': 'end_moment1y',
            'message': 'End Moment 1 (strong direction) (kN*m)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
            'when': lambda answers: answers['end_moment']
        },
        {
            'type': 'input',
            'name': 'end_moment1x',
            'message': 'End Moment 1 (weak direction) (kN*m)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
            'when': lambda answers: answers['end_moment']
        },
        {
            'type': 'input',
            'name': 'end_moment2y',
            'message': 'End Moment 2 (strong direction) (kN*m)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
            'when': lambda answers: answers['end_moment']
        },
        {
            'type': 'input',
            'name': 'end_moment2x',
            'message': 'End Moment 2 (weak direction) (kN*m)',
            'validate': NumberValidator,
            'filter': lambda val: float(val),
            'when': lambda answers: answers['end_moment']
        }
    ]
    answers = prompt(loads_prompt)
    # Check that all end moment values are initialized in dict
    try:
        answers['end_moment1y']
    except:
        end_moments = {'end_moment1y': 0,
                'end_moment1x': 0,
                'end_moment2y': 0,
                'end_moment2x': 0}
        answers.update(end_moments)

    return answers

# Run steel design program and return outputs
def steel():
    steel_prompt = [
        {
            'type': 'list',
            'name': 'section',
            'message': 'What section profile?',
            'choices': ['W','HSS_Square','HSS_Rectangular','C','WT','L','2L','Pipe'],
            'filter': lambda val: val.lower()
        }
    ]
    design = prompt(steel_prompt)
    properties = member_info()
    # Combine section info with load info
    design.update(properties)
    print(design)
    # Run steel design program using design values collected
    #steel.main(design)
    
# Changes options presented to user depending on concrete section being designed
def concrete_member_types(answers):
    if answers['member_type'] == 'slab':
        options = ['One-Way','Two-Way']
    elif answers['member_type'] == 'beam':
        options = ['Rectangular','T']
    else:
        options = ['Rectangular','Circular']
    return options

# Run concrete design program and return outputs
def concrete():
    concrete_prompt = [
        {
            'type': 'list',
            'name': 'member_type',
            'message': 'Type of Member',
            'choices': ['Column', 'Beam', 'Slab'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'section',
            'message': 'What section profile?',
            'choices': concrete_member_types,
            'filter': lambda val: val.lower()
        }
    ]
    design = prompt(concrete_prompt)
    properties = member_info()
    # Combine section info with load info
    design.update(properties)
    #print("CONCRETE")

# Run wood design program and return outputs
def wood():
    wood_prompt = [
        {
            'type': 'list',
            'name': 'member_type',
            'message': 'Type of Member',
            'choices': ['Column', 'Beam'],
            'filter': lambda val: val.lower()
        }
    ]
    design = prompt(wood_prompt)
    properties = member_info()
    # Combine section info with load info
    design.update(properties)
    #print("WOOD")


### Main function, everything good starts here yo
def main():
    material = ask_material()
    if (material == 'steel'):
        steel()
    elif (material == 'concrete'):
        concrete()
    else:
        wood()


# Answers to questions stored as dict with format {'name': <'answer'>, ...}

if __name__ == "__main__":
    main()
