# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/network-wired.svg" card_color="#22A7F0" width="50" height="50" style="vertical-align:bottom"/> Create services skill
Create various features for an e2e network slice

## About
A Mycroft Skill that helps create various features of an E2E network slice.

## Examples
Mycroft trigger `create.service.intent`:
* "Hey mycroft, create a service, please."

Get the name of the service `create.service.name.dialog`:
* "Please tell me the name of the service."

Get the machines that will have access to the service `create.service.access.dialog`:
* "Please tell me which machines will have access to the service."

Check if the service needs internet access `create.service.internet.dialog`:
* "Does the service need internet access?"

Define the performance of the service `create.service.performance.dialog`:
* "Please specify the performance of the service."

Output the results `final.response.dialog`:
* "Ok, here's what I got: the service {name} will provide access to the machines {access}, and {internet} internet access. Its performance will be {performance} Mbits/sec."

## Credits
Nuno Miguens

## Category
**Configuration**
Information



