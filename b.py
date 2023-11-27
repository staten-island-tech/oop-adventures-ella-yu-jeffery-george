import json
import os
class talents():
    def skills(self,title,effect):
        self.title= title
        self.effect= effect
        
    def to_dict(self):
        return {'title': title,
                'effect': effect,        
                 
        }
        
with open("data.json", "r") as f:

    data= json.load(f)
    
    title= input("Enter title of skill: ").capitalize()
    effect= input("Enter effect: ").capitalize()

    new_talents= talents()
    talents.skills("self","title","effect")

    new_talents_data= new_talents.to_dict()
    data.append(new_talents_data)

new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=2)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")

