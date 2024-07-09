#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
import models
from models.city import City 
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states' # Defines the table name in the database

    # Conditional attribute definition based on storage type
    if storage_type == 'db':
        # Define 'name' column, max length 128 characters, cannot be null
        name = Column(String(128), nullable=False)
        # State has many cities, each city has a back reference to state
        cities = relationship("City", backref="state")
    else:
        # If storage is not a database, set 'name' to an empty string
        name = ""

        @property
        def cities(self):
            """list of cities in this state"""
            city_list = [] # Initialize an empty list to store cities
            all_cities = models.storage.all(City) # Get all cities from the storage
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city) # Add city if it belongs to this state
            return city_list # Return the list of cities


if getenv('HBNB_TYPE_STORAGE') != 'db':
    @property
    def cities(self):
        """Getter method for cities"""
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
