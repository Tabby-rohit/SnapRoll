from src.database.config import supabase
import bcrypt
def hashpass(p):
    return bcrypt.hashpw(p.encode(),bcrypt.gensalt()).decode()
def checkpass(pwd,hashpwd):
    return bcrypt.checkpw(pwd.encode(),hashpwd.encode())



def check_teacher_exist(username):
    #checks unique useranme
    response=supabase.table("teacher").select("username").eq("username",username).execute()
    return len(response.data)>0
def create_teacher(username,password,name):
    data={"name":name,"username":username,"password":hashpass(password)}
    res=supabase.table("teacher").insert(data).execute()
    return res.data

def teacher_login(username,password):
    res=supabase.table("teacher").select("*").eq("username",username).execute()
    teacher=res.data[0]
    if checkpass(password,teacher["password"]):
        return teacher
    return None

def get_all_students():
    response=supabase.table("teacher").select("*").execute()
    return response.data