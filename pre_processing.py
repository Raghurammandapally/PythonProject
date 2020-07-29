import pandas as pd
df = pd.read_csv('Contacts.csv')
contact = df[['contact_id','first_name','middle_name','last_name']]
contact.columns = ['Contact_id','Fname','Mname','Lname']
contact_table_csv = contact.to_csv('contact_table.csv',index=None,header=True)

home_address = df[['contact_id','home_address','home_state','home_zip']]
home_address.columns = ['Contact_id','Address','State','Zip']
home_address.insert(1,'Address_type','Home')

work_address = df[['contact_id','work_address','work_state','work_zip']]
work_address.columns = ['Contact_id','Address','State','Zip']
work_address.insert(1,'Address_type','Work')

address = pd.concat([home_address,work_address], axis=0)

address.reset_index(inplace=True,drop=True)
address.index +=1
address.insert(0,'Address_id',address.index)

address_table_csv = address.to_csv('address_table.csv',index=None,header=True)

home_phone = df[['contact_id','home_zip','cell_phone']]
home_phone.columns = ['Contact_id','Area_code','Number']
home_phone.insert(2,'Phone_type','Home')

work_phone = df[['contact_id','work_zip','work_phone']]
work_phone.columns = ['Contact_id','Area_code','Number']
work_phone.insert(2,'Phone_type','Work')

phone = pd.concat([home_phone,work_phone], axis=0)
phone.reset_index(inplace=True,drop=True)
phone.index += 1
phone.insert(0,'Phone_id',phone.index)
phone_table_csv = phone.to_csv('phone_table.csv',index=None,header=True)

date = df[['contact_id','birth_date']]
date.columns = ['Contact_id','Date']
date.insert(1,'Date_type','Birth')
date.reset_index(inplace=True,drop=True)
date.index += 1
date.insert(0,'Date_id',date.index)
date_table_csv = date.to_csv('date_table.csv',index=None,header=True)
