import sys
import os

this_file_path = os.path.abspath(__file__)

project_root = os.path.dirname(os.path.dirname(os.path.dirname(this_file_path)))

if project_root not in sys.path:
    sys.path.append(project_root)


from exercices.exercice2 import delete_duplicate

def test_delete_duplicate():
    assert delete_duplicate([1, 1, 2, 2, 3, 1]) == [1, 2, 3, 1]
    assert delete_duplicate(['a', 'a', 'b', 'a']) ==  ['a', 'b', 'a']