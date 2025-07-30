import os
import io
import mysql.connector
from mysql.connector import Error
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# Get script path and create save folder
script_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(script_dir, "player_headshots_pdf")

db_config = {
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': "localhost",
    'database': "mlb"
}

def fetch_players_by_team():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT full_name, team_name, height, weight, date_of_birth, headshot
        FROM player_headshots
        ORDER BY team_name, full_name
    """)
    players = cursor.fetchall()
    conn.close()

    grouped = {}
    for full_name, team_name, height, weight, dob, blob in players:
        grouped.setdefault(team_name, []).append((full_name, height, weight, dob, blob))
    return grouped

def create_team_headshot_pdf(players_by_team, output_filename="team_player_headshots.pdf"):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    output_path = os.path.join(save_dir, output_filename)
    c = canvas.Canvas(output_path, pagesize=letter)
    page_width, page_height = letter
    cols = 5
    cell_width = page_width / cols
    cell_height = 120  # enough room for headshot and text

    for team, players in players_by_team.items():
        # Page title
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(page_width / 2, page_height - 40, f"{team} Headshots Stored in SQL")

        x_margin = 5
        y_position = page_height - 50
        for idx, (name, height, weight, dob, blob) in enumerate(players):
            col = idx % cols
            row = idx // cols
            x = x_margin + col * cell_width
            y = y_position - (row + 1) * cell_height

            if y < 10:  # prevent bottom overflow
                c.showPage()
                y_position = page_height - 80
                c.setFont("Helvetica-Bold", 18)
                c.drawCentredString(page_width / 2, page_height - 40, f"{team} Headshots Stored in SQL")
                col = 0
                row = 0
                x = x_margin
                y = y_position - cell_height

            try:
                # Draw headshot
                headshot_image = ImageReader(io.BytesIO(blob))
                c.drawImage(headshot_image, x + 10, y + 40, width=60, height=80, preserveAspectRatio=True, mask="auto")

                # Draw player info below image
                c.setFont("Helvetica", 6)
                c.drawCentredString(x + 40, y + 20, name)
                c.drawCentredString(x + 40, y + 12, f"{height}, {weight}")
                c.drawCentredString(x + 40, y + 4, f"DOB: {dob.strftime('%Y-%m-%d') if dob else 'N/A'}")

            except Exception as e:
                print(f"⚠️ Error drawing {name}: {e}")
                continue

        c.showPage()  # page break after each team

    c.save()
    print(f"✅ PDF created at {output_path}")

def main():
    players_by_team = fetch_players_by_team()
    create_team_headshot_pdf(players_by_team)

if __name__ == "__main__":
    main()
