package laboratorios.lab01.codigo.Recursion2;

public class groupSum5 {
    public boolean groupSum5(int start, int[] nums, int target) {
        if(target == 0 && start >= nums.length) return true;
        if(start >= nums.length) return false;
        
        if (nums[start]%5==0 && start < nums.length - 1 && nums[start+1] == 1){
            return groupSum5(start + 2, nums, target - nums[start]);
        }
        
        boolean f = groupSum5(start + 1, nums, target - nums[start]);
        return nums[start]%5==0  ? f : f || groupSum5(start + 1, nums, target);
    }
}
