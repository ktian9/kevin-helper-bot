import psycopg2


conn = psycopg2.connect(database="accuweather",
                        host="localhost",
                        user="postgres",
                        password="8512201",
                        port="5432")


cursor = conn.cursor()


def insert_into_weathertable(query_params):
    
    try:
        
        cursor.execute(
                "prepare insert_weather_table as "
                "INSERT INTO daily_weather_logs VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17)")
        cursor.execute("execute insert_weather_table (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(query_params.values()))
        conn.commit()
        return "sucessfully added to database"
    except Exception as e:
        return "Something went wrong with insertion into weather table! {e}"