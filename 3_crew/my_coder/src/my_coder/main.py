#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from my_coder.crew import MyCoder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    assignment = 'Write a python program to do k bandit problem'
    inputs = {
        'assignment': assignment
    }
    
    result = MyCoder().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()
    