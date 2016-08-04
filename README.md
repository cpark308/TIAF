# TIAF
Texas Instruments Acronym Finder

This is the code for TIAF. There are two parts to this file

Alexa Voice Service

There are three files for AVS: intent_schema.txt, sample_utterances.txt, and subentry.txt.
intent_schema.txt and sample_utterances.txt can be copy pasted onto the AVS.
subentry.txt is a Custom Slot Types, with type "subentry" and values as texts inside the file.

AWS Lambda Function

Zip TIAF.py and acronyms file, and upload it to the Lambda function.
