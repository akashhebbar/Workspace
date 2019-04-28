public class StringBufferExample {
	public static void main(String[] args) {
		StringBuffer sb = new StringBuffer("hellogoodmorning ");
		System.out.println("Given stringbuffer is: " + sb);
		System.out.println("length of stringbuffer is: " + sb.length() + ", capacity of stringbuffer is: " + sb.capacity());
		System.out.println("character at index 5 of the stringbuffer is: " + sb.charAt(5));
		System.out.println("codePointAt index 5 of the stringbuffer is: " + sb.codePointAt(5));
		System.out.println("append the stringbuffer: " + sb.append("appended"));
        System.out.println("substring of stringbuffer from index 10 to 20 is: " + sb.substring(10,20));
        System.out.println("deleteing of string from index 5 to 10 is: " + sb.delete(5,10));
		System.out.println("reverse of the stringbuffer is: " + sb.reverse());
		System.out.println("insert to the stringbuffer is: " + sb.insert(16,1233));
	}
}