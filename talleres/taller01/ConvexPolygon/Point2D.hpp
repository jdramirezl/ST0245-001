#include <cmath>

using namespace std;

class Point2D{
private:
    double polar_radius;
    double polar_angle;
    double centroid_angle;
    double centroid_magnitud;

public:
    double x;
    double y;


    Point2D() {}

    Point2D(double x, double y){
        this->x = x;
        this->y = y;
        this->polar_radius = sqrt(pow(this->x, 2) + pow(this->y, 2));

        if (x == 0 && y == 0)
            this->polar_angle = 0;
        else if (x == 0)
            this->polar_angle = y >= 0 ? 90 : 270;
        else if (y == 0)
            this->polar_angle = x >= 0 ? 0 : 180;
        else {
            this->polar_angle = (atan(this->y / this->x)) * (180 / M_PI);
            int plane = get_plane();

            if(plane == 2 || plane == 3) this->polar_angle += 180;
            else if (plane == 4) this->polar_angle += 360;
        }
    }


    int get_plane(){
        if(x>0 && y > 0) return 1;
        else if(x<0 && y < 0) return 3;
        else if (x<0 && y > 0) return 2;
        return 4;
    }

    void set_cangle(double centroid_angle){
        this -> centroid_angle = centroid_angle;
    }

    void set_cmagnitud(double centroid_magnitud){
        this -> centroid_magnitud = centroid_magnitud;
    }

    double get_cAngle() const {
        return centroid_angle;
    }

    double get_cMagnitud() const {
        return centroid_magnitud;
    }

    double get_polar_radius(){
        return this->polar_radius;
    }

    double get_polar_angle(){
        return this->polar_angle;
    }

    double euclidean_distance(Point2D *p2){
        return sqrt(pow(this->x - p2->x, 2) + pow(this->y - p2->y, 2));
    }
};