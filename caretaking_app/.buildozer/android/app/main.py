from kivy.app import App
from kivy.properties import StringProperty
from sqlalchemy.exc import SQLAlchemyError
from sys import stderr

# noinspection PyUnresolvedReferences
from login_screen import LoginScreen
# noinspection PyUnresolvedReferences
from input_screen import ObservationEntry
# noinspection PyUnresolvedReferences
from create_account import CreateAccount
# noinspection PyUnresolvedReferences
from caretaking_review_screen import ReviewScreen


class CareTakingApp(App):
    location = StringProperty('location type')
    activity = StringProperty('activity')
    appetite = StringProperty('appetite')
    date = StringProperty('date')
    city = StringProperty('city')
    weight = StringProperty('weight')
    temp = StringProperty('temperature')
    patient = StringProperty('Select the patient visited')
    error = StringProperty('')
    patient_id = StringProperty('')
    birth = StringProperty('')
    account_surname = StringProperty('')
    account_given_name = StringProperty('')
    account_patient_id = StringProperty('')

    def load(self):
        self.load_kv('caretaking.kv')



    def create_log(self):
        self.patient_id = self.root.ids.patient_spinner.text
        self.location = self.root.ids.location_type_spinner.text
        self.activity = self.root.ids.physical_activity.text
        self.appetite = self.root.ids.appetite.text
        self.error = self.root.ids.submit.text
        self.birth = self.root.ids.birthdate.text
        self.city = self.root.ids.address.text
        self.temp = self.root.ids.temp.text
        self.weight = self.root.ids.weight.text
        self.missing_field = 'You are missing one or many fields'

        if self.patient_id == 'Select the patient visited':
            self.app.error = self.missing_field
        if self.location == 'Select the location type of visit':
            self.app.error = self.missing_field
        if self.activity == "Select value of Patient\'s physical activity":
            self.app.error == self.missing_field
        if self.appetite == "Select value of Patient\'s appetite level":
            self.app.error == self.missing_field
        if self.birth == '':
            self.app.error == self.missing_field
        if self.city == '':
            self.app.error == self.missing_field
        if self.temp == '':
            self.app.error == self.missing_field
        if self.weight == '':
            self.app.error == self.missing_field
        else:
            self.app.error == 'Log Completed'
            self.root.transition.direction = 'left'
            self.root.current = 'review'

    def login_in(self):
        self.root.transition.direction = 'left'
        self.root.current = 'observation'

    def create_account(self):
        self.root.transition.direction = 'left'
        self.root.current = 'create account'
        self.account_surname = self.root.ids.create_account.ids.surname.text
        self.account_given_name = self.root.ids.create_account.ids.given_name.text
        self.account_patient_id = self.root.ids.create_account.ids.patient_id.text


    def back_to_login(self):
        self.root.transition.direction = 'left'
        self.root.current = 'login'


if __name__ == '__main__':
    try:
        app = CareTakingApp()
        app.run()
    except SQLAlchemyError as exception:
        print('Initial database connection failed!', file=stderr)
        print('Cause: {exception}'.format(exception=exception), file=stderr)
        exit(1)
