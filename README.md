# Cloud Computing Lab 5: AWS RDS & NoSQL

## Assignment 1: AWS RDS (PostgreSQL) Integration
* **Database:** PostgreSQL on AWS RDS (`us-east-1`, `db.t3.micro`).
* **Security:** RDS inbound rules restricted to the EC2 Security Group.
* **Application:** Wagtail Admin connected to RDS, successfully performing Create, Read, Update, and Delete (CRUD).

## Assignment 2: AWS NoSQL (DynamoDB) Integration
* **Database:** DynamoDB table (`StudentProfiles`) in `us-east-1`.
* **Security:** EC2 instance connects securely using an IAM Role.
* **Data Types Used:** String, Number, Boolean, List, Map.
* **Application:** Python Boto3 script (`dynamo_crud.py`) executing CRUD operations.
