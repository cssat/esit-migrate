from faker import Faker
import connection
import random

faker = Faker()

conn = connection.get_connection('ESIT_COPY')

cursor = conn.cursor()

# Child

cursor.execute('SELECT ChildId FROM [ESITDMS_COPY].[dbo].[Child]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Child SET '
    update += f"FirstName = '{faker.first_name()}', "
    update += f"MiddleName = '{faker.first_name()}', "
    update += f"LastName = '{faker.last_name()}', "
    update += f"BirthDate = '{faker.date_of_birth()}' "
    update += f"WHERE ChildId = {row.ChildId}"
    # print(update)

# ChildAddressHistory

cursor.execute('SELECT ChildAddressHistoryId FROM [ESITDMS_COPY].[dbo].[ChildAddressHistory]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildAddressHistory SET '
    update += f"AddressLine1 = '{faker.street_address()}', "
    update += f"AddressLine2 = NULL, "
    update += f"AddressLine3 = NULL, "
    update += f"CityName = '{faker.city()}', "
    update += f"ZipCode = '{faker.zipcode_in_state('WA')}', "
    update += f"ZipAdd4Code = NULL "
    update += f"WHERE ChildAddressHistoryId = {row.ChildAddressHistoryId}"
    # print(update)

# ChildAgencyHistory

cursor.execute('SELECT ChildAgencyHistoryId FROM [ESITDMS_COPY].[dbo].[ChildAgencyHistory]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildAgencyHistory SET '
    update += f"CountyTypeId = `{random.randint(1, 39)}` "
    update += f"WHERE ChildAgencyHistoryId = {row.ChildAgencyHistoryId}"
    # print(update)

# ChildDocument

cursor.execute('SELECT ChildDocumentId FROM [ESITDMS_COPY].[dbo].[ChildDocument]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildDocument SET '
    update += f"Name = '{faker.first_name()}', "
    update += f"Description = 'asdf' "
    update += f"WHERE ChildDocumentId = {row.ChildDocumentId}"
    # print(update)

# ChildDocumentViewRequest

cursor.execute('SELECT ChildDocumentViewRequestId FROM [ESITDMS_COPY].[dbo].[ChildDocumentViewRequest]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildDocumentViewRequest SET '
    update += f"Name = '{faker.first_name()}' "
    update += f"WHERE ChildDocumentViewRequestId = {row.ChildDocumentViewRequestId}"
    # print(update)

# ChildInformation

cursor.execute('SELECT ChildInformationId FROM [ESITDMS_COPY].[dbo].[ChildInformation]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildInformation SET '
    update += f"PreviousServicesReceivedText = NULL, "
    update += f"ChildHealthSummaryText = NULL, "
    update += f"AdditionalChildHealthInformationText = NULL, "
    update += f"AllergyList = NULL, "
    update += f"MedicationList = NULL, "
    update += f"MedicalAlertList = NULL, "
    update += f"ChildActivityLocationPersonText = NULL, "
    update += f"ChildActivityChildEnjoysText = NULL, "
    update += f"ChildActivityFamilyEnjoysText = NULL, "
    update += f"ChildActivityGoingWellText = NULL, "
    update += f"ChildActivityDifficultText = NULL, "
    update += f"ChildActivityFamilyDoesNotDoText = NULL, "
    update += f"WaiveFamilyConcernsFlag = NULL, "
    update += f"FamilyConcernsSummaryText = NULL, "
    update += f"FamilyConcernsPriorityText = NULL, "
    update += f"FamilyStrengthsText = NULL, "
    update += f"FamilyAdditionalConcernsText = NULL "
    update += f"WHERE ChildInformationId = {row.ChildInformationId}"
    # print(update)

# ChildNameHIstory

cursor.execute('SELECT ChildNameHistoryId FROM [ESITDMS_COPY].[dbo].[ChildNameHistory]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildNameHistory SET '
    update += f"FirstName = '{faker.first_name()}', "
    update += f"MiddleName = '{faker.first_name()}', "
    update += f"LastName = '{faker.last_name()}', "
    update += f"BirthDate = '{faker.date_of_birth()}' "
    update += f"WHERE ChildNameHistoryId = {row.ChildNameHistoryId}"
    # print(update)

# ChildOutcome

cursor.execute('SELECT ChildOutcomeId FROM [ESITDMS_COPY].[dbo].[ChildOutcome]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildOutcome SET '
    update += f"Description = 'asdf', "
    update += f"CurrentStatusText = 'asdf', "
    update += f"SuccessCriteriaText = 'asdf', "
    update += f"StrategiesText = 'asdf' "
    update += f"WHERE ChildOutcomeId = {row.ChildOutcomeId}"
    # print(update)

# ContactPerson

cursor.execute('SELECT ContactPersonId FROM [ESITDMS_COPY].[dbo].[ContactPerson]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ContactPerson SET '
    update += f"FirstName = '{faker.first_name()}', "
    update += f"LastName = '{faker.last_name()}' "
    update += f"WHERE ContactPersonId = {row.ContactPersonId}"
    # print(update)

# COSFOutcome

cursor.execute('SELECT COSFOutcomeId FROM [ESITDMS_COPY].[dbo].[COSFOutcome]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.COSFOutcome SET '
    update += f"COSFOutcomeDescriptorConcernsDescription = NULL, "
    update += f"COSFOutcomeDescriptorText = NULL, "
    update += f"ResultsSummaryText = NULL "
    update += f"WHERE COSFOutcomeId = {row.COSFOutcomeId}"
    # print(update)

# COSFOutcomeSupportingEvidence

cursor.execute('SELECT COSFOutcomeSupportingEvidenceId FROM [ESITDMS_COPY].[dbo].[COSFOutcomeSupportingEvidence]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.COSFOutcomeSupportingEvidence SET '
    update += f"SupportingEvidenceSourceTypeOtherName = NULL, "
    update += f"ResultsSummaryText = NULL "
    update += f"WHERE COSFOutcomeSupportingEvidenceId = {row.COSFOutcomeSupportingEvidenceId}"
    # print(update)

# Referral

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

# Address

cursor.execute('SELECT AddressId FROM [ESITDMS_COPY].[dbo].[Address]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Address SET '
    update += f"AddressLine1 = '{faker.street_address()}', "
    update += f"CityName = '{faker.city()}', "
    update += f"ZipCode = '{faker.zipcode_in_state('WA')}' "
    #### update -- sanitize lat/lon? -- currently all values are null in our copy database
    update += f"WHERE AddressId = {row.AddressId}"
    # print(update)

# Email

cursor.execute('SELECT EmailId FROM [ESITDMS_COPY].[dbo].[Email]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Email SET '
    update += f"EmailAddress = '{faker.email()}' "
    update += f"WHERE EmailId = {row.EmailId}"
    # print(update)
