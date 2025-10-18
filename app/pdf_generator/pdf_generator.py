from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import io

def generate_pdf(analysts, title: str):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    heading = ParagraphStyle("Heading", parent=styles["Heading2"], spaceAfter=12)
    story = [Paragraph(title, styles["Title"]), Spacer(1, 12)]

    for idx, analyst in enumerate(analysts, 1):
        story.append(Paragraph(f"Analyst {idx}: {analyst.name}", heading))
        story.append(Paragraph(f"<b>Role:</b> {analyst.role}", normal))
        story.append(Spacer(1, 6))

        swot_data = [
            ["Strengths", analyst.swot.get("Strengths", "")],
            ["Weaknesses", analyst.swot.get("Weaknesses", "")],
            ["Opportunities", analyst.swot.get("Opportunities", "")],
            ["Threats", analyst.swot.get("Threats", "")]
        ]
        swot_table = Table(swot_data, colWidths=[100, 380])
        swot_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey)
        ]))
        story.append(swot_table)
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Plan of Action</b>", normal))
        for step in analyst.plan_of_action:
            story.append(Paragraph(f"- {step}", normal))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Competitor Landscape</b>", normal))
        story.append(Paragraph(analyst.competitor_landscape, normal))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Marketing Suggestions</b>", normal))
        story.append(Paragraph(analyst.marketing_suggestions, normal))
        story.append(Spacer(1, 24))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
