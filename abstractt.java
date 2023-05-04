abstract class Animal{
    abstract void walk();
    Animal(){
        System.out.println("you r creating animal");

    }
    public void eat(){
        System.out.println("animal eats");
    }

}
class Horse extends Animal{
    Horse()
    {
        System.out.println("created a horse");
    }
    public void walk() {
        System.out.println("walks on 4 legs");
        
    }
}   
class Chicken extends Animal{
    public void walk (){
        System.out.println("walks on 2 legs");
    }
}
public class abstractt {
    public static void main(String[] args) {
         Horse horse = new Horse();
         
    }
}
