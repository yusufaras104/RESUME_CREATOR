# Resume Creator

The **Resume Creator** is a Python application that allows users to create dynamic resumes using JSON data. It provides a simple and customizable way to generate a resume with six main sections: Personal Details, Personal Profile, Skillset, Employment History, Education and Training, Hobbies and Interests, and References.

## Features

- **Dynamic Resume Creation**: The application uses a JSON data structure to create and customize resumes with user-provided information.

- **Multiple Sections**: It offers six main sections, each of which can be filled with specific details.

- **PDF Resume Export**: The application can generate a PDF version of the resume based on the entered data.

## Prerequisites

Before you start using the Resume Creator, make sure you have the following prerequisites installed:

- Python 3.x: You can download Python from [python.org](https://www.python.org/downloads/).

- Required Python libraries: Install the necessary libraries using `pip`:


## Usage

1. Clone the repository to your local machine:


2. Navigate to the project directory:


3. Run the Python script:


4. Follow the on-screen prompts to enter information for each section of the resume.

5. Once you've provided all the required information, the application will save the resume data to a JSON file and generate a PDF resume named `resume.pdf`.

## Customization

- You can customize the JSON data structure in the `resume_data.json` file to add more fields or modify existing ones to suit your needs.

- To change the appearance of the generated PDF, you can modify the formatting in the `generate_pdf_resume` function in the `resume_creator.py` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [reportlab](https://www.reportlab.com/dev/docs/) and [fpdf](https://pyfpdf.readthedocs.io/en/latest/) libraries for PDF generation.

