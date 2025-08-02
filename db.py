import os
import psycopg2
# Get the connection string from the environment variable
conn_string = "postgresql://neondb_owner:npg_mBWGJ3ZoFM9Q@ep-old-recipe-a1odeuyt-pooler.ap-southeast-1.aws.neon.tech/users?sslmode=require&channel_binding=require"

try:
  conn = psycopg2.connect(conn_string)
  cur = conn.cursor()
except Exception as e:
  print(e)

def api_response(data):
  return {
    "data":data,
    "status": True
  }

def api_error(err):
  return {
    "data":err or None,
    "status": False
  }

def register_user(data):
  try:
    cur.execute("""
      INSERT INTO users (name,email,password) 
      VALUES (%s,%s,%s);
    """,data)
    conn.commit()
    print("User registered sucessfully")
    return api_response(None)
  except Exception as e:
    print(e)
    return api_error(e)
  

def login_user(data):
  try:
    cur.execute("""
      SELECT * FROM users 
      WHERE email = %s AND password = %s;
    """,data)
    user_details = cur.fetchone()
    print(user_details)
    if user_details == None:
      return api_error("No user found")
    print("Login sucessfully")
    return api_response(user_details)
  except Exception as e:
    print(e)
    return api_error(e)
  

# login_user(("a2@gmail.com","123456"))
# register_user(("Aniket","a3@gmail.com","123456"))