# add_20_examples.py

import pandas as pd

# Load the existing dataset
df = pd.read_csv("data/cleaned_data.csv")

# New examples
new_rows = [
    {"Date": "2023-07-01", "Title": "Gender Rights Judgment", "Category": "Judgment",
     "Document_Text": "The court ruled in favor of equal rights for all genders.",
     "Cleaned_Text": "thecourtruledinfavorofequalrightsforallgenders"},

    {"Date": "2022-05-10", "Title": "Data Protection Policy Update", "Category": "Policy",
     "Document_Text": "An update to the data protection act was released today.",
     "Cleaned_Text": "anupdatetothedataprotectionactwasreleasedtoday"},

    {"Date": "2021-12-05", "Title": "Social Media Guidelines", "Category": "Policy",
     "Document_Text": "New guidelines for social media platforms were introduced.",
     "Cleaned_Text": "newguidelinesforsocialmediaplatformswereintroduced"},

    {"Date": "2023-01-18", "Title": "Digital ID Ruling", "Category": "Judgment",
     "Document_Text": "The court ruled digital IDs must comply with privacy standards.",
     "Cleaned_Text": "thecourtruleddigitalidsmustcomplywithprivacystandards"},

    {"Date": "2022-08-09", "Title": "AI Governance Framework", "Category": "Policy",
     "Document_Text": "A framework for AI governance has been published.",
     "Cleaned_Text": "aframeworkforaigovernancehasbeenpublished"},

    {"Date": "2022-03-20", "Title": "Right to Education Expansion", "Category": "Judgment",
     "Document_Text": "The court extended the right to education for marginalized children.",
     "Cleaned_Text": "thecourtextendedtherighttoeducationformarginalizedchildren"},

    {"Date": "2023-04-02", "Title": "Blockchain Adoption Policy", "Category": "Policy",
     "Document_Text": "The government released its official blockchain adoption roadmap.",
     "Cleaned_Text": "thegovernmentreleaseditsofficialblockchainadoptionroadmap"},

    {"Date": "2021-10-10", "Title": "Environmental Protection Order", "Category": "Judgment",
     "Document_Text": "The Supreme Court passed orders to protect river basins.",
     "Cleaned_Text": "thesupremecourtpassedorderstoprotectriverbasins"},

    {"Date": "2022-06-12", "Title": "Freedom of Speech Policy", "Category": "Policy",
     "Document_Text": "A new policy guarantees broader freedom of speech protections.",
     "Cleaned_Text": "anewpolicyguaranteesbroaderfreedomofspeechprotections"},

    {"Date": "2023-03-03", "Title": "Workplace Harassment Law Update", "Category": "Judgment",
     "Document_Text": "The court updated legal definitions of workplace harassment.",
     "Cleaned_Text": "thecourtupdatedlegaldefinitionsofworkplaceharassment"},

    {"Date": "2022-11-15", "Title": "Digital Health Data Policy", "Category": "Policy",
     "Document_Text": "Digital health data sharing is now regulated under a new policy.",
     "Cleaned_Text": "digitalhealthdatasharingisnowregulatedunderanewpolicy"},

    {"Date": "2023-05-25", "Title": "Free Speech Case Dismissal", "Category": "Judgment",
     "Document_Text": "The High Court dismissed the free speech limitation case.",
     "Cleaned_Text": "thehighcourtdismissedthefreespeechlimitationcase"},

    {"Date": "2021-09-17", "Title": "Social Media Surveillance Policy", "Category": "Policy",
     "Document_Text": "Surveillance of social media must follow new legal procedures.",
     "Cleaned_Text": "surveillanceofsocialmediamustfollownewlegalprocedures"},

    {"Date": "2023-02-10", "Title": "Labor Rights Ruling", "Category": "Judgment",
     "Document_Text": "The court recognized digital gig workers' rights under labor laws.",
     "Cleaned_Text": "thecourtrecognizeddigitalgigworkersrightsunderlaborlaws"},

    {"Date": "2022-01-06", "Title": "Remote Work Policy Guidelines", "Category": "Policy",
     "Document_Text": "Companies must now follow new guidelines for remote work.",
     "Cleaned_Text": "companiesmustnowfollownewguidelinesforremotework"},

    {"Date": "2022-12-24", "Title": "Medical Data Sharing Judgment", "Category": "Judgment",
     "Document_Text": "Court ruled hospitals must anonymize data before sharing.",
     "Cleaned_Text": "courtruledhospitalsmustanonymizedatabeforesharing"},

    {"Date": "2023-06-01", "Title": "Crypto Taxation Policy", "Category": "Policy",
     "Document_Text": "Cryptocurrency earnings will be taxed under new policy.",
     "Cleaned_Text": "cryptocurrencyearningswillbetaxedundernewpolicy"},

    {"Date": "2021-08-30", "Title": "Biometric Surveillance Ban", "Category": "Judgment",
     "Document_Text": "The court banned mass biometric surveillance in public spaces.",
     "Cleaned_Text": "thecourtbannedmassbiometricsurveillanceinpublicspaces"},

    {"Date": "2023-07-10", "Title": "Digital Voting Policy", "Category": "Policy",
     "Document_Text": "The election commission introduced a secure digital voting system.",
     "Cleaned_Text": "theelectioncommissionintroducedasecuredigitalvotingsystem"},

    {"Date": "2022-04-15", "Title": "AI Bias Case Judgment", "Category": "Judgment",
     "Document_Text": "The court ruled against biased AI systems used in hiring.",
     "Cleaned_Text": "thecourtruledagainstbiasedaisystemsusedinhiring"},
]

# Append and save
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ 20 new examples added successfully!")
print("📁 Total rows in cleaned_data.csv after update:", len(df))

