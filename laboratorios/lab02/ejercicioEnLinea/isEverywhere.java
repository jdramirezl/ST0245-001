package laboratorios.lab02.ejercicioEnLinea;

public class isEverywhere {
    public boolean isEverywhere(int[] nums, int val) {
        int total = 0;
        
        if(nums.length == 0){
          return true;
        }
        
        for(int i = 0; i<nums.length-1; i++){
          if (nums[i]==val ||nums[i+1]==val){
            total++;
          }
        }
        
        return total == nums.length-1;
        
      }
}
