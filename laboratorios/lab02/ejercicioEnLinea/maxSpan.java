

public int maxSpan(int[] nums) {
    if (nums.length == 0) return 0;
    int[] map = new int[20];
    Arrays.fill(map, -1);
    int answer = 1;
    for (int i = 0; i < nums.length; i++) {
      if (map[nums[i]] != -1) {
        answer = Math.max(answer, i - map[nums[i]]+1);
      } else {
        map[nums[i]] = i;
      }
    }
    return answer;
  }