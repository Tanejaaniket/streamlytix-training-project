import psycopg2

conn_string = ""
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
  

def verify_user(data):
  try:
    cur.execute("""
      SELECT * FROM users 
      WHERE email = %s AND password = %s
    """,data)
    user_details = cur.fetchone()
    if user_details == None:
      return api_error("No such user found")
    print("verification sucessfully",user_details)
    return api_response(user_details)
  except Exception as e:
    print(e)
    return api_error(e)
  

def update_user_account(data):
  try:
    res = verify_user((data[len(data)-2],data[len(data)-1]))
    if res["status"]:
      cur.execute("""
        UPDATE users
        SET name = %s,email = %s,password = %s
        WHERE email = %s
      """,(data[0],data[1],data[2],data[3]))
      conn.commit()
      print("Update successfull")
      return api_response("")
    else:
      print("User not verified")
      return api_error("User not verified")
  except Exception as e:
    print(e)
    return api_error(e)
