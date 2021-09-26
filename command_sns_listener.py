from sqs_listener import SqsListener

class CommandListener(SqsListener):
    def handle_message(self, body, attributes, messages_attributes):
        print(body)