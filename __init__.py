from mycroft import MycroftSkill, intent_file_handler


class Createserviceskill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('create.service.intent')
    def handle_createserviceskill(self, message):
        # Step 1: Get the name of the service
        name_service = self.get_response('create.service.name')

        # Step 2: Get the machines that will have access to the service
        access_service = self.get_response('create.service.access')

        # Step 3: Check if the service needs internet access
        internet_service_resp = self.get_response('create.service.internet')
        internet_access = ""

        if internet_service_resp == 'yes':
            internet_access = 'will have'
        elif internet_service_resp == 'no':
            internet_access = 'will not have'
                
        # Step 4: Define the performance of the service
        performance_service = self.get_response('create.service.performance')

        # Step 5: Output the results
        self.speak_dialog('final.response', {'name': name_service, 'access':access_service, 'internet':internet_access,'performance':performance_service})



def create_skill():
    return Createserviceskill()

