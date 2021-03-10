import pyodbc 
from faker import Faker
import os
from dotenv import load_dotenv

load_dotenv()

faker = Faker()

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=delolydb12021;'
                      'DATABASE=ESITDMS_COPY;'
                      f"UID={os.getenv('DB_USER')};"
                      f"PWD={os.getenv('DB_PASSWORD')}")

cursor = conn.cursor()
cursor.execute('''SELECT TOP 100 
                    [ReferralId] AS referralId--,
	                --[ChildFirstName],
                    --[ChildLastName], 
                    --[ChildBirthDate] AS childDateOfBirth,
	                --[PrimaryContactFirstName],
                    --[PrimaryContactLastName], 
	                --[ReferrerFirstName],
	                --[ReferrerLastName]
                FROM [ESITDMS_COPY].[dbo].[Referral]''')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Referral SET '
    update += f"ChildFirstName = '{faker.first_name()}', "
    update += f"ChildLastName = '{faker.last_name()}', "
    update += f"ChildBirthDate = '{faker.date_of_birth()}', "
    update += f"PrimaryContactFirstName = '{faker.first_name()}', "
    update += f"PrimaryContactLastName = '{faker.last_name()}', "
    update += f"ReferrerFirstName = '{faker.first_name()}', "
    update += f"ReferrerLastNamee = '{faker.last_name()}' "
    update += f"WHERE ReferralId = {row.referralId}"
    # child_first_name = faker.first_name()
    # child_last_name = faker.last_name()
    # print(f"UPDATE ESITDMS_COPY.dbo.Referral SET ChildFirstName = '{faker.first_name()}' SET ChildLastName = '{faker.last_name()}' SET ChildBirthDate = '{faker.date_of_birth()}' WHERE ReferralId = {row.referralId}")
    # print(update)


cursor.execute('''SELECT TOP 100 
	                AddressId--,
	                --[AddressLine1] AS prim_address1, --o
	                --[CityName] AS prim_city, --o
	                --[StateTypeId] AS [prim_state], --o
	                --[ZipCode] AS prim_zip --o
                 FROM [ESITDMS_COPY].[dbo].[Address]''')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Address SET '
    update += f"AddressLine1 = '{faker.street_address()}', "
    update += f"CityName = '{faker.city()}', "
    update += f"ZipCode = '{faker.zipcode_in_state('WA')}' "
    update += f"WHERE AddressId = {row.AddressId}"
    # print(update)

cursor.execute('''SELECT TOP 100 EmailId--,
                    --EmailAddress
                FROM [ESITDMS_COPY].[dbo].[Email]''')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Email SET '
    update += f"EmailAddress = '{faker.email()}' "
    update += f"WHERE EmailId = {row.EmailId}"
    print(update)