import json
import pymysql
import os

#Configuration Values

endpoint = os.environ['HOST']
username = os.environ['USER']
password = os.environ['PASS']
database_name = os.environ['DBNAME']

#Connection To Database
try:
    connection = pymysql.connect(endpoint, user=username, passwd=password, db=database_name)
    print('****connected to db****')
except:
    print('Error in connecting to db')

# GET REQUEST
def getTenMostRecent(event, context):

    # SQL Query to get the 10 most recent error logs
    # Since the timestamp is UNIX timestamp, the higher the value the more recent it is
    # So the 10 highest values are the most recent logs
    query = "SELECT error_number, time_stamp FROM Logs ORDER BY time_stamp DESC LIMIT 10"

    # Query execution
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()


    # Build the result variable
    # array of objects
    # Error code and timestamp only  
    result = []
    for row in rows:
        data = {}
        data['error_code'] = row[0]
        data['timestamp'] = row[1]
        # print("{0} {1}".format(row[0], row[1]))
        result.append(data)

    # Response body
    body = {
        "result": result
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


# For Local Running and Testing
# if __name__ == '__main__':
#     endpoint = os.environ['HOST']
#     print(endpoint)
