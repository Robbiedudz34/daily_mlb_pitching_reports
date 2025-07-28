import os
import requests
import mysql.connector
from mysql.connector import Error

# ✅ ESPN API endpoint for all MLB teams
ESPN_API_URL = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams"

def connect_db(initial_db=None):
    try:
        conn = mysql.connector.connect(
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host="localhost",
            database=initial_db  # can be None for initial connection
        )
        if conn.is_connected():
            print(f"✅ Connected to MySQL{'' if not initial_db else ' (' + initial_db + ')'}")
            return conn
    except Error as e:
        print(f"❌ MySQL Error: {e}")
    return None

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mlb;")
    cursor.execute("USE mlb;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_logos (
            team_id INT AUTO_INCREMENT PRIMARY KEY,
            team_abbr VARCHAR(5) UNIQUE NOT NULL,
            team_name VARCHAR(100) NOT NULL,
            logo LONGBLOB NOT NULL
        );
    """)
    conn.commit()
    print("✅ team_logos table created/verified")

def fetch_team_list():
    resp = requests.get(ESPN_API_URL)
    if resp.status_code != 200:
        print("❌ Failed to fetch ESPN team data")
        return []
    
    data = resp.json()
    team_entries = []
    
    # ESPN returns 'sports' -> 'leagues' -> 'teams'
    for team in data.get("sports", [])[0].get("leagues", [])[0].get("teams", []):
        info = team["team"]
        abbr = info["abbreviation"]
        name = info["displayName"]
        logo_url = info["logos"][0]["href"] if info.get("logos") else None
        
        team_entries.append((abbr, name, logo_url))
    
    return team_entries

def download_logo(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.content  # raw PNG
    else:
        print(f"⚠️ Could not download logo: {url}")
        return None

def insert_logo(conn, team_abbr, team_name, logo_data):
    cursor = conn.cursor()
    query = """
        INSERT INTO team_logos (team_abbr, team_name, logo)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            team_name = VALUES(team_name),
            logo = VALUES(logo);
    """
    cursor.execute(query, (team_abbr, team_name, logo_data))
    conn.commit()

def main():
    # Step 1: connect WITHOUT a database so we can create mlb
    conn = connect_db(initial_db=None)
    if not conn:
        return
    
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS mlb;")
    conn.commit()
    cursor.close()
    conn.close()

    # Step 2: now reconnect specifying 'mlb'
    conn = connect_db(initial_db="mlb")
    if not conn:
        return

    create_table(conn)

    teams = fetch_team_list()
    print(f"Found {len(teams)} MLB teams")

    for abbr, name, logo_url in teams:
        if logo_url:
            logo_data = download_logo(logo_url)
            if logo_data:
                insert_logo(conn, abbr, name, logo_data)
                print(f"✅ Inserted {abbr} - {name}")

    conn.close()
    print("✅ All ESPN MLB logos stored in MySQL successfully")

if __name__ == "__main__":
    main()
