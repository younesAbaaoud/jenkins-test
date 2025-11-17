import sys
import os

this_file_path = os.path.abspath(__file__)

project_root = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

if project_root not in sys.path:
    sys.path.append(project_root)

from exercices.exercice1 import addition,soustraction,multiplication,division

def test_addition():
    assert addition(1,2) == 3

def test_soustraction():
    assert soustraction(1,2) == -1

def test_multiplication():
    assert multiplication(1,2) == 2
    
def test_division():
    assert division(1,2) == 0.5