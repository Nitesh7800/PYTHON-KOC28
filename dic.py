myDictionary={
"name":"Parashamt",
"age" :20,
"course": "Faishon design",
"assigment left":5,





}
#a=myDictionary["name"]
#a=myDictionary.keys()
#a=myDictionary.items()
#b=myDictionary.values
#print(myDictionary)

myDictionary = {
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}
print(myDictionary['class']['student']['marks']['web'])
