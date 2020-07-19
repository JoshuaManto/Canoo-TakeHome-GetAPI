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

    query = "SELECT error_number, time_stamp FROM Logs ORDER BY time_stamp DESC LIMIT 10"

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
