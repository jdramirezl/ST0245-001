class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def compare_dates(self, other_date):
        if self.year < other_date.year or self.year == other_date.year and self.month < other_date.month or self.year == other_date.year and self.month == other_date.month and self.day < other_date.day:
            print("La fecha actual es antes que la comparada")
        elif self.year > other_date.year or self.year == other_date.year and self.month > other_date.month or self.year == other_date.year and self.month == other_date.month and self.day > other_date.day:
            print("La fecha comparada es antes que la actual")
        else:
            print("Las fechas son iguales")

    def __str__(self):
        return ("Date: "+str(self.day)+"/"+str(self.month)+"/"+str(self.year))
