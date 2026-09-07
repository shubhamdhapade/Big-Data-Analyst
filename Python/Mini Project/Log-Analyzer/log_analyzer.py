import re
import csv
import sqlite3
from pathlib import Path
from typing import List, Dict, Any
import os

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / 'data' / 'sample_server.log'
OUTPUT_CSV = BASE_DIR / 'data' / 'cleaned_log.csv'
DB_FILE = BASE_DIR / 'data' / 'logs_db.sqlite3'

def parse_logs() -> List[Dict[str, Any]]:
    parsed_data = []
    pattern = r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(\S+)\s+(\d{3})\s+(\d+)ms'
    try:
        with open(LOG_FILE, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    date, time, method, endpoints, status, latency = match.groups()
                    parsed_data.append(
                        {
                            
                            'date': date,
                            'time': time,
                            'method': method,
                            'endpoints': endpoints,
                            'status': int(status),
                            'latency': int(latency)
                        }
                    )
    except FileNotFoundError:
        print(f"Error: The log file {LOG_FILE} was not found.")
    return parsed_data
    
def export_to_csv(data):
    with open(OUTPUT_CSV, 'w', newline='') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Successfully processed and exported {len(data)} log entries to {OUTPUT_CSV}")

def export_to_sqlite(data : List[Dict[str, Any]]) -> None:
    if not data:
        print("No data to export to SQLite.")
        return
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS server_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                    log_date TEXT,
                    log_time TEXT,
                    http_method TEXT,
                    endpoint TEXT,
                    status_code INTEGER,
                    latency_ms INTEGER
                )
            ''')
            insert_query = '''
                INSERT INTO server_logs (log_date, log_time, http_method, endpoint, status_code, latency_ms)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor.executemany(insert_query, [(entry.get('date'), entry.get('time'), entry.get('method'), entry.get('endpoints'), 
                                               entry.get('status'), entry.get('latency')) for entry in data])
            conn.commit()
            print(f"Successfully exported {len(data)} log entries to SQLite database {DB_FILE}")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
        return

def query_analystics() -> None:
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            
            print("Average latency per endpoint:")
            cursor.execute('''
                SELECT endpoint, AVG(latency_ms) as avg_latency
                FROM server_logs
                GROUP BY endpoint
            ''')
            for row in cursor.fetchall():
                print(f"Endpoint: {row[0]}, Average Latency: {row[1]:.2f} ms")
            
            print("\n--- Analytics Summary (SQLite) ---")
            
            cursor.execute("SELECT status_code, COUNT(*) FROM server_logs GROUP BY status_code")
            print("Status Code Breakdown:", cursor.fetchall())

            cursor.execute("SELECT AVG(latency_ms) FROM server_logs")
            print(f"Average Latency: {cursor.fetchone()[0]:.2f} ms")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
        return

if __name__ == "__main__":
    os.system('cls')
    parsed_logs = parse_logs()
    if parsed_logs:
        export_to_csv(parsed_logs)
        save_to_db = input("Do you want to save the parsed logs to SQLite database? (yes/no): ").strip().lower()
        if save_to_db == 'yes':
            export_to_sqlite(parsed_logs)
            query_analystics()
        else: 
            print("Parsed logs were not saved to the database.")
    else:
        print("No valid log entries found to process.")