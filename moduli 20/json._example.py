person = {
    "name":"John Doe",
    "age":17,
    "address":{
        "street":"123 Main St",
        "city":"Anytown",
        "state":"Ca",
    },
    "Contact":[
        {
            "type":"email",
            "value":"johndoe@gmail.com"
        },
        {
            "type":"phone",
            "value":"324-185-352"

        }
    ]
}

print(person["name"])
print(person["age"])
print(person["address"]["city"])
print(person["contact"][1]["value"])