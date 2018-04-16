
public class ArraysOfStrings {

	public static void main(String[] args) {

		String[] words = new String[3];
		
		words[0] = "Hello";
		words[1] = "to";
		words[2] = "you";
		
		System.out.println(words[2]);
		
		for(int i =0; i<words.length;i++)
			System.out.println(words[i]);
		
		String[] fruits = {"apple", "bannana", "pear", "kiwi"};
		
		for(String fruit: fruits) {
			System.out.println(fruit);
		}
		
		int value = 123;
		
		
	}

}
