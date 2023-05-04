class pen{
    String color;
    String type;
    public void printColor() {
        System.out.println(this.color);
    } 

}
public class Oops {
public static void main(String[] args) {
    pen pen1 = new pen();//pen( )-->constructor 
    pen1.color ="blue";
    pen1.type ="gel";
    pen1.printColor();
    
}
}