package laboratorios.lab02.ejercicioEnLinea;

public class fizzBuzz {
    public String[] fizzBuzz(int start, int end) {
        String[] nums = new String[end-start];
        
        for(int i = start, indice = 0; i < end; i++, indice++){
          
          if(i%15==0){
            nums[indice] = "FizzBuzz";
          }
          else if(i%5==0){
            nums[indice] = "Buzz";
          }
          else if(i%3==0){
            nums[indice] = "Fizz";
          }
          else{
            nums[indice] = String.valueOf(i);
          }
        }
        
        return nums;
        
      }
}
