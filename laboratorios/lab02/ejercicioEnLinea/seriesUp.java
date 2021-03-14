
    public int[] seriesUp(int n) {
        int size = 0;
        for (int k = 1; k <= n; k++) size += k;
        int[] answer = new int[size];
        int j = 0;
        for (int i = 1; i <= n; i++) {
          for (int x = 1; x <= i; x++){
            answer[j] = x;
            j++;
          }
        }
        return answer;
      }

