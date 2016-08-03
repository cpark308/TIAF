"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import re

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "searchOne":
        return search_one(intent, session)
    elif intent_name == "searchTwo":
        return search_two(intent, session)
    elif intent_name == "searchThree":
        return search_three(intent, session)
    elif intent_name == "searchFour":
        return search_four(intent, session)
    elif intent_name == "searchFive":
        return search_five(intent, session)
    elif intent_name == "searchSix":
        return search_six(intent, session)
    elif intent_name == "searchSeven":
        return search_seven(intent, session)
    elif intent_name == "searchEight":
        return search_eight(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Texas Instruments Acronym Finder. " \
                    "Please tell me your acronym by saying, " \
                    "What does ADC stand for?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your acronym by saying, " \
                    "What does ADC stand for?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Texas Instruments Acronym Finder." \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def search_one(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_two(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_three(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_four(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])
    subentry.append(intent['slots']['subentryFour']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_five(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])
    subentry.append(intent['slots']['subentryFour']['value'])
    subentry.append(intent['slots']['subentryFive']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_six(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])
    subentry.append(intent['slots']['subentryFour']['value'])
    subentry.append(intent['slots']['subentryFive']['value'])
    subentry.append(intent['slots']['subentrySix']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_seven(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])
    subentry.append(intent['slots']['subentryFour']['value'])
    subentry.append(intent['slots']['subentryFive']['value'])
    subentry.append(intent['slots']['subentrySix']['value'])
    subentry.append(intent['slots']['subentrySeven']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def search_eight(intent, session):
    card_title = intent['name']
    session_attributes = {}
    should_end_session = False
    reprompt_text = None

    subentry = []
    subentry.append(intent['slots']['subentryOne']['value'])
    subentry.append(intent['slots']['subentryTwo']['value'])
    subentry.append(intent['slots']['subentryThree']['value'])
    subentry.append(intent['slots']['subentryFour']['value'])
    subentry.append(intent['slots']['subentryFive']['value'])
    subentry.append(intent['slots']['subentrySix']['value'])
    subentry.append(intent['slots']['subentrySeven']['value'])
    subentry.append(intent['slots']['subentryEight']['value'])

    searchWord = get_searchWord(subentry)
    sayWord = get_sayWord(searchWord)
    definition = get_acronym(searchWord)

    if definition:
        speech_output = sayWord + " means " + definition + "."
    else:
        speech_output = sayWord + " could not be found."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_searchWord(subentry):
    searchWord = ""

    for i in range (0, len(subentry)):
        if subentry[i] == 'and':
            searchWord += '&'
        elif subentry[i][0].isalpha():
            searchWord += subentry[i][0].upper()
        elif subentry[i][0].digit():
            searchWord += subentry[i][0]

    return searchWord

def get_sayWord(searchWord):
    sayWord = ""

    for i in range (0, len(searchWord)):
        if searchWord[i].isalpha():
            sayWord += searchWord[i] + "."
        elif seachWord[i] == "&":
            sayWord += " and "
        elif searchWord[i].isdigit():
            sayWord += " " + searchWord[i] + " "

    return sayWord

def get_acronym(searchWord):
    if searchWord[0].isdigit():
        fileName = "acronyms/#.txt"
    else:
        fileName = "acronyms/" + searchWord[0].lower() + ".txt"
    f = open(fileName)
    line = f.readline()
    found = 0
    definition = ""
    while line and (found == 0):
        line = line.strip()
        lineArray = re.split(",", line)
        acronym = lineArray[0]
        if acronym == searchWord:
            found = 1
            for i in range (1, len(lineArray)):
                if i == 1:
                    definition += lineArray[i]
                else:
                    definition += ", or, " + lineArray[i]

        line = f.readline()
    f.close()
    return definition

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
