#include <iostream>

using namespace std;

class Date
{
    int day;
    int month;
    int year;

public:
    Date(int day, int month, int year){
        this->day = day;
        this->month = month;
        this->year = year;
    }

    int get_day(){
        return this->day;
    }

    int get_month(){
        return this->month;
    }

    int get_year(){
        return this->year;
    }

    int compare_dates(Date *other){
        if (this->year < other->year or this->year == other->year and this->month < other->month or this->year == other->year and this->month == other->month and this->day < other->day){
            cout << "-1" << endl;
        }
        else if (this->year > other->year or this->year == other->year and this->month > other->month or this->year == other->year and this->month == other->month and this->day > other->day){
            cout << "0" << endl;
        }
        else{
            cout << "1" << endl;
        }
    }
};

std::ostream &operator<<(std::ostream &out, Date &date){
    return out << "Date: " + to_string(date.get_day()) + "/" + to_string(date.get_month()) + "/" + to_string(date.get_year()) << endl;
}

int main(){
    Date hoy(27, 1, 2021), ayer(26, 1, 2021);

    cout << hoy.get_day() << endl;
    hoy.compare_dates(&ayer);
    cout << hoy << endl;
}