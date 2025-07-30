import os
import time
import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from io import BytesIO

# --- MySQL Configuration ---
db_config = {
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'host': 'localhost',
    'database': 'mlb'
}

# --- Create Table If Not Exists ---
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_headshots (
            player_id INT AUTO_INCREMENT PRIMARY KEY,
            full_name VARCHAR(100),
            team_name VARCHAR(100),
            height VARCHAR(20),
            weight VARCHAR(20),
            date_of_birth DATE,
            headshot LONGBLOB
        );
    """)
    conn.commit()

# --- Download image from headshot URL ---
def download_headshot_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"⚠️ Error downloading image: {e}")
    return None

# --- Insert player data into MySQL ---
def insert_player(conn, full_name, team_name, height, weight, birth_date, headshot_blob):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO player_headshots (full_name, team_name, height, weight, date_of_birth, headshot)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (full_name, team_name, height, weight, birth_date, headshot_blob))
        conn.commit()
    except Error as e:
        print(f"MySQL insert error for {full_name}: {e}")

# --- Parse the ESPN API and insert each player ---
def process_team_roster(conn, team_id):
    url = f"https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/{team_id}/roster"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch roster for team ID {team_id}")
        return

    data = response.json()
    team_name = data.get("team", {}).get("displayName", f"Team {team_id}")
    athlete_groups = data.get("athletes", [])

    for group in athlete_groups:
        for player in group.get("items", []):
            try:
                full_name = player.get("fullName", "").strip()
                height = player.get("displayHeight", "")
                weight = player.get("displayWeight", "")
                dob_raw = player.get("dateOfBirth", "")
                dob = datetime.strptime(dob_raw[:10], "%Y-%m-%d").date() if dob_raw else None
                headshot_url = player.get("headshot", {}).get("href", "")

                headshot_blob = download_headshot_image(headshot_url) if headshot_url else None

                if headshot_blob:
                    insert_player(conn, full_name, team_name, height, weight, dob, headshot_blob)
                    print(f"✅ Added {full_name} ({team_name})")
                else:
                    print(f"⚠️ Skipped {full_name} — No image")

            except Exception as e:
                print(f"❌ Error processing player: {e}")
                continue

# --- Main Script ---
def main():
    try:
        conn = mysql.connector.connect(**db_config)
        if not conn.is_connected():
            print("❌ Could not connect to MySQL.")
            return

        print("✅ Connected to MySQL.")
        create_table(conn)

        for team_id in range(1, 31):  # Team IDs 1–30
            print(f"\n🔎 Processing team ID {team_id}...")
            process_team_roster(conn, team_id)
            time.sleep(1)  # Be respectful to ESPN's servers

        conn.close()
        print("\n✅ All done. Database connection closed.")

    except Error as e:
        print(f"❌ MySQL error: {e}")

if __name__ == "__main__":
    main()
