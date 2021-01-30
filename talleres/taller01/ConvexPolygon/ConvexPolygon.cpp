#include "Line2D.hpp"

#include <cmath>
#include <vector>
#include <queue>
#include <iostream>
#include <string>

#define D(x) cout << #x << " " << x << endl;

using namespace std;


struct comparator{
    bool operator()(Point2D first, Point2D second){
        if(first.get_cAngle() == second.get_cAngle()){
            return first.get_cMagnitud() > second.get_cMagnitud();
        }
        return first.get_cAngle() > second.get_cAngle();
    }
};

class Polygon{
private:
    vector<Line2D> polygon_outlines;
    double centroid_x;
    double centroid_y;

public:
    int get_plane(double x, double y){
        if(x>0 && y > 0) return 1;
        else if(x<0 && y < 0) return 3;
        else if (x<0 && y > 0) return 2;
        return 4;
    }

    Polygon(vector<Point2D> &points){

        if(points.size() < 3){
            cout << "Not enough points for a polygon!" << endl;
        }
        else {

            //Priority Declaration
            priority_queue<Point2D, vector<Point2D>, comparator> pq, pq2;

            double x_sum = 0, y_sum = 0;
            for(int i = 0; i < points.size(); ++i){
                x_sum += points[i].x;
                y_sum += points[i].y;
            }

            this -> centroid_x = (x_sum)/points.size();
            this -> centroid_y = (y_sum)/points.size();

            D(centroid_x)
            D(centroid_y)

            double temp_x, temp_y;
            for(int i = 0; i < points.size(); ++i){
                temp_x = (points[i].x - this -> centroid_x);
                temp_y = (points[i].y - this -> centroid_y);
                points[i].set_cmagnitud(sqrt(pow(temp_x,2) + pow(temp_y ,2)));

                if (temp_x == 0 && temp_y == 0)
                    points[i].set_cangle(0);
                else if (temp_x == 0)
                    points[i].set_cangle(temp_y >= 0 ? 90 : 270);
                else if (temp_y == 0)
                    points[i].set_cangle(temp_x >= 0 ? 0 : 180);
                else {
                    points[i].set_cangle((atan(temp_y / temp_x)) * (180 / M_PI));
                    int plane = get_plane(temp_x, temp_y);

                    if(plane == 2 || plane == 3) points[i].set_cangle( points[i].get_cAngle() + 180);
                    else if (plane == 4) points[i].set_cangle( points[i].get_cAngle() + 360);
                }
            }


            //Priority Filling
            for(auto & point : points) pq.push(point);

            /*
            while(!pq2.empty()){
                pq.push(pq2.top());
                cout << "("<<pq2.top().x << "," << pq2.top().y << ") ";
                pq2.pop();
            }
            cout << endl;
             */

            //CREATING LINES
            Point2D first, prev, cur;
            first = pq.top();
            prev = first;

            while (pq.size() > 1) {
                pq.pop();
                cur = pq.top();
                cout << "From: " << prev.x << "," << prev.y << " to: " << cur.x << "," << cur.y << endl;
                this->polygon_outlines.push_back(getLine(prev, cur));
                prev = cur;
            }


            cout << "From: " << prev.x << "," << prev.y << " to: " << first.x << "," << first.y << endl;
            this->polygon_outlines.push_back(getLine(prev, first));

            for (int i = 0; i < this->polygon_outlines.size(); ++i) {
                polygon_outlines[i].get_formula();
            }
        }
    }

    Line2D getLine(Point2D initial, Point2D final) {
        return Line2D(initial, final);
    }
};


int main(){
    vector<Point2D> points {Point2D(-8,-3),Point2D(-4,-4),Point2D(2,2),Point2D(-1,1),Point2D(-6,-2)};
    Polygon triangle(points);
}