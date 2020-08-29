# Sunset Alert Script
This script pulls the current sunset forecast image from https://sunsetwx.com/sunset/sunset_et.png , analyzes it, and sends a text to your phone via Twilio.
## Setup
After setting up your Twilio account, add your SID and Auth token in the appropriate places in the code, and update the to and from phone numbers with what you registered on your account.

You will also need to adjust the cropped size/location of the image to match your geography of interest.

Also, I hosted this code on Google Cloud Platform as a Cloud Function, scheduled to run everyday around 3:00. If you decide to use this code in GCP, you will need to upload the `requirements.txt` as well.
