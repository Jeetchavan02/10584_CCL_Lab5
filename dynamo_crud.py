import boto3

# Initialize DynamoDB resource for the Mumbai region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('StudentProfiles')

def perform_crud():
    # 1. CREATE (Inserting item with 5 different datatypes: String, Number, Boolean, List, Map)
    print("--- 1. CREATE ---")
    table.put_item(
        Item={
            'student_id': 'S101',                     # String (Partition Key)
            'name': 'Jeet Chavan',                    # String (S)
            'age': 19,                                # Number (N)
            'is_active': True,                        # Boolean (BOOL)
            'skills': ['Python', 'AWS', 'Django'],    # List (L)
            'address': {                              # Map (M)
                'city': 'Mumbai',
                'state': 'Maharashtra'
            }
        }
    )
    print("Item created successfully with 5+ datatypes!")

    # 2. READ (Fetching the item)
    print("\n--- 2. READ ---")
    response = table.get_item(Key={'student_id': 'S101'})
    print("Retrieved Item:", response.get('Item'))

    # 3. UPDATE (Modifying an attribute)
    print("\n--- 3. UPDATE ---")
    table.update_item(
        Key={'student_id': 'S101'},
        UpdateExpression="SET age = :val",
        ExpressionAttributeValues={':val': 20}
    )
    updated_response = table.get_item(Key={'student_id': 'S101'})
    print("Updated Item Age:", updated_response.get('Item').get('age'))

    # 4. DELETE (Removing the item)
    print("\n--- 4. DELETE ---")
    table.delete_item(Key={'student_id': 'S101'})
    print("Item deleted successfully!")

if __name__ == '__main__':
    perform_crud()
