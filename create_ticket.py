# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    create_ticket.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yel-hadd <yel-hadd@mail.com>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/15 02:21:59 by yel-hadd          #+#    #+#              #
#    Updated: 2023/05/15 03:08:58 by yel-hadd         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import base64
import os

# Define the function to create a new Zendesk ticket
def create_zendesk_ticket(subdomain, email, password):
    # Define the URL to create a new ticket
    url = f"https://{subdomain}.zendesk.com/api/v2/tickets.json"

    # Define the JSON payload to create a new ticket
    payload = {
        "ticket": {
            "subject": "My printer is on fire!",
            "comment": {
                "body": "The smoke is very colorful."
            }
        }
    }

    # Define the headers for the HTTP request
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{email}:{password}'.encode()).decode(),
        'Content-Type': 'application/json'
    }

    # Send the HTTP request to create a new ticket
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code and print a success or error message
    if response.status_code == 201:
        print('Ticket created successfully.')
    else:
        print('Error creating ticket.')

# Get the email, password and subdomain from environment variables
email = os.environ.get('MAIL')
password = os.environ.get('PW')
subdomain = os.environ.get('SUBDOMAIN')

# Call the function to create a new Zendesk ticket
create_zendesk_ticket(subdomain, email, password)
