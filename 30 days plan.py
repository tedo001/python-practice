from reportlab.platypus import SimpleDocTemplate, LongTable, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

file_path = "D:/New folder/python-practice/Tedo_365_Day_Todo_List.pdf"

doc = SimpleDocTemplate(
    file_path,
    pagesize=A4,
    rightMargin=20,
    leftMargin=20,
    topMargin=20,
    bottomMargin=20
)

styles = getSampleStyleSheet()

title = Paragraph("<b>Tedo – 365 Day Todo List</b>", styles["Title"])

table_data = [
    ["Day", "Focus Area", "Topics / Tasks", "Status"],
]

for day in range(1, 366):
    table_data.append([
        f"Day {day}",
        "",
        "",
        "☐ Done"
    ])

table = LongTable(
    table_data,
    colWidths=[50, 110, 260, 80],
    repeatRows=1   # header repeats on every page
)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 1), (-1, -1), 9),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
]))

doc.build([title, table])

print("✅ 365-Day Todo PDF created successfully!")

