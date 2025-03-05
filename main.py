from flask import Flask, Response
from faker import Faker
import json
 
 
app = Flask(__name__)
#Tento řádek je potřebný pro vytvoření formátu na českých jménech, případech atd
fake = Faker("cs_CZ")
 
#generace pro 1 človeka
def generate_user():
#Tento řádek slouží k tomu, aby neukazoval zbytečné hodnoty, například /n.
    address = fake.street_address() + ", " + fake.postcode() + " " + fake.city()
    first_name = fake.first_name().lower()  
    last_name = fake.last_name().lower()   
    email = f"{first_name}.{last_name}@example.com"  
    return {
        "name": first_name,            # jmeno
        "last_name": last_name, #prijmeni
        "address": address,#fake.address().replace("/n", ", "),# adresa
        "email":email,#fake.email(),         # poštaa/email
        "username": fake.user_name(),  # jmeno2
        "birthdate": fake.date_of_birth().strftime('%Y-%m-%d')  # data
    }
 
# Endpoint pro generování dat uživatele
@app.route('/', methods=['GET'])
def generate_single_user():
    user = generate_user()
    ordered_user = {
        "name": user["name"],
        "last_name": user["last_name"],
        "address": user["address"],
        "email": user["email"],
        "username": user["username"],
        "birthdate": user["birthdate"]
    }
    # Vrácení JSON ve správném pořadí
    response = json.dumps(ordered_user, indent=2, ensure_ascii=False)  # format JSON
    return Response(response, content_type="application/json")
 

# Spuštění programu
if __name__ == '__main__':
    app.run(debug=True)