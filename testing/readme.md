
This folder consists of unit tests for two primary functions of the SenOR Legal Advisor: 
`model` and `text_speech`. These functions are designed to generate responses to legal queries and convert text to speech, respectively. The tests are implemented using Python's `unittest` framework.

## Project Structure

- **back.py**: This file contains the implementations of the `model` and `text_speech` functions.
- **test_back.py**: This file contains the unit tests for the functions in `back.py`.
- **README.md**: This file provides an overview of the project and instructions for running the tests.

## Requirements

- Python 3.x
- `unittest` library (comes pre-installed with Python)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SenORLegalAdvisor.git
    cd SenORLegalAdvisor
    ```

2. Ensure you have Python 3 installed on your system.

## Running the Tests

To run the unit tests, execute the following command in your terminal:

```bash
python -m unittest test_back.py
