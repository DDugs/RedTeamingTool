from fpdf import FPDF

def generate_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Red Team Report", ln=True, align='C')

    for entry in data:
        pdf.cell(200, 10, txt=f"{entry}", ln=True)

    pdf.output("report.pdf")
    print("PDF report generated.")

# Call this function after attacks are done to generate the final report
