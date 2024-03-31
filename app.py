# bot.py
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Dictionary containing activities and their corresponding information
activities = {
    '1': 'Join The Community ',
    '2': 'Want to Know more about LRI',
    '3': 'NWN Scholarship Program',
}

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body', '').strip().upper()
    response = MessagingResponse()

    if incoming_message:
        if incoming_message.startswith('HELLO'):
            sender_name = request.form.get('From', '').split(':')[1]
            # Respond with list of activities
            activities_list = "\n".join([f"{key}. {value}" for key, value in activities.items()])
            response.message(f"Hello {sender_name}.\nHow may I assist you today?\n{activities_list}")
        elif incoming_message in activities.keys():
            # Check if the selected activity is option 1
            if incoming_message == '1':
                response.message("Here is the link: https://navigatingwithnoel.com/onboarding/")
            else:
                # Respond with information about the selected activity
                response.message(activities[incoming_message])
        else:
            response.message("Sorry, I didn't understand that. Please select an option from the list.")
    else:
        response.message("Please send a message.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
