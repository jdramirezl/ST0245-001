package laboratorios.lab01.codigo.Recursion2;

public class split53 {
    public boolean split(int[] nums, int f, int s, int i) {
        if(i >= nums.length) return f==s;
        if(nums[i]%3==0 && nums[i]%5!=0){
            return split(nums, f + nums[i], s, i + 1);
        }
        else if(nums[i]%5==0){
            return split(nums, f, s+ nums[i], i + 1);
        }
        
        return split(nums, f + nums[i], s, i + 1) || split(nums, f , s+ nums[i], i + 1);
    }
    
    public boolean split53(int[] nums) {
        return split(nums, 0, 0, 0);
    }
}
