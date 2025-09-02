#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from weatherai.crew import Weatherai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'city': 'Dublin',
        'date': '2025-09-03'
    }
    result = Weatherai().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()