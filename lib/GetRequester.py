import requests
import json

class GetRequester:
    """
    A class for retrieving data from a remote URL and converting
    JSON response data into Python objects.
    """

    def __init__(self, url):
        """
        Initialize a GetRequester instance with a URL.

        Args:
            url (str): The URL of the remote API endpoint.
        """
        self.url = url

    def get_response_body(self):
        """
        Send a GET request to the stored URL and return the response body.

        Returns:
            bytes: The raw response content returned by the endpoint.
        """
        # Send a GET request to the provided API endpoint
        response = requests.get(self.url)
        # Return the raw response body
        return response.content

    def load_json(self):
        """
        Retrieve the response body and convert the JSON data
        into a Python object.

        Returns:
            list: The parsed JSON data returned by the endpoint.
        """
        # Retrieve the raw response data from the endpoint
        data = self.get_response_body()

        # Convert the JSON response into Python data
        json_data = json.loads(data)

        return json_data