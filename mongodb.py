
from pymongo import MongoClient
from bson.objectid import ObjectId
import numpy as np
class MongoDB:
    def __init__(self, db_name="test_db", collection_name="test_collection"):
    
        self.client = MongoClient("mongodb://localhost:27017")  # Connect to MongoDB
        self.db = self.client[db_name]  # Select the database
        self.collection = self.db[collection_name]  # Select the collection

    def create(self, data):
        """Insert a document into the collection"""
        result = self.collection.insert_one(data)  # Insert the document
        return result.inserted_id  # Return the inserted document ID

    def read(self, query={}):
        """Read documents from the collection"""
        return list(self.collection.find(query))  # Return matching documents as a list

    def update(self, query, new_values):
        """Update a document in the collection"""
        result = self.collection.update_one(query, {"$set": new_values})  # Update document
        return result.modified_count  # Return number of updated documents

    def delete(self, query):
        """Delete a document from the collection"""
        result = self.collection.delete_one(query)  # Delete document
        return result.deleted_count  # Return number of deleted documents
