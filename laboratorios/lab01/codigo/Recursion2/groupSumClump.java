package laboratorios.lab01.codigo.Recursion2;

public class groupSumClump {
    public boolean groupSumClump(int start, int[] nums, int target) {
        if(target == 0) return true;
        if(start >= nums.length) return false;
        
        int copia = target;
        
        target -= nums[start];
        while(start < nums.length - 1 && nums[start] == nums[start+1]){
            start++;
            target -= nums[start];
        }
        start++;
        
        return groupSumClump(start, nums, target) || groupSumClump(start, nums, copia);
    }
}
