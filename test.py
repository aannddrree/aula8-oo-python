from views import Carro, Motor
import pymongo
import jsons

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbcarros"]
mycol = mydb["carro"]
mycolMotor = mydb["motor"]

motor = Motor("2","1.0")
#carro = Carro("Palio", "Fiat", motor)
id_return_code = mycolMotor.insert_one(jsons.dump(motor))

#id_return_code = mycol.insert_one(carro.__dict__)

print("Registro inserido: " + str(id_return_code))
