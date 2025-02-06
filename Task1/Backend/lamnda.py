import json
import math
import requests

def lambda_handler(event, context):
    try:
        # Extract the number from the query string parameters
        number = int(event['queryStringParameters']['number'])
        
        # Determine if the number is prime
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        # Determine if the number is perfect
        def is_perfect(n):
            return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

        # Determine if the number is an Armstrong number
        def is_armstrong(n):
            digits = [int(d) for d in str(n)]
            power = len(digits)
            return sum(d ** power for d in digits) == n

        # Fetch fun fact from Numbers API
        fun_fact_api_url = f"http://numbersapi.com/{number}"
        fun_fact_response = requests.get(fun_fact_api_url)
        fun_fact = fun_fact_response.text if fun_fact_response.ok else "No fun fact available."

        # Compute properties
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        # Build the response
        response_body = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(response_body)
        }

    except (ValueError, KeyError):
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({"error": True, "message": "Invalid number input."})
        }
