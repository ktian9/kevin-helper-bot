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
                "INSERT INTO daily_weather_logs VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18)")
        cursor.execute("prepare check_existing_active_channels as "
                       "select channel_id, user_submitted, accu_key from active_channels WHERE active_channels.channel_id=$1 AND active_channels.user_submitted=$2 AND active_channels.accu_key=$3") 
        cursor.execute(
                "prepare insert_active_channels as "
                "INSERT INTO active_channels VALUES ($1, $2, $3, $4, $5, $6)")
    except Exception as e:
        print("prepared statements already exist")
        conn.rollback()
    
    
    try:
       

        cursor.execute("execute check_existing_active_channels (%s, %s, %s)", (query_params['channel_id'], query_params['user_submitted'], query_params['accu_key']))
        if (len(list(cursor.fetchall())) == 0):
            print("active channel entry doesn't exist, creating new one")
            
            cursor.execute("execute insert_active_channels (%s, %s, %s, %s, %s, %s)", (query_params["channel_id"], 
                                                                   query_params["user_submitted"],
                                                                   query_params["accu_key"],
                                                                   query_params["tracked_state"],
                                                                   query_params["tracked_country"],
                                                                   query_params["tracked_name"]))
            conn.commit()
            cursor.execute("execute insert_weather_table (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(query_params.values()))
            conn.commit()
        else:
            conn.commit()
            print("record already exists, do nothing!")        
        return "sucessfully completion"
    except Exception as e:
        conn.rollback()
        return f"Something went wrong with insertion into weather table! {e}"

    
    
def get_channel_ids():
    try:
        cursor.execute("select DISTINCT channel_id from active_channels")
        
        if (len(list(cursor.fetchall())) == 0):
            return None
        else:
            return list(cursor.fetchall()[0])
    except Exception as e:
        print(f"Exception {e}")
        