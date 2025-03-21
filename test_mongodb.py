import unittest  # Import the unittest framework
from unittest.mock import patch  # Import patch to mock objects
import mongomock  # Import mongomock to simulate MongoDB
from bson.objectid import ObjectId  # Import ObjectId for MongoDB IDs

# Import the MongoDB class from your module
from mongodb import MongoDB  

class TestMongoDBOperations(unittest.TestCase):
    """
    Unit test class for MongoDB operations using mongomock.
    """

    @patch('pymongo.MongoClient', new=mongomock.MongoClient)  
    def setUp(self):
        """Set up a mock MongoDB client for each test."""
        self.db = MongoDB()  # Use the mocked MongoDB instance

    def test_create(self):
        """Test the create operation."""
        data = {"name": "Alice", "age": 30}
        inserted_id = self.db.create(data)  # Insert the document
        self.assertIsInstance(inserted_id, ObjectId)  # Check if it returns an ObjectId
    
    def test_read(self):
        """Test the read operation."""
        data = {"name": "Bob", "age": 25}
        self.db.create(data)  # Insert the document
        result = self.db.read({"name": "Bob"})  # Query the document
        self.assertEqual(len(result), 1)  # Ensure exactly 1 document is returned
        self.assertEqual(result[0]["name"], "Bob")  # Ensure data matches
    
    def test_update(self):
        """Test the update operation."""
        data = {"name": "Charlie", "age": 40}
        inserted_id = self.db.create(data)  # Insert the document
        result = self.db.update({"name": "Charlie"}, {"age": 45})  # Update 'age'
        self.assertEqual(result, 1)  # 1 document should be updated
        
        # Verify the update
        updated_data = self.db.read({"name": "Charlie"})
        self.assertEqual(updated_data[0]["age"], 45)  # Ensure age is updated
    
    def test_delete(self):
        """Test the delete operation."""
        data = {"name": "Dave", "age": 50}
        inserted_id = self.db.create(data)  # Insert the document
        result = self.db.delete({"name": "Dave"})  # Delete document
        self.assertEqual(result, 1)  # 1 document should be deleted
        
        # Verify the document is deleted
        deleted_data = self.db.read({"name": "Dave"})
        self.assertEqual(len(deleted_data), 0)  # Ensure no data is returned

# Run the tests
if __name__ == '__main__':
    unittest.main()
