from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(text, output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []
    flowables.append(Paragraph(text, styles['Normal']))
    doc.build(flowables)

if __name__ == "__main__":
    input_text = """
A farmer had a goose that laid one golden egg a day. He would sell the golden eggs, and they enjoyed a comfortable life. However, the farmer became greedy and wanted more than one egg a day. His wife foolishly agreed to his idea. The next day the farmer cut open the goose after it laid the golden egg. He could only find blood and guts. He realised his mistake. He now had no source of income, and the couple became poorer every day.
    """
    output_filename = "egg.pdf"
    generate_pdf(input_text, output_filename)
    print(f"PDF generated successfully: {output_filename}")
