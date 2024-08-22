# Algorithm

# 1) Import Required Modules:
#    Import necessary modules and functions from the reportlab library, such as SimpleDocTemplate, Table, Paragraph,
#    TableStyle, colors, getSampleStyleSheet, and A4.
#    Define Data for the Table:

# 2) Create a list of lists (DATA) representing the data that will be displayed in the table. Each inner
#    list represents a row of the table, and each element in the inner list represents a column value.

# 3) Create a PDF Document Template:
#    Use SimpleDocTemplate to create a new PDF file named "receipt.pdf" with the A4 page size.

# 4) Define Styles:
#    Get a sample style sheet using getSampleStyleSheet() and store it in the styles variable.

# 5) Extract a specific style (e.g., Heading1) from the style sheet and store it in title_style.

# 6) Set the alignment of the title to center using title_style.alignment = 1.

# 7) Add a Title for the PDF:

# 8) Create a Paragraph object with the title and apply the title style to it.

# 9) Create a Table Object:
#    Create a Table object using the DATA list, which will display the data in a table format in the PDF.
   
# 10) Apply Styles to the Table:
#     Create a TableStyle object that defines the visual styles for the table, such as borders, grid lines, 
#     background colors, text colors, and alignment.
#     [
#     ("BOX", (0, 0), (-1, -1), 1, colors.black),
#     ("GRID", (0, 0), (-1, -1), 1, colors.black),
#     ("BACKGROUND", (0, 0), (-1, 0), colors.gray),  # Header background
#     ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
#     ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Align all cells to center
#     ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Cell background
# ]

# 11) Apply the style to the table using the table.setStyle(style) method.

# 12) Build the PDF with Title and Table:
#     Use the build() method of the SimpleDocTemplate object to generate the PDF file, including both the
#     title (title) and the table (table) in the document.


from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


DATA = [
    ["Date","Name","Subscription","Price(Rs .)"],
    ["20/08/2024","Web Dev","2 years","3000.00/-"],
    ["20/08/2024","DSA","2 years","3000.00/-"],
    ["SUBTOTAL","","","6000.00/-"],
    ["DISCOUNT","","","1000.00/-"],
    ["TOTAL","","","5000.00/-"],
]

pdf = SimpleDocTemplate("receipt_1.pdf",pagesize=A4)

styles = getSampleStyleSheet()
title_style = styles["Heading1"]

title_style.alignment = 1

title = Paragraph("LOOTCODE",title_style)

style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),  # Header background
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Align all cells to center
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Cell background
])

table = Table(DATA)
table.setStyle(style)

pdf.build([title,table])