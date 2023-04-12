from mycroft import MycroftSkill, intent_file_handler


class AnotherIceCream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cream.ice.another.intent')
    def handle_cream_ice_another(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('cream.ice.another', data={
            'flavour': flavour
        })


def create_skill():
    return AnotherIceCream()

