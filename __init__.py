from mycroft import MycroftSkill, intent_file_handler


class IceCreamShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    # »»»»»»»»»»»»»»»  Logging info
    def initialize(self):
        self.log.info("the skill has loaded huzza!")
        self.log.warning("Something is slightly off")
        self.log.error("Oh noes! Something is broken")
        try:
            print(new_var)
        except NameError:
            self.log.exception("the code broke!")


    @intent_file_handler('shop.cream.ice.intent')
    def handle_shop_cream_ice(self, message):
        flavour = message.data.get('flavour')

        self.speak_dialog('shop.cream.ice', data={
            'flavour': flavour
        })


def create_skill():
    return IceCreamShop()
    
    
"""
»»»» 


"""

