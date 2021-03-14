package laboratorios.lab02.ejercicioEnLinea;

public class sum28 {
    public boolean sum28(int[] nums) {
        int total = 0;
        for (int i = 0; i < nums.length; i++){
          if(nums[i] == 2){
            total += 2;
          }
        }
        
        if(total == 8){
          return true;
        }
        
        return false;
        
      }
}
