
public class WhileLoops {

    public static void main(String[] args) {
        int i = 5, j = 5;

        while (i > 0) 
        {
            while (j > 0) {
                System.out.print("*");
                j--;
            }
            i--;
            j = i;
            System.out.print("\n");
        }
    }
}