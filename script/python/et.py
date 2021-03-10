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
    update = 'UPDATE ESITDMS_COPY.dbo.Referral SET '
    update += f"ChildFirstName = '{faker.first_name()}', "
    update += f"ChildLastName = '{faker.last_name()}', "
    update += f"ChildBirthDate = '{faker.date_of_birth()}', "
    update += f"PrimaryContactFirstName = '{faker.first_name()}', "
    update += f"PrimaryContactLastName = '{faker.last_name()}', "
    update += f"ReferrerFirstName = '{faker.first_name()}', "
    update += f"ReferrerLastNamee = '{faker.last_name()}', "
    update += f"WHERE ReferralId = {row.referralId}"
    # child_first_name = faker.first_name()
    # child_last_name = faker.last_name()
    # print(f"UPDATE ESITDMS_COPY.dbo.Referral SET ChildFirstName = '{faker.first_name()}' SET ChildLastName = '{faker.last_name()}' SET ChildBirthDate = '{faker.date_of_birth()}' WHERE ReferralId = {row.referralId}")
    print(update)