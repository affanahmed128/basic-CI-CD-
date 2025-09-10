import os
from file_writer import write_to_file

def test_write_to_file():
    
    test_filename = 'test_output.txt'
    test_content = 'Test content for Ci'
    write_to_file(test_filename, test_content)
    assert os.path.exists(test_filename), "File was not created"
    with open(test_filename, 'r') as file:
        content = file.read()
        assert content == test_content, "File content does not match"