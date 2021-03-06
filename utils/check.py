import hashlib

def hash(pword):
    h = hashlib.md5()
    h.update(pword)
    return h.hexdigest()

def load(filename):
    instream = open(filename, 'r') 
    content = instream.read() 
    instream.close()
    return content

def split(L):
    list=L.rsplit(',')
    i = 0
    dict={}
    while i < len(list)-1:
        dict[list[i]]=list[i+1]
        i+=2
    return dict

def isUser(d):
    dict = split(load("data/data.csv"))
    return d["user"] in dict.keys()

def check(d):    
    dict = split(load("data/data.csv"))
    if d["user"] in dict.keys():
        return hash(d["password"]) == dict[d["user"]]
    return false

def register(d):
    if isUser(d):
        print "Username already taken"
    else:
        outstream = open("data/data.csv",'a')
        outstream.write(d["user"]+","+hash(d["password"])+",")
        outstream.close()

if __name__=='__main__':
    register("Ely","Sandine")
    print split(load("../data/data.csv"))
    

