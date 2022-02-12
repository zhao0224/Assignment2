class Model:
    '''
      Record Class documents all columns' name that want to display from the dataset as part of the source code
      It also has getter and setter methods for call in future.
      Class objects support two kinds of operations: attribute references and instantiation
      Reference:  https://docs.python.org/3/tutorial/classes.html
    '''

    def __init__(self, incident_number, incident_type, reported_date,
                 nearest_populated_centre, province, company, substance, significant,
                 what_happened_category):
        '''
        constructor for Record, if call Record, user must pass all parameters in
        :param incident_number: column A
        :param incident_type: column B
        :param reported_date: column C
        :param nearest_populated_centre: column D
        :param province: column E
        :param company: column F
        :param substance: column K
        :param significant: column M
        :param what_happened_category: column R
        '''
        self.A = incident_number
        self.B = incident_type
        self.C = reported_date
        self.D = nearest_populated_centre
        self.E = province
        self.F = company
        self.K = substance
        self.M = significant
        self.R = what_happened_category


    def get_incident_number(self):
        '''
        This method to get incident number
        :return: incident number
        '''
        return self.A

    def set_incident_number(self, value):
        '''
        This method to set incident number
        :param value: the value to set
        :return: set the value to incident number
        '''
        self.A = value

    def get_incident_type(self):
        '''
        This method to get incident type
        :return: the incident type
        '''
        return self.B

    def set_incident_type(self, value):
        '''
        This method to set incident type
        :param value: the value to set
        :return: set the value to incident type
        '''
        self.B = value

    def get_reported_date(self):
        '''
        This method to get reported date
        :return: the reported date's value
        '''
        return self.C

    def set_reported_date(self, value):
        '''
        This method to set reported date
        :param value: the value to set
        :return: the new value to reported date
        '''
        self.C = value

    def get_nearest_populated_centre(self):
        '''
        This method to get value of the nearest populated centre
        :return: the value of the nearest populated centre
        '''
        return self.D


    def set_nearest_populated_centre(self, value):
        '''
        This method to set the nearest populated centre
        :param value: the value to set
        :return: new value store in the nearest populated centre
        '''
        self.D = value

    def get_province(self):
        '''
        This method to get value of province
        :return: the value
        '''
        return self.E

    def set_province(self, value):
        '''
        This method to set province value
        :param value: the value to set
        :return: new value to province
        '''
        self.E = value

    def get_company(self):
        '''
        This method to get the value of company
        :return: the value
        '''
        return self.F

        # set value for company
    def set_company(self, value):
        '''
        This method to set compnay value
        :param value: the value to set
        :return: new value to company
        '''
        self.F = value

       # get substance attribute
    def get_substance(self):
        '''
        This method to get the value of substance
        :return: substance value
        '''
        return self.K

    def set_substance(self, value):
        '''
        This method to set substance
        :param value: the value to set
        :return: the new value to substance
        '''
        self.K = value

    def get_significant(self):
        '''
        This method to get significant
        :return: the value of significant
        '''
        return self.M

    def set_significant(self, value):
        '''
        This method to set significant
        :param value: the value to set
        :return: the new value to significant
        '''
        self.M = value

    def get_what_happened_category(self):
        '''
        This method to get value of what happened category
        :return: the value of what happened category
        '''
        return self.R

        # set value for what_happened_category
    def set_what_happened_category(self, value):
        '''
        This method to set a value to what happened category
        :param value: the value to set
        :return: the new value of what happened category
        '''
        self.R = value

        # create a list which collect all used columns attribute)
    def toString(self):
        '''
        This method is a list which stores all values by getter for each columns
        :return: a list of values
        '''
        return Model.get_incident_number(self) + "," + Model.get_incident_type(self) + "," + Model.get_reported_date(self) \
               + "," + Model.get_nearest_populated_centre(self) + "," + Model.get_province(self) + "," + Model.get_company(self) \
               +"," + Model.get_substance(self) + "," + Model.get_significant(self) + "," + Model.get_what_happened_category(self)


    def toList(self):
        list=[]
        list.append(Model.get_incident_number(self))
        list.append(Model.get_incident_type(self))
        list.append(Model.get_reported_date(self))
        list.append(Model.get_nearest_populated_centre(self))
        list.append(Model.get_province(self))
        list.append(Model.get_company(self))
        list.append(Model.get_substance(self))
        list.append(Model.get_significant(self))
        list.append(Model.get_what_happened_category(self))
        return list
