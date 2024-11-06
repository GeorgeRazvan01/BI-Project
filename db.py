import psycopg2-binary
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )
    return connection

# Example query function to fetch sales by decoration type
def get_sales_by_decoration_type():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT decoration_type, SUM(total_price) as total_sales
        FROM Sale
        JOIN Decoration ON Sale.ID_Decoration = Decoration.ID_Decoration
        GROUP BY decoration_type
        ORDER BY total_sales DESC
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

