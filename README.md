# TIAF
Texas Instruments Acronym Finder

for instructions, refer to https://e2e.ti.com/group/launchyourdesign/m/intern2016/666636

This is the code for TIAF. There are two parts to this file

Alexa Voice Service

There are three files for AVS: intent_schema.txt, sample_utterances.txt, and subentry.txt.
Contents of intent_schema.txt and sample_utterances.txt is used to fill in parts of Interaction Model indicated by the name of the file.
Make a Custom Slot Types named "subentry", and fill in values using contents of subentry.txt.

AWS Lambda Function

Compress TIAF.py and "acronyms" file, and upload it to the Lambda function.
