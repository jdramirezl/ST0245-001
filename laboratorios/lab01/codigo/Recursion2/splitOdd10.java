package laboratorios.lab01.codigo.Recursion2;

public class splitOdd10 {
    public boolean split(int[] nums, int ten, int odd, int i) {
        if(i >= nums.length) return ten%10==0 && odd%2!=0;
        return split(nums, ten + nums[i], odd, i + 1) || split(nums, ten , odd+ nums[i], i + 1);
    }
    
    public boolean splitOdd10(int[] nums) {
        return split(nums, 0, 0, 0);
    }
}
