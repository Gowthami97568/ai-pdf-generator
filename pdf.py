from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(content, filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)

    styles = getSampleStyleSheet()
    story = []

    lines = content.split("\n")

    for i, line in enumerate(lines):
        line = line.strip()

        if not line:
            continue

        # Title
        if i == 0:
            story.append(Paragraph(f"<b>{line}</b>", styles["Title"]))
            story.append(Spacer(1, 15))

        # Headings
        elif ":" in line:
            story.append(Paragraph(f"<b>{line}</b>", styles["Heading2"]))
            story.append(Spacer(1, 10))

        # Normal text
        else:
            story.append(Paragraph(line, styles["BodyText"]))
            story.append(Spacer(1, 10))

    doc.build(story)