import os
import psycopg2
# Get the connection string from the environment variable
conn_string = "postgresql://neondb_owner:npg_mBWGJ3ZoFM9Q@ep-old-recipe-a1odeuyt-pooler.ap-southeast-1.aws.neon.tech/users?sslmode=require&channel_binding=require"

try:
  conn = psycopg2.connect(conn_string)
  cur = conn.cursor()
except Exception as e:
  print(e)

def insert_user(data):
  try:
    cur.execute("""
      INSERT INTO users (name,email,password) 
      VALUES (%s,%s,%s);
    """,data)
    conn.commit()
    print("Data inserted sucessfully")
    return True
  except Exception as e:
    print(e)
    return False
  

insert_user(("ani","a2@gmail.com","123456"))