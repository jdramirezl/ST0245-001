#include <vector>
#include <cmath>

using namespace std;

class Point{
private:
    double polar_radius;
    double polar_angle;

public:
    double x;
    double y;

    Point() {}

    Point(double x, double y){
        this->x = x;
        this->y = y;
        this->polar_radius = sqrt(pow(this->x, 2) + pow(this->y, 2));

        if (x == 0 && y == 0)
            this->polar_angle = 0;
        else if (x == 0)
            this->polar_angle = y >= 0 ? 90 : 270;
        else if (y == 0)
            this->polar_angle = x >= 0 ? 0 : 180;
        else
            this->polar_angle = atan(this->y / this->x);
    }

    double get_polar_radius(){
        return this->polar_radius;
    }

    double get_polar_angle(){
        return this->polar_angle;
    }

    double euclidean_distance(Point *p2){
        return sqrt(pow(this->x - p2->x, 2) + pow(this->y - p2->y, 2));
    }
};

