"""Module for Binary authorize websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#authorize

class Authorize(Base):
    """Class for Binary authorize websocket chanel."""

    name = "authorize"

    def __call__(self, authorize: str, add_to_login_history: int = None, passthrough=None, req_id: int = None):
        """Method to send message to authorize websocket chanel.
        Authorize (request)
        Authorize current WebSocket session to act on behalf of the owner of a given token. Must precede requests that need to access client account, for example purchasing and selling contracts or viewing portfolio.
        :param authorize: Authentication token. May be retrieved from https://www.binary.com/en/user/security/api_tokenws.html
        :type authorize: str
        :param add_to_login_history: [Optional] Send this when you use api tokens for authorization and want to track activity using `login_history` call.
        :type add_to_login_history: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "authorize": authorize
        }

        if add_to_login_history:
            data['add_to_login_history'] = int(add_to_login_history)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
