public int[] squareUp(int n) {
    int[] answer = new int[n * n];
    Arrays.fill(answer, 0);
    for (int i = n; i > 0; i--) {
        int tmp = (i * n) - 1;
        for (int j = 1; j <= i; j++){
          answer[tmp] = j;
          tmp--;
        }
    }
    return answer;
  }
  