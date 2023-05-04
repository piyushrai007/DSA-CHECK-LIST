import java.util.ArrayList;
public class arrayList {
    public static void main(String[] args) {
    ArrayList<Integer> list = new ArrayList<Integer>();
    //add elemnt
    list.add(0,1);
    list.add(2);
    System.out.println(list);
    //get element
    int element = list.get(0);
    System.out.println(element);
    //element in betweeen
    list.set(0,5);
    System.out.println(list);
    //delet element 
    list.remove(0);
    System.out.println(list);
    }
    
}  