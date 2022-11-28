from app import app
from flask import Flask, request
import africastalking
import os, requests, json
from config import *

africastalking.initialize(USSD_username, USSD_api_key)
sms = africastalking.SMS

# idlinterns.onrender.com
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    string = text.split("*")
    

    # service_code = '*384*2760*267*0076888271*2*1#'
    # text = "267*0076888271*2*1"
    # string = text.split("*")
    # string = ["267", "0076888271", "2", "1"]


    #ussd logic
    if text == "":
        #main menu
        response = "CON Please Enter amount.\n"
    elif len(string)==1: #   *384*2760*267#
        #sub menu 1
        # amount = int(string[0])
        amount = int(float(string[0]))
        if not amount > 0:
            response = f"END Amount NGN {string[0]} is invalid"
        else:
            response = "CON Please Enter Account number.\n"
    elif len(string)==2: #   *384*2760*267*0076888271#
        #sub menu 2
        account = string[1]
        if len(string[1])!=10 or len(''.join(i for i in string[1] if i.isdigit())) != 10:
            response = "END Account number must be 10 digits"
        else:
            url = f"{SAFEPAY_URI}/api/v1/likelybanks/{string[1]}"
            r = requests.get(url)
            resp = r.json()
            if resp["status"]:
                banklist = resp["data"][1]
                response = f"CON {banklist} .\n"
            else:
                message = resp.get("message")
                response = f"END {message} .\n"
    elif len(string)==3: #   *384*2760*267*0076888271*2#
        #sub menu 3
        url = f"{SAFEPAY_URI}/api/v1/likelybanks/{string[1]}"
        r = requests.get(url)
        resp = r.json()
        if not resp["status"]:
            message = resp.get("message")
            response = f"END {message} .\n"
        elif int(float(string[2])) < 1 or int(float(string[2])) > len(resp["data"][0]): #string[2] range from 1 to max displayed banks
            message = "Sorry, Invalid bank selection."
            response = f"END {message} .\n"
        else:
            bankcode = resp["data"][0][string[2]]
            url = f"{SAFEPAY_URI}/api/v1/verifyaccount/{string[1]}/{bankcode}"
            print(f"url: {url}")
            r = requests.get(url)
            resp = r.json()
            if resp["status"]:
                bank_name = resp["data"]["bank_name"]
                account_name = resp["data"]["account_name"]
                # response = f"CON Enter 1 to confirm the transfer of NGN {string[0]} to AcctNo:{string[1]}, {bank_name}"
                response = f"CON Enter 1 to confirm the transfer of NGN {string[0]} to {account_name}, AcctNo:{string[1]}, {bank_name}"
            else:
                message = resp.get("message")
                response = f"END {message} .\n"

    elif len(string)==4: #   *384*2760*<267>*<0076888271>*<2>*1#
        #sub menu 4
        if string[3] != "1":
            message = "Transaction not confirmed. \nThank you for your time."
            response = f"END {message} .\n"
        else:
            message = "Transaction processing.... \nDeveloped by Emeka, Samson & Frank."
            response = f"END {message} .\n"

    else:
        message = "Sorry, Invalid input. Try again."
        response = f"END {message} .\n"

    return response

