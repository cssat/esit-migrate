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
    with open('sql/Child.sql', 'a') as file:
        file.write(update)
        file.write('\n')

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
    with open('sql/ChildAddressHistory.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ChildAgencyHistory

cursor.execute('SELECT ChildAgencyHistoryId FROM [ESITDMS_COPY].[dbo].[ChildAgencyHistory]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildAgencyHistory SET '
    update += f"CountyTypeId = '{random.randint(1, 39)}' "
    update += f"WHERE ChildAgencyHistoryId = {row.ChildAgencyHistoryId}"
    # print(update)
    with open('sql/ChildAgencyHistory.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ChildDocument

cursor.execute('SELECT ChildDocumentId FROM [ESITDMS_COPY].[dbo].[ChildDocument]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildDocument SET '
    update += f"Name = '{faker.first_name()}', "
    update += f"Description = 'asdf' "
    update += f"WHERE ChildDocumentId = {row.ChildDocumentId}"
    # print(update)
    with open('sql/ChildDocument.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ChildDocumentViewRequest

cursor.execute('SELECT ChildDocumentViewRequestId FROM [ESITDMS_COPY].[dbo].[ChildDocumentViewRequest]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ChildDocumentViewRequest SET '
    update += f"Name = '{faker.first_name()}' "
    update += f"WHERE ChildDocumentViewRequestId = {row.ChildDocumentViewRequestId}"
    # print(update)
    with open('sql/ChildDocumentViewRequest.sql', 'a') as file:
        file.write(update)
        file.write('\n')

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
    update += f"WaiveFamilyConcernsFlag = 0, "
    update += f"FamilyConcernsSummaryText = NULL, "
    update += f"FamilyConcernsPriorityText = NULL, "
    update += f"FamilyStrengthsText = NULL, "
    update += f"FamilyAdditionalConcernsText = NULL "
    update += f"WHERE ChildInformationId = {row.ChildInformationId}"
    # print(update)
    with open('sql/ChildInformation.sql', 'a') as file:
        file.write(update)
        file.write('\n')

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
    with open('sql/ChildNameHistory.sql', 'a') as file:
        file.write(update)
        file.write('\n')

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
    with open('sql/ChildOutcome.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ContactPerson

cursor.execute('SELECT ContactPersonId FROM [ESITDMS_COPY].[dbo].[ContactPerson]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ContactPerson SET '
    update += f"FirstName = '{faker.first_name()}', "
    update += f"LastName = '{faker.last_name()}' "
    update += f"WHERE ContactPersonId = {row.ContactPersonId}"
    # print(update)
    with open('sql/ContactPerson.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# COSFOutcome

cursor.execute('SELECT COSFOutcomeId FROM [ESITDMS_COPY].[dbo].[COSFOutcome]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.COSFOutcome SET '
    update += f"COSFOutcomeDescriptorConcernsDescription = NULL, "
    update += f"COSFOutcomeDescriptorText = NULL, "
    update += f"ResultsSummaryText = NULL "
    update += f"WHERE COSFOutcomeId = {row.COSFOutcomeId}"
    # print(update)
    with open('sql/COSFOutcome.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# COSFOutcomeSupportingEvidence

cursor.execute('SELECT COSFOutcomeSupportingEvidenceId FROM [ESITDMS_COPY].[dbo].[COSFOutcomeSupportingEvidence]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.COSFOutcomeSupportingEvidence SET '
    update += f"SupportingEvidenceSourceTypeOtherName = NULL, "
    update += f"ResultsSummaryText = NULL "
    update += f"WHERE COSFOutcomeSupportingEvidenceId = {row.COSFOutcomeSupportingEvidenceId}"
    # print(update)
    with open('sql/COSFOutcomeSupportingEvidence.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# Eligibility

cursor.execute('SELECT EligibilityId FROM [ESITDMS_COPY].[dbo].[Eligibility]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Eligibility SET '
    update += f"InformedClinicalOpinionText = NULL, "
    update += f"DecisionDate = NULL "
    update += f"WHERE EligibilityId = {row.EligibilityId}"
    # print(update)
    with open('sql/Eligibility.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ESITService

cursor.execute('SELECT ESITServiceId FROM [ESITDMS_COPY].[dbo].[ESITService]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ESITService SET '
    update += f"ServiceSettingTypeOtherName = NULL, "
    update += f"NonNaturalEnvironmentExplanationText = NULL, "
    update += f"MoveToNaturalEnvironmentPlanText = NULL, "
    update += f"ConsensusDiscussionText = NULL, "
    update += f"DeclinedNotesText = NULL, "
    update += f"LateOrNotStartedReasonText = NULL, "
    update += f"MethodDescription = 'asdf' "
    update += f"WHERE ESITServiceId = {row.ESITServiceId}"
    # print(update)
    with open('sql/ESITService.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ESITStaffPerson

cursor.execute('SELECT ESITStaffPersonId FROM [ESITDMS_COPY].[dbo].[ESITStaffPerson]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ESITStaffPerson SET '
    update += f"FirstName = '{faker.first_name()}', "
    update += f"LastName = '{faker.last_name()}' "
    update += f"WHERE ESITStaffPersonId = {row.ESITStaffPersonId}"
    # print(update)
    with open('sql/ESITStaffPerson.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# EvaluationDomain

cursor.execute('SELECT EvaluationDomainId FROM [ESITDMS_COPY].[dbo].[EvaluationDomain]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.EvaluationDomain SET '
    update += f"PresentDevelopmentLevelText = NULL, "
    update += f"RecommendationText = NULL "
    update += f"WHERE EvaluationDomainId = {row.EvaluationDomainId}"
    # print(update)
    with open('sql/EvaluationDomain.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# FunctionalDomainTestResult

cursor.execute('SELECT FunctionalDomainTestResultId FROM [ESITDMS_COPY].[dbo].[FunctionalDomainTestResult]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.FunctionalDomainTestResult SET '
    update += f"PresentDevelopmentLevelText = NULL, "
    update += f"DevelopmentAgeMonths = NULL "
    update += f"WHERE FunctionalDomainTestResultId = {row.FunctionalDomainTestResultId}"
    # print(update)
    with open('sql/FunctionalDomainTestResult.sql', 'w') as file:
        file.write(update)
        file.write('\n')

# FunctionalTestResult

cursor.execute('SELECT FunctionalTestResultId FROM [ESITDMS_COPY].[dbo].[FunctionalTestResult]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.FunctionalTestResult SET '
    update += f"AdministeredByName = 'asdf', "
    update += f"LocationCompletedName = 'asdf', "
    update += f"ResultsSummaryText = 'asdf' "
    update += f"WHERE FunctionalTestResultId = {row.FunctionalTestResultId}"
    # print(update)
    with open('sql/FunctionalTestResult.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# IFSP

cursor.execute('SELECT IFSPId FROM [ESITDMS_COPY].[dbo].[IFSP]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.IFSP SET '
    update += f"InterimIFSPReasonText = 'asdf', "
    update += f"OverdueReasonText = 'asdf', "
    update += f"OtherCurrentServiceNotesText = 'asdf' "
    update += f"WHERE IFSPId = {row.IFSPId}"
    # print(update)
    with open('sql/IFSP.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# IFSPOtherCurrentService

cursor.execute('SELECT IFSPOtherCurrentServiceId FROM [ESITDMS_COPY].[dbo].[IFSPOtherCurrentService]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.IFSPOtherCurrentService SET '
    update += f"NonESITServiceTypeOtherList = NULL "
    update += f"WHERE IFSPOtherCurrentServiceId = {row.IFSPOtherCurrentServiceId}"
    # print(update)
    with open('sql/IFSPOtherCurrentService.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# IFSPOtherDesiredService

cursor.execute('SELECT IFSPOtherDesiredServiceId FROM [ESITDMS_COPY].[dbo].[IFSPOtherDesiredService]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.IFSPOtherDesiredService SET '
    update += f"ProviderName = 'asdf', "
    update += f"StrategyText = 'asdf' "
    update += f"WHERE IFSPOtherDesiredServiceId = {row.IFSPOtherDesiredServiceId}"
    # print(update)
    with open('sql/IFSPOtherDesiredService.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# InboxMessage

cursor.execute('SELECT InboxMessageId FROM [ESITDMS_COPY].[dbo].[InboxMessage]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.InboxMessage SET '
    update += f"SubjectDescription = 'asdf', "
    update += f"MessageText = 'asdf', "
    update += f"SentDatetime = GETDATE(), "
    update += f"CreatedDateTime = GETDATE() "
    update += f"WHERE InboxMessageId = {row.InboxMessageId}"
    # print(update)
    with open('sql/InboxMessage.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# Notification

cursor.execute('SELECT NotificationId FROM [ESITDMS_COPY].[dbo].[Notification]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Notification SET '
    update += f"MessageText = 'asdf', "
    update += f"PostedDateTime = GETDATE(), "
    update += f"LastUpdatedDateTime = GETDATE() "
    update += f"WHERE NotificationId = {row.NotificationId}"
    # print(update)
    with open('sql/Notification.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ProgressNote

cursor.execute('SELECT ProgressNoteId FROM [ESITDMS_COPY].[dbo].[ProgressNote]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ProgressNote SET '
    update += f"SubjectDescription = 'asdf', "
    update += f"NotesText = 'asdf' "
    update += f"WHERE ProgressNoteId = {row.ProgressNoteId}"
    # print(update)
    with open('sql/ProgressNote.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# ResourceCoordinationOutcome

cursor.execute('SELECT ResourceCoordinationOutcomeId FROM [ESITDMS_COPY].[dbo].[ResourceCoordinationOutcome]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.ResourceCoordinationOutcome SET '
    update += f"Name = 'asdf', "
    update += f"Description = 'asdf', "
    update += f"StrategiesText = 'asdf' "
    update += f"WHERE ResourceCoordinationOutcomeId = {row.ResourceCoordinationOutcomeId}"
    # print(update)
    with open('sql/ResourceCoordinationOutcome.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# SchoolDistrict

cursor.execute('SELECT SchoolDistrictId FROM [ESITDMS_COPY].[dbo].[SchoolDistrict]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.SchoolDistrict SET '
    update += f"Name = '{faker.city()}' "
    update += f"WHERE SchoolDistrictId = {row.SchoolDistrictId}"
    # print(update)
    with open('sql/SchoolDistrict.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# TableUpdateLog

print("TRUNCATE TABLE TableUpdateLog;")

# TransferChild

cursor.execute('SELECT TransferChildId FROM [ESITDMS_COPY].[dbo].[TransferChild]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.TransferChild SET '
    update += f"TransferReasonText = 'asdf' "
    update += f"WHERE TransferChildId = {row.TransferChildId}"
    # print(update)
    with open('sql/TransferChild.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# TransitionPlan

print("TRUNCATE TABLE TransitionPlan;")

# TransitionPlanActivity

print("TRUNCATE TABLE TransitionPlanActivity;")

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
    update += f"ReferrerLastName = '{faker.last_name()}', "
    update += f"ReferralClosureReasonOtherName = null "
    update += f"WHERE ReferralId = {row.referralId}"
    # print(update)
    with open('sql/Referral.sql', 'a') as file:
        file.write(update)
        file.write('\n')

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
    with open('sql/Address.sql', 'a') as file:
        file.write(update)
        file.write('\n')

# Email

cursor.execute('SELECT EmailId FROM [ESITDMS_COPY].[dbo].[Email]')

for row in cursor:
    update = 'UPDATE ESITDMS_COPY.dbo.Email SET '
    update += f"EmailAddress = '{faker.email()}' "
    update += f"WHERE EmailId = {row.EmailId}"
    # print(update)
    with open('sql/Email.sql', 'a') as file:
        file.write(update)
        file.write('\n')
