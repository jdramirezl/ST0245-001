package laboratorios.lab01.codigo.Recursion2;

public class groupNoAdj {
    public boolean groupNoAdj(int start, int[] nums, int target) {
        if(target == 0) return true;
        if(start >= nums.length) return false;
        return groupNoAdj(start + 2, nums, target - nums[start]) || groupNoAdj(start + 1, nums, target);
    }
}
