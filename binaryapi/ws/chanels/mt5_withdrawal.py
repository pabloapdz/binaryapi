"""Module for Binary mt5_withdrawal websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#mt5_withdrawal

class Mt5Withdrawal(Base):
    """Class for Binary mt5_withdrawal websocket chanel."""

    name = "mt5_withdrawal"

    def __call__(self, amount, from_mt5: str, to_binary: str, passthrough=None, req_id: int = None):
        """Method to send message to mt5_withdrawal websocket chanel.
        MT5: Withdrawal (request)
        This call allows withdrawal from MT5 account to Binary account.
        :param amount: Amount to withdraw (in the currency of the MT5 account); min = $1 or an equivalent amount, max = $20000 or an equivalent amount.
        :type amount: 
        :param from_mt5: MT5 account login to withdraw money from
        :type from_mt5: str
        :param to_binary: Binary account loginid to transfer money to
        :type to_binary: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "mt5_withdrawal": 1,
            "amount": amount,
            "from_mt5": from_mt5,
            "to_binary": to_binary
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
