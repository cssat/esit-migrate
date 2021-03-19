* should createdAt in the destination database be the migrate timestamp or a "timestamp" of the original referral creation date?
* Should organization IDs port over directly from the legacy db, or do we need to create a temporary map from old to new ids?
* As long as child details are sanitized, are we safe to leave things like start/end dates for cases and dates for events (like school history) intact, as well as things like mapped diagnoses descriptions?
* What to do about tables specific to existing esit functionality that may not be ported over exactly?  I.e., the task table or the transition tables?


