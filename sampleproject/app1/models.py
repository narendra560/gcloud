from django.db import models
from neo4j import GraphDatabase
database=GraphDatabase.driver(uri="neo4j+s://d4d2732f.databases.neo4j.io",auth=("neo4j","2_mP4qdXFEYSsqSY3zLsgQQl94-QumH9m-daGTcivfI"))
def getUsers():
    session=database.session()
    q="MATCH(n) return n"
    records=session.run(q)
    ans=[]
    for m in records:
        ans.append(m["n"]['name'])
    return ans
def createMCQ(d):
    session=database.session()
    q=f"CREATE(N:MCQ $props )"
    records=session.run(q,props=d)
    ans=[]
    for m in records:
        ans.append(m["N"]["id"])
    return ans
def fetchMCQS():
    session=database.session()
    q=f"MATCH(N:MCQ) WHERE N.submit='submit' return N"
    records=session.run(q)
    ans=[]
    for i in records:
        ans.append(i["N"])
    return ans
