from mailjet_rest import Client


def send_email(to, subject, content):
    api_key = "7e6dcfaee8923071842870ec32b05a34"
    api_secret = "a707b24f61914286e2cd162e367ca506"
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "oumaimahaimar2000@gmail.com",
                    "Name": "Oumaima HAIMAR"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": to
                    }
                ],
                "Subject": subject,
                "TextPart": content,
            }
        ]
    }

    result = mailjet.send.create(data=data)
