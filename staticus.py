from requests import get

API_KEY = ""
MY_DOMAIN = "mailgun.net"
MY_STATUS_LIST = "status-updates@mailgun.net"
EVENTS_API_URL = "https://api.mailgun.net/v2/{}/events".format(MY_DOMAIN)


def main():
    response = get(EVENTS_API_URL,
                   auth=('api', API_KEY),
                   params={
                       "event": "stored"
                   })

    events = response.json()

    message_urls = [event['storage']['url'] for event in events['items']
                    if MY_STATUS_LIST in event['message']['recipients']]

    for url in message_urls:
        message = get(url,
                      auth=('api', API_KEY)).json()

        print "From: ", message['from']
        print '--------------------------- {} --------------------------------'.format(message['subject'])
        print message['body-plain']


if __name__ == "__main__":
    main()
