from mycroft import MycroftSkill, intent_file_handler


class Createserviceskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('createserviceskill.intent')
    def handle_createserviceskill(self, message):
        self.speak_dialog('createserviceskill')


def create_skill():
    return Createserviceskill()

