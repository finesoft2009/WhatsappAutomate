import pymysql

connection = pymysql.connect("182.72.62.130", "root", "root", "messages")
cursor = connection.cursor()

sql_query = "Select branch,sid,Recipient,body,whatsapp from messages where whatsapp='N'"

try:
    cursor.execute(sql_query)
    data = cursor.fetchall()

    for record in data:
        branch = record[0]
        sid = record[1]
        recipient = record[2]
        body = record[3]
        whatsapp = record[4]

    # print(data, end="\n")
    print("SID.No: %s ""\n" 
          "Branch: %s ""\n"
          "Recipient: %s ""\n"
          "Body: %s " % (sid, branch, recipient, body))

except Exception as e:
    print("Exception : ", e)

connection.close()


