import requests, os
import xlrd  #pip install xlrd==1.2.0
from xlutils.copy import copy
from dotenv import load_dotenv
from config import API_KEY,SAFEPAY_URI

# load_dotenv()  # take environment variables from .env.
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



####################################### Functions #################################
def get_transaction():
    headers = {'content-type': 'application/json', 'x-access-token': API_KEY}
    url = f"{SAFEPAY_URI}/api/v1/safepay/querypayment/initiated"

    try:
        #Make API call
        r = requests.get(url=url, headers=headers)
        print(f"Status code: {r.status_code}")  #Print status code
        response = r.json()
    except Exception as e:
        return f"Encountered error: {e}"

    if not response.get("status"):
        return response.get("message")

    #Record needed to be saved in excel
    records = response.get("data")    #This record is a list dictionaries.
    print(f"first record: {records[0]}")

    FOLDER = '/home/megzy/Desktop/IDL_PROJECTS/IDL_Interns/app/static'
    filename = "transactions.xlsx"

    if filename in os.listdir(FOLDER):

        file=u'{}/{}'.format(FOLDER, filename)
        print(file)
        try:
            book = xlrd.open_workbook(file,encoding_override="cp1251")  
        except:
            book = xlrd.open_workbook(file)

        #xlutils is for updating the table later
        wb = copy(book)
        sheet1 = wb.get_sheet(0) #open sheet 1
        
        count = 0
        row = 0

        for element in records:
            print(element)
            count += 1
            print(count)
            row += 1
            initiating_date = element.get("initiating_date")
            paymentref = element.get("paymentref")
            merchant_id = element.get("merchant_id")
            business_name = element.get("business_name")
            product_amount = element.get("product_amount")
                
            sheet1.write(row,0,initiating_date)
            sheet1.write(row,1,paymentref)
            sheet1.write(row,2,merchant_id)
            sheet1.write(row,3,business_name)
            sheet1.write(row,4,product_amount)
            continue    #continue to For-loop

        #save the updated table
        wb.save(file)
        return "All data successfully recorded in spreadsheet."
    else:
        return "Excel file not in Folder"


#CALL THE get_transaction() FUNCTION
# get_transaction()