public class Fibonacci {
    public static void main(String[] args) {
        int num = 13;  //valor informado
        int a = 0;
        int b = 1;
        int aux = 0;

        System.out.print(a + " " + b);

        for(int i = 0; i < num; i++){
            a = a + b;
            b = a - b;
            System.out.print(" "+ a);
            if(a == num){
                aux++;
            }
        }

        if (aux > 0){
            System.out.println("\nO número "+ num + " pertence à sequência de Fibonacci!");
        }
        else {
            System.out.println("\nO número "+ num + " não pertence à sequência de Fibonacci!");
        }
    
    }
}
