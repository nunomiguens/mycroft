from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.format import join_list


class AnotherIceCream(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.toppings = ["sprinkles", "whipped cream", "nuts", "gummy bears", "chocolate chips"]


    def toppings_validator(self, response):
        #return response in self.toppings
        requested_toppings = []
        for topping in self.toppings:
            if topping in response:
                requested_toppings.append(topping)
        return requested_toppings
        # requested-toppings = [topping if topping in response for topping in self.toppings] 


    @intent_file_handler('request_icecream.intent')
    def handle_cream_ice_another(self, message):
        self.speak_dialog("welcome", data={'name':"stratus"
        })
        topping_response = self.get_response("toppings_request", 
                                             validator = self.toppings_validator, 
                                             on_fail = "topping_missing", num_retries = 2)
        self.log.info(topping_response)
        flavour = message.data.get('flavour')

        if topping_response is not None:
            requested_toppings = join_list(self.toppings_validator(topping_response), "and")                   
            self.speak_dialog('icecream_with_toppings', data={
            'flavour': flavour, 'toppings' : requested_toppings
            })
        else:
            self.speak_dialog('icecream_without_toppings', data={
            'flavour': flavour
            })



def create_skill():
    return AnotherIceCream()

