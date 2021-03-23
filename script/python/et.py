from faker import Faker
import connection

faker = Faker()

conn = connection.get_connection('ESIT_COPY')

cursor = conn.cursor()
cursor.execute('SELECT [ReferralId] AS referralId FROM [ESITDMS_COPY].[dbo].[Referral]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Referral SET '
    update += f"ChildFirstName = '{faker.first_name()}', "
    update += f"ChildLastName = '{faker.last_name()}', "
    update += f"ChildBirthDate = '{faker.date_of_birth()}', "
    update += f"PrimaryContactFirstName = '{faker.first_name()}', "
    update += f"PrimaryContactLastName = '{faker.last_name()}', "
    update += f"ReferrerFirstName = '{faker.first_name()}', "
    update += f"ReferrerLastNamee = '{faker.last_name()}', "
    update += f"ReferralClosureReasonOtherName = null "
    update += f"WHERE ReferralId = {row.referralId}"
    # print(update)

cursor.execute('SELECT AddressId FROM [ESITDMS_COPY].[dbo].[Address]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Address SET '
    update += f"AddressLine1 = '{faker.street_address()}', "
    update += f"CityName = '{faker.city()}', "
    update += f"ZipCode = '{faker.zipcode_in_state('WA')}' "
    #### update -- sanitize lat/lon? -- currently all values are null in our copy database
    update += f"WHERE AddressId = {row.AddressId}"
    # print(update)

cursor.execute('SELECT EmailId FROM [ESITDMS_COPY].[dbo].[Email]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Email SET '
    update += f"EmailAddress = '{faker.email()}' "
    update += f"WHERE EmailId = {row.EmailId}"
    print(update)
