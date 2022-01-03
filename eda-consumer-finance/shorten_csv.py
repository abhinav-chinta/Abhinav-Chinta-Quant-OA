import csv
import random

chances_selected = 0.05
file = open("/Users/abhinav_chinta/Code/Abhinav-Chinta-Quant-OA/eda-consumer-finance/consumer_complaints.csv")
result = open("/Users/abhinav_chinta/Code/Abhinav-Chinta-Quant-OA/eda-consumer-finance/consumer_complaints_short.csv", "w+")
writer = csv.writer(result)
rdr = csv.reader(file)
header = ['date_received','product','sub_product','issue','sub_issue','consumer_complaint_narrative','company_public_response','company','state','zipcode','tags','consumer_consent_provided','submitted_via','date_sent_to_company','company_response_to_consumer','timely_response','consumer_disputed?','complaint_id']
writer.writerow(header)
for line in rdr:
   if random.random() < chances_selected:
       writer.writerow(line)
        
file.close()
result.close()