#include "Point2D.hpp"
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

class Line2D{
private:
    Point2D initial;
    Point2D final;
    Point2D difference;
    double slope;
    double b;

public:
    Line2D(Point2D initial, Point2D final)
    {
        //Puntos
        this->initial = initial;
        this->final = final;

        //Vector method calculations
        double norm = sqrt(pow(final.x - initial.x, 2) + pow(final.y - initial.y, 2));
        this->difference = Point2D((final.x - initial.x) / norm, (final.y - initial.y) / norm);

        // Line method calculations
        if (initial.x == final.x) this->slope = 0;
        else this->slope = (initial.y - final.y) / (initial.x - final.x);
        this->b = (initial.x * -1 * slope) + initial.y;
    }

    //Line equation method
    void get_formula(){
        string x = "- ";
        if (b >= 0)
            x = "+ ";
        cout << "y = " + to_string(this->slope) + "x " + x + to_string(this->b) << endl;
    }

    void generate_points(){
        //x iguales
        if (slope == 0)
        {
            cout << "Points: [ ";
            int miny = min(this->initial.y, this->final.y), maxy = max(this->initial.y, this->final.y);
            for (int i = miny; i <= maxy; i++)
            {
                cout << "(" + to_string(0) + "," + to_string(i) + ") ";
            }
            cout << "]" << endl;
        }
        else
        {
            //x distintas
            cout << "Points: [ ";
            for (int i = initial.x; i <= final.x; ++i)
            {
                double y = this->slope * i + this->b;
                cout << "(" + to_string(i) + "," + to_string(y) + ") ";
            }
            cout << "]" << endl;
        }
    }


    //Vector method
    double get_magnitude(int x, int y){
        return sqrt(pow(x, 2) + pow(y, 2));
    }

    void generate_vectors()
    {
        // while
        int i = 1;
        cout << "Points: [ ";
        double finalMagnitude = get_magnitude(this->final.x, this->final.y);
        while (get_magnitude(this->initial.x + (i * this->difference.x), this->initial.y + (i * this->difference.y)) < finalMagnitude)
        {
            cout << "(" + to_string(this->initial.x + (i * this->difference.x)) + "," + to_string(this->initial.y + (i * this->difference.y)) + ") ";
            i++;
        }
        cout << "]" << endl;
    }
};