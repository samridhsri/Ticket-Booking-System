from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf(file_name, data):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list to store the flowables (content elements) that will be added to the PDF
    elements = []

    # Add a title to the PDF
    title = "Venue and Show Information"
    elements.append(Paragraph(title, styles['Title']))

    # Add some space after the title
    elements.append(Spacer(1, 12))

    # Format and add the table to the PDF
    venue_and_shows = data['venueAndShows']
    table_data = [['Venue ID', 'Show Name', 'Rating', 'Timing', 'Genre', 'Seats Available']]

    for venue, shows in venue_and_shows.items():
        for show in shows:
            table_data.append([
                show[0], show[1], show[2], show[3], show[4], show[5]
            ])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    
    # Build the PDF document
    doc.build(elements)

if __name__ == "__main__":
    # Example usage with the provided data:
    data = {
        'venues': [[1, 'Venue_01', 'IITM', 'Chennai', 250], [2, 'Venue_02', 'IIT Delhi', 'Delhi', 300]],
        'shows': [[1, 'Show-01', 4.7, '10.00 Am - 12.00 Am', 'Action, Thriller', 150, 'Venue_01', 244], [2, 'Batman', 9, '10 Am - 12 Am', 'Action, Adventure', 1200, 'Venue_02', 282]],
        'venueAndShows': {'Venue_01': [[1, 'Show-01', 4.7, '10.00 Am - 12.00 Am', 'Action, Thriller', 150, 'Venue_01', 244]], 'Venue_02': [[2, 'Batman', 9, '10 Am - 12 Am', 'Action, Adventure', 1200, 'Venue_02', 282]]}
    }

    file_name = "venue_and_shows.pdf"
    create_pdf(file_name, data)
    print(f"PDF created: {file_name}")
