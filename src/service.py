#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The code in this file has been obtained from Google Analytics API V3
# quickstart examples - which was licensed under the Apache License 2.0.

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service


def initialize_service(key_file_location):
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'

    # Authenticate and construct service.
    return get_service(api_name='analyticsreporting',
                       api_version='v4',
                       scopes=[scope],
                       key_file_location=key_file_location)
