from model import Base, Restaurant

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def Add_Restaurant(name, location, foods):
	restaurant_object = Restaurant(Name=name,Location=location,Foods=foods)
	session.add(restaurant_object)
	session.commit()
	

def Delete_Restaurant(name):
	restaurant_object = session.query(
		Restaurant).filter_by(
		Name=name).delete()
	session.commit()

def Edit_Restaurant(name, location, food):
	restaurant_object = session.query(
		Restaurant).filter_by(
		Name=name)
	restaurant_object.name = name
	restaurant_object.location = location
	restaurant_object.food = food
	session.commit()

def Get_Restaurant(name):
	restaurant_object = session.query(
		Restaurant).filter_by(
		Name=name)
	return restaurant_objects

def Get_All_Restaurants():
	restaurants = session.query(
		Restaurant).all()
	return restaurants


# Add_Restaurant("Panorama Pizza", "Nazareth", "pizza")
# Add_Restaurant("Uri Buri", "Acre", "fish, shrimps, bread, vegetables, rice")
# Add_Restaurant("Restaurant 1910", "Degania Alef", "ice cream, pizza, fruits, cake, pasta, fish, rice, potato, vegetables, hummus")
# Add_Restaurant("Decks Restaurant", "Tiberias", "fries, steak, vegetables, bread, ice cream, fruits")
# Add_Restaurant("Miznon", "Tel Aviv-Yafo", "vegetables, falafel, bread, hummus, fruits, rice, meat")
# Add_Restaurant("Estalliano Dalla Costa", "Haifa", "fruits, cake, pizza, falafel, pasta, meat, potato, fish")
# Add_Restaurant("Y.M.C.A Nazareth", "Nazareth", "meat, potato, vegetables, hummus")
# Add_Restaurant("Tanureen", "Migdal", "fries, fish, bread, vegetables, chicken, cake, hummus, meat")
# Add_Restaurant("iShushi", "Nazareth Illit", "sushi")
# Add_Restaurant("Dolphin Yam", "Jerusalem", "shrimps, fish, vegetables, bread, chicken, meat, ice cream, pasta, potato, rice")

