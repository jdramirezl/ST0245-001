package laboratorios.lab01.codigo.Recursion1;

public class triangle {
    public int triangle(int rows) {
        if (rows == 0){
            return 0;
        } else if (rows == 1){
            return 1;
        } else {
            return rows+triangle(rows-1);
        }
    }
}
