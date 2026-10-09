from src.database.config import supabase
import bcrypt
def hashpass(p):
    return bcrypt.hashpw(p.encode(),bcrypt.gensalt()).decode()
def checkpass(pwd,hashpwd):
    return bcrypt.checkpw(pwd.encode(),hashpwd.code())



def check_teacher_exist(username):
    #checks unique useranme
    response=supabase.table("teacher").select("username").eq("username",username).execute()
    return len(response)>0
def create_teacher(username,password,name):
    data={"name":name,"username":username,"password":hashpass(password)}
    res=supabase.table("teacher").insert(data).execute()
    return res.data

def teacher_login(username,password):
    res=supabase.table("teacher").select("*").eq("useranme",username).execute()
    teacher=res[0]
    if checkpass(password,teacher["password"]):
        print("correct")