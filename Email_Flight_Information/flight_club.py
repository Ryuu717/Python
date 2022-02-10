import requests
POST_ENDPOINT = "https://api.sheety.co/cab8fcdc711d37084c15d04c7306dccd/flightDeals/users"


class FlightClub:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.email_val = None

    def join(self):
        print("Welcome to Dummy's flight club.\nWe find the best flight deals and email you. ")

        self.first_name = input("what is your first name? ")
        self.last_name = input("what is your last name? ")

        while True:
            self.email = input("what is your email addrass? ")
            self.email_val = input("please re-enter your email. ")
            if self.email == self.email_val:
                data = {
                    "user":{
                        "firstName": self.first_name,
                        "lastName": self.last_name,
                        "email": self.email,
                    }
                }

                response = requests.post(url=POST_ENDPOINT, json=data)
                print(response.text)
                print("Thank you! You are in the club ")
                break
            else:
                print("emails do not match, please re enter ")


flight_club = FlightClub()
flight_club.join()


# print("Welcome to Dummy's flight club.\nWe find the best flight deals and email you. ")
#
# first_name = input("what is your first name? ")
# last_name = input("what is your last name? ")
#
# while True:
#     email = input("what is your email addrass? ")
#     email_val = input("please re-enter your email. ")
#     if email == email_val:
#         data = {
#             "user":{
#                 "firstName": first_name,
#                 "lastName": last_name,
#                 "email": email,
#             }
#         }
#
#         response = requests.post(url=POST_ENDPOINT, json=data)
#         print(response.text)
#         print("Thank you! You are in the club ")
#         break
#     else:
#         print("emails do not match, please re enter ")