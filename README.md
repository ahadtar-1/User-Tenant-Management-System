User Tenant Management System

In this project a backend service was created in a microservices environment. The service had two entities: User and Tenant. Two separate API groups for both entities were created using FastAPI which comprised of several types of functionalities such as GET, POST, DELETE, and PATCH. A Kafka Consumer consumes the user/tenant data which is created by the service from a Kafka topic, parses the data, and inserts into the appropriate database table. A postgres database is used to interact with the service via Object Relational Mapping. 

Technologies used: Python - Docker - Postgres - Kafka - FastAPI - SQLAlchemy
