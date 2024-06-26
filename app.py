import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

# Dictionary containing activities and their corresponding information
activities = {
    '1': 'Join The Community',
    '2': 'Want to Know more about LRI?',
    '3': 'NWN Scholarship Program',
}

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body', '').strip().lower()  # Ensure message is stripped and lowercased
    print("Debug - Incoming Message:", incoming_message)  # Debug print

    response = MessagingResponse()

    if incoming_message:
        if 'hello' == incoming_message:  # Check explicitly for 'hello'
            response.message("Hello! How may I assist you today?\n" + "\n".join([f"{key}. {value}" for key, value in activities.items()]))
        elif incoming_message in activities:
            if incoming_message == '1':
                response.message("Here is the link: https://navigatingwithnoel.com/onboarding/")
            else:
                response.message(activities[incoming_message])
        else:
            # Updated part: Include the list of activities with the error message
            activities_list = "\n".join([f"{key}. {value}" for key, value in activities.items()])
            response.message(f"Sorry, I didn't understand that. Please select an option from the list.\n{activities_list}")
    else:
        response.message("Please send a message.")

    return str(response)


if __name__ == "__main__":
    app.run()
