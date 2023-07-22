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
    
def generate_pdf_file_show(data, pdf_file="show_details.pdf"):
    try:
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)

        c.drawString(50, 800, "Show Details:")
        c.drawString(50, 780, "ID    Show Name         Rating    Time             Genre                        Capacity    Venue Name     Ticket Price")

        y_position = 760
        for item in data:
            show_info = f"{item[0]:<5} {item[1]:<20} {item[2]:<9} {item[3]:<17} {item[4]:<30} {item[5]:<11} {item[6]:<14} {item[7]:<12}"
            c.drawString(50, y_position, show_info)
            y_position -= 20

        c.save()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"message": str(e)}


