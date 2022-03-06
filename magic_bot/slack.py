import os

from slack_sdk import WebClient


class SlackAPI:
    def __init__(self):
        self.client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
