from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import traceback
from flask import jsonify

def generate_pdf_file_venue(data, pdf_file="venue_details.pdf"):
    try:
        c = canvas.Canvas(pdf_file, pagesize=letter)


        c.setFont("Helvetica", 12)

        c.drawString(50, 800, "Venue Details:")
        c.drawString(50, 780, "ID    Venue Name       Location       Capacity")

        y_position = 760
        for item in data:
            venue_info = f"{item[0]:<5} {item[1]:<20} {item[2]:<15} {item[4]:<8}"
            c.drawString(50, y_position, venue_info)
            y_position -= 20

        c.save()
    except Exception as e:
        traceback.print_exc()
        return jsonify({"message": str(e)})

if __name__ == "__main__":
    data = [(1, 'Venue_01', 'IITM', 'Chennai', 250), 
            (2, 'Venue_02', 'IIT Delhi', 'Delhi', 300), 
            (5, 'Venue_03', 'Central Park', 'Delhi', 600)]

    generate_pdf_file_venue(data)
