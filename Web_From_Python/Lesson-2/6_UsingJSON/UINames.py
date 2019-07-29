#!/usr/bin/env python3
#
# Client for the UINames.com service.
#
# 1. Decode the JSON data returned by the UINames.com API.
# 2. Print the fields in the specified format.
#
# Example output:
# My name is Tyler Hudson and the PIN on my card is 4840.

import requests


def SampleRecord():
    r = requests.get("http://uinames.com/api?ext&region=United%20States",
                     timeout=2.0)
    # 1. Add a line of code here to decode JSON from the response.
    json_data = r.json()
    print("json_data:", json_data)

    last_name = json_data['surname']
    first_name = json_data['name']
    pin = json_data['credit_card']['pin']
    print("***Information Decoded Successfully***")
    print("first name:", first_name)
    print("last name:", last_name)
    print("Phone number:", pin)


    return "My name is {} {} and the PIN on my card is {}.".format(
        # 2. Add the correct fields from the JSON data structure.
        json_data['surname'],
        json_data['name'],
        json_data['credit_card']['pin']
        )

if __name__ == '__main__':
    SampleRecord()
