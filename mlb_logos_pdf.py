import os
import io
import mysql.connector
from mysql.connector import Error
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

script_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(script_dir, "mlb_logos_pdf")

# MySQL credentials
db_config = {
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': "localhost",
    'database': "mlb"
}

def fetch_all_logos():
    """Fetch team_abbr, team_name, logo blob from DB"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT team_abbr, team_name, logo FROM team_logos ORDER BY team_name")
    teams = cursor.fetchall()
    conn.close()
    return teams

def create_logo_pdf(teams, output_filename="mlb_logos_from_sql.pdf"):
    # Ensure save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Final full path
    output_path = os.path.join(save_dir, output_filename)
    
    # PDF settings
    page_width, page_height = letter
    c = canvas.Canvas(output_path, pagesize=letter)
    
    # Title
    title_text = "MLB Logos Stored in SQL Database"
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(page_width / 2, page_height - 40, title_text)
    
    # Grid settings
    cols = 5
    rows = 6
    cell_width = page_width / cols
    cell_height = (page_height - 80) / rows  # minus space for title
    
    x_offset_start = -5
    y_offset_start = page_height - 50  # start below title
    
    for idx, (abbr, name, logo_blob) in enumerate(teams):
        col = idx % cols
        row = idx // cols
        
        if row >= rows:
            # Only fit 30 logos on one page (5x6)
            break
        
        # Position in grid
        x = x_offset_start + col * cell_width + 8
        y = y_offset_start - (row + 1) * cell_height + 10
        
        # Convert logo blob into ImageReader
        logo_image = ImageReader(io.BytesIO(logo_blob))
        
        # Scale logos nicely (fit inside ~width 100, height 50)
        logo_width = cell_width * 0.8
        logo_height = cell_height * 0.6
        
        # Draw image
        c.drawImage(logo_image, x + (cell_width - logo_width) / 2, y + 10,
                    width=logo_width, height=logo_height, preserveAspectRatio=True, mask='auto')
        
        # Add team name below logo
        c.setFont("Helvetica", 8)
        c.drawCentredString(x + cell_width / 2, y + 2, f"{name} ({abbr})")
    
    c.showPage()
    c.save()
    print(f"✅ PDF created: {output_path}")

def main():
    teams = fetch_all_logos()
    print(f"Fetched {len(teams)} logos from database.")
    create_logo_pdf(teams)

if __name__ == "__main__":
    main()
