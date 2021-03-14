public boolean linearIn(int[] outer, int[] inner) {
    if (inner.length == 0) return true; 
    int i = 0, j = 0;
    while (outer[i] < inner[0]) i++;
    while(i < outer.length && j < inner.length) {
      if (outer[i] == inner[j]) j++;
      i++;
    }
    return j == inner.length;
  }
  