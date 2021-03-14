
    public boolean canBalance(int[] nums) {
        if (nums.length < 2) return false;
        for (int i = 1; i < nums.length; i++) nums[i] += nums[i-1];
        for (int i =0 ; i < nums.length; i++) {
          if (2 * nums[i] == nums[nums.length -1]) return true;
        }
        return false;
      }      
