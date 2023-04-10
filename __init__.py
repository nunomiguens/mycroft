from mycroft import MycroftSkill, intent_file_handler


class IceCreamShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shop.cream.ice.intent')
    def handle_shop_cream_ice(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('shop.cream.ice', data={
            'flavour': flavour
        })


def create_skill():
    return IceCreamShop()

