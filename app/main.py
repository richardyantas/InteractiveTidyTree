
#import pandas as pd
import numpy as np
#import json
import pytest

# https://tdhopper.com/blog/my-python-environment-workflow-with-conda
# https://github.com/full-stack-deep-learning/fsdl-text-recognizer-project/blob/master/setup.md
# https://stackoverflow.com/questions/42352841/how-to-update-an-existing-conda-environment-with-a-yml-file
# pytest main.py

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")


def func(x):
    return x+1

def test_answer():
    assert func(3) == 5

#tree = {}
#tree["flare"] = node("flare",null)
# tree[ data_csv[i].name ] = node(data_csv[i].name, null)


#data_csv = pd.read_csv("flare.csv")
#print(data_csv.head())
#data_csv = data_csv[0:15]
#csvTojson(data_csv)

test_answer()


'''
import cherrypy

class HelloWorld(object):
    #@cherrypy.expose
    def index(self):
        return "Hello World!"
cherrypy.quickstart(HelloWorld())
'''



'''
def csvTojson(data):
    root = {
        "name": "flare",
        "children": []
    }
    i=1
    it = root["children"]
    #print()
    #for i in range(i,len(data))
    while( np.isnan( data["value"][i] ) ):
        names = data["id"][i].split(".")
        it.append({"name": names[-1],"children": [] })
        print("i:", i)
    print(root)
node = {
    "name": "dl",
    "content_link": "src/name_.html",
    "parent": "flare",
    "children": []
}
'''




'''
class TreeJson:
    def __init__(self,name_root):
        self.data_json = {}
        self.data_json["name"]="flare"
        self.data_json["children"]=[]

    def addNode(self,path):
        it = self.data_json
        while(it["children"]):
            if it["name"]==path[j]:
                j=j+1


        print(path)

path = "flare.analytics"
path = path.split(".")

data_json_obj.addNode(path)

data_json = {}

data_json['name']="1"
data_json['children']=[]
data_json['children'].append(
    {
        'name': "1.2",
        'children': []
    }
)   

data_json['name'] = "1.3"
data_json['children'] = []
'''


# print( json.dump(data_json,indent=4) )
#print(json.dumps(data_json, indent=4, sort_keys=True))
# csv to json - implementation in python
# python -m Simple...Ht..  4000
#class node:
#    def __init__():

'''
def addNode(node_name,children_name):
    data['name'] = node_name 
    data['children'].append(
        {
            'name': children_name,
            'size': 1000
        }
    )



data['name']   = "deepLearning" 
data['children'] = []
data['children'].append(
    {
        'name': "LinearAlgebra",
        'children': []
    }
)

data['children'][0]['children'].append(
    {
        'name': "LinearSub",
        'children': []
    }
)

'''



# data['deepLearning']['LinearAlgebra']


'''
data['Children'] = []
data['Children'].append({
    'name':    'LinearAlgebra'
})

data['Children']

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
'''



