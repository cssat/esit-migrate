import pyodbc 
from faker import Faker

faker = Faker()

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=delolydb12021;'
                      'DATABASE=ESITDMS_COPY;'
                      'UID=;'
                      'PWD=')

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
    print(f"UPDATE ESITDMS_COPY.dbo.Referral SET ChildFirstName='{faker.first_name()}' WHERE ReferralId={row.referralId}")