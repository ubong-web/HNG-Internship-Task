TECHNICAL ARCHITECTURAL DRAWING
![Technical Architecture](NumberclassificationAPI.drawio.png)

# Number Classification API Documentation
## Project Overview
This project provides a serverless solution for classifying numbers and fetching interesting facts about them using AWS Lambda, API Gateway, and the Numbers API.

## Key Features:
1. Number Classification: Identifies properties of numbers, such as whether they are prime, perfect, or Armstrong.
2. Fun Fact Retrieval: Fetches fascinating facts about user-inputted numbers from the Numbers API.
3. Serverless Architecture: Utilizes AWS Lambda and API Gateway for scalable backend operations.
3. User-Friendly Frontend: A simple web interface where users can input a number and instantly receive results.    

## How It Works:
1. The user enters a number in the frontend application.
2. A request is sent via API Gateway to trigger the Lambda function.
3. The Lambda function processes the request by:
Analyzing the number's properties (e.g., prime, perfect, or Armstrong).
4. Fetching a fun fact from the Numbers API.
5. The response is displayed on the user interface, including the number properties and fun fact.

## Project Structure:
1. lambda.py: The main Lambda function script that handles number classification and external API integration.
2. Frontend: Simple HTML and JavaScript-based interface for user interaction.
3. AWS API Gateway: Manages API requests and routes them to the Lambda function.