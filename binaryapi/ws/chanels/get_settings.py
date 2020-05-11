"""Module for Binary get_settings websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#get_settings

class GetSettings(Base):
    """Class for Binary get_settings websocket chanel."""

    name = "get_settings"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to get_settings websocket chanel.
        Get Account Settings (request)
        Get User Settings (email, date of birth, address etc)
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "get_settings": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
