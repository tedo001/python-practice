from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A2
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ✅ CHANGE THIS PATH
file_path = "D:/New folder/python-practice/30_Day_AI_Study_Todo_List.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A2)
styles = getSampleStyleSheet()

title = Paragraph(
    "<b>tedo todo list</b>",
    styles["Title"]
)

table_data = [
    ["Day", "Focus Area", "Topics / Tasks", "Status"],
]

for day in range(1, 366):
    table_data.append([
        f"Day {day}",
        "",
        "",
        "      ☐ Done"
    ])

table = Table(table_data, colWidths=[50*30, 100, 220, 120])

table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("GRID", (0,0), (-1,-1), 1, colors.black),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("FONT", (0,0), (-1,0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0,0), (-1,0), 10),
    ("TOPPADDING", (0,0), (-1,0), 10),
]))

doc.build([title, table])

print("✅ PDF created successfully!")
