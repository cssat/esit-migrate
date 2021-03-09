SELECT TOP 100 
	eo.[Name] AS assignedAgency,
	ref.[ChildId] AS id,
	ref.[ChildFirstName], --o
    ref.[ChildLastName], --o
    ref.[ChildBirthDate] AS childDateOfBirth, --o
    ref.[GenderTypeIdChild] AS sexOfChild,
	ref.[PrimaryContactFirstName], --o
    ref.[PrimaryContactLastName], --o
	ref.[ContactInformationIdPrimaryContact],
	prima.[AddressLine1] AS prim_address1, --o
	prima.[CityName] AS prim_city, --o
	NULL AS [prim_state],
	prima.[ZipCode] AS prim_zip, --o
	NULL AS ref_preferredContactMethod, -- NOT SURE WHERE TO FIND THIS
	prime.[EmailAddress] AS prim_email, --o
	ref.[ReferralId] AS referralId, 
	ref.[ReferrerFirstName], --o
	ref.[ReferrerLastName], --o
	NULL AS [role], -- NOT SURE WHERE TO FIND THIS
	NULL AS con_preferredContactMethod, -- NOT SURE WHERE TO FIND THIS
	refe.[EmailAddress] AS prim_email, --o
	ref.[ReceivedDate] AS dateOfInitialReferral, 
	ref.[ReferralSubmittedReasonTypeId] AS reason,
	NULL AS familyContactDate
FROM [ESITDMS].[dbo].[Referral] as ref
LEFT JOIN [ESITDMS].[dbo].[ESITOrganizationServiceAreaMap] AS eosam
	ON ref.[ESITOrganizationServiceAreaMapIdAssignedTo] = eosam.ESITOrganizationServiceAreaMapId
LEFT JOIN [ESITDMS].[dbo].[ESITOrganization] AS eo
	ON eosam.ESITOrganizationId = eo.ESITOrganizationId
LEFT JOIN [ESITDMS].[dbo].[Address] AS prima
	ON ref.[ContactInformationIdPrimaryContact] = prima.[ContactInformationId]
LEFT JOIN [ESITDMS].[dbo].[Email] AS prime
	ON ref.[ContactInformationIdPrimaryContact] = prime.[ContactInformationId]
LEFT JOIN [ESITDMS].[dbo].[Email] AS refe
	ON ref.[ContactInformationIdPrimaryContact] = refe.[ContactInformationId]
WHERE ref.[DeletedFlag] = 0 
	AND eosam.[DeletedFlag] = 0 
	AND eo.[DeletedFlag] = 0
	AND prima.[DeletedFlag] = 0
	AND prime.[DeletedFlag] = 0
	AND ref.[DeletedFlag] = 0
