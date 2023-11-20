from twilio.rest import Client
import geocoder

def send_sos(phone_number):
    account_sid = "AC593f4bf7c0e2c2c0e22afee18cad033e"
    auth_token = "0b6978517d0ecd40a0d3b2b978403885"
    client = Client(account_sid, auth_token)

    # Get current location
    g = geocoder.ip('me')
    if g.latlng is not None:
        latitude, longitude = g.latlng
        location_info = f"Latitude: {latitude}, Longitude: {longitude}"
    else:
        location_info = "Location information not available."

    # Send SOS message with location
    message = client.messages.create(
        body=f"SOS! Help needed! {location_info}",
        from_="+19712165202",
        to=phone_number
    )

    if message.sid:
        print("SOS message sent successfully.")
    else:
        print("Failed to send SOS message.")

    # Make a call with SOS message
    call = client.calls.create(
        twiml=f'<Response><Say>SOS! Help needed! {location_info}</Say></Response>',
        from_='+19712165202',
        to=phone_number
    )

    if call.sid:
        print("SOS call initiated successfully.")
    else:
        print("Failed to initiate SOS call.")

def rescue():
    print("Rescue mission initiated.")
