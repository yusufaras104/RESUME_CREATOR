import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from fpdf import FPDF

# Function to load or create a JSON resume file
def load_or_create_resume(filename):
    try:
        with open(filename, 'r') as file:
            resume_data = json.load(file)
    except FileNotFoundError:
        resume_data = {
            "PersonalDetails": {
                "Name": "",
                "Mobile": "",
                "Email": "",
                "PostCode": ""
            },
            "PersonalProfile": "",
            "Skillset": "",
            "EmploymentHistory": [],
            "EducationAndTraining": [],
            "HobbiesAndInterests": "",
            "References": "Available on request"
        }
    return resume_data

# Function to save the resume data to a JSON file
def save_resume_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to generate a PDF resume
def generate_pdf_resume(data, pdf_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add sections to the PDF
    for section, content in data.items():
        pdf.add_page()
        pdf.cell(200, 10, txt=section, ln=True, align='C')

        # Check if the content is a dictionary
        if isinstance(content, dict):
            for key, value in content.items():
                pdf.multi_cell(0, 10, f"{key}: {value}", align='L')
        else:
            pdf.multi_cell(0, 10, txt=content, align='L')

    # Save the PDF to the specified filename
    pdf.output(pdf_filename)


# Main function to run the resume creator
def main():
    json_filename = 'resume_data.json'
    pdf_filename = 'resume.pdf'

    resume_data = load_or_create_resume(json_filename)

    # Collect user input for each section
    for section, content in resume_data.items():
        if isinstance(content, dict):
            for field in content:
                resume_data[section][field] = input(f"Enter {field}: ")
        else:
            resume_data[section] = input(f"Enter {section}: ")

    # Save the updated data to JSON
    save_resume_data(resume_data, json_filename)

    # Generate the PDF resume
    generate_pdf_resume(resume_data, pdf_filename)

if __name__ == "__main__":
    main()