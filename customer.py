from cryptography.fernet import Fernet
import json



class Customer:
    def __init__(self, ID: int, name: str, number: str = None, email: str = None, owed: float = 0.0, revenue: float = 0.0):
        if not isinstance(name, str):
            raise TypeError("Customer init failed -> name must be str")
        elif not isinstance(number, (type(None), str)):
            raise TypeError("Customer init failed -> number must be str")
        elif not isinstance(email, (type(None), str)):
            raise TypeError("Customer init failed -> email must be str")
        elif not isinstance(owed, float):
            raise TypeError("Customer init failed -> owed must be float")
        elif not isinstance(revenue, float):
            raise TypeError("Customer init failed -> revenue must be float")
        elif not isinstance(ID, int):
            raise TypeError("Customer init failed -> ID must be int")
        
        self.__ID = str(ID)

        key_data = self.read("key_data")

        key_data[self.__ID] = {
                
            "card": None,
            "number": None,
            "email": None
                
            }
        self.dump(key_data, "key_data") 


                   


        self.__name = name
        if not number == None:
            number = self.encrypt_data(number, "number")
        
        if not email == None:
            email = self.encrypt_data(email, "email")


        customer_data = self.read("customer_data")

        customer_data[self.__ID] = {
            "name": name,
            "card": None,
            "number": number,
            "email": email,
            "owed": owed,
            "revenue": revenue,
            "id": self.__ID
        }

        self.dump(customer_data, "customer_data")
    
    

    def encrypt_data(self, data: str, data_type: str) -> str:
        key_data = self.read("key_data")

        key = Fernet.generate_key()
        key_data[self.__ID][data_type] = key.decode()

        self.dump(key_data, "key_data")
        
        return Fernet(key).encrypt(data.encode()).decode()
        
    
    
    def add_card(self, card: str):
        customer_data = self.read("customer_data")
        customer_data[self.__ID]["card"] = self.encrypt_data(card, "card")
        self.dump(customer_data, "customer_data")
    
    
    def dump(self, data, location: str):
        if location.lower() == "customer_data":
            with open("customers.json", "w") as file:
                json.dump(data, file)
        elif location.lower() == "key_data":
            with open("keys.json", "w") as file:
                json.dump(data, file)
        else:
            raise ValueError(f'"customer_data" or "key_data" expected {location} given')

    def read(self, location: str) -> dict:
        if location.lower() == "customer_data":
            with open("customers.json", "r") as file:
                return json.load(file)
        elif location.lower() == "key_data":
            with open("keys.json", "r") as file:
                return json.load(file)
        else:
            raise ValueError(f'"customer_data" or "key_data" expected {location} given')

    

class Pull:
    def __init__(self):
        
        with open("customers.json", "r") as file:
            customers = json.load(file)
        
        self.customers_list = []
        for customer in customers:
            self.customers_list.append(customers[customer])

    def names(self) -> list:
        name_list = []
        for customer in self.customers_list:
            name_list.append(customer["name"])
        return name_list
    
    def phones(self) -> list:
        numbers_list = []
        for customer in self.customers_list:
            id = customer["id"]
            number = self.get("number", id)
            numbers_list.append(number)

        return numbers_list
    
    def emails(self) -> list:
        email_list = []
        for customer in self.customers_list:
            id = customer["id"]
            email = self.get("email", id)
            email_list.append(email)
        return email_list
    
    def cards(self) -> list:
        card_list = []
        for customer in self.customers_list:
            id = customer["id"]
            card = self.get("card", id)
            card_list.append(card)
        return card_list
    
    def customers(self):
        return self.customers_list
        
    def dump(self, data, location: str):
        if location.lower() == "customer_data":
            with open("customers.json", "w") as file:
                json.dump(data, file)
        elif location.lower() == "key_data":
            with open("keys.json", "w") as file:
                json.dump(data, file)
        else:
            raise ValueError(f'"customer_data" or "key_data" expected {location} given')

    def read(self, location: str) -> dict:
        if location.lower() == "customer_data":
            with open("customers.json", "r") as file:
                return json.load(file)
        elif location.lower() == "key_data":
            with open("keys.json", "r") as file:
                return json.load(file)
        else:
            raise ValueError(f'"customer_data" or "key_data" expected {location} given')
        
    def get(self, type: str, ID: str) -> str:
        key_data = self.read("key_data")
        customer_data = self.read("customer_data")
        card = customer_data[ID]["card"]
        number = customer_data[ID]["number"]
        email = customer_data[ID]["email"]
        
        key = key_data[ID][type]
        key = key.encode()
        if type.lower() == "card" and card != None:
            return Fernet(key).decrypt(card).decode()
        elif type.lower() == "number" and number != None:
            return Fernet(key).decrypt(number).decode()
        elif type.lower() == "email" and email != None:
            return Fernet(key).decrypt(email).decode()
        else:
            raise TypeError("Expected str, NoneType was given")
        
            