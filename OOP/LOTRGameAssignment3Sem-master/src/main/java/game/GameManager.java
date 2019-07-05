package game;

public class GameManager {
    public static void fight(Character c1, Character c2){
        System.out.println("Now " + c1.getClass() + "'s power is " + c1.getPower() + " and hp is " + c1.getHp());
        System.out.println("and " + c2.getClass() + "'s power is " + c2.getPower() + " and hp is " + c2.getHp() + "\n");
        while(c1.isAlive() && c2.isAlive()){
            if (c1.getClass() == Hobbit.class && c2.getClass() == Hobbit.class){
                System.out.println("hobbit can not fight hobbit, game over.");
                return;
            }
            if (c1.getClass() == Elf.class && c2.getClass() == Elf.class){
                System.out.println("Elf can not fight Elf, game over.");
                return;
            }
            c1.kick(c2);
            System.out.println(c1.getClass() + " kicked the " + c2.getClass());
            System.out.println("Now " + c1.getClass() + "'s power is " + c1.getPower() + " and hp is " + c1.getHp());
            System.out.println("and " + c2.getClass() + "'s power is " + c2.getPower() + " and hp is " + c2.getHp() + "\n");

            c2.kick(c1);
            System.out.println(c2.getClass() + " kicked the " + c1.getClass());
            System.out.println("Now " + c1.getClass() + "'s power is " + c1.getPower() + " and hp is " + c1.getHp());
            System.out.println("and " + c2.getClass() + "'s power is " + c2.getPower() + " and hp is " + c2.getHp()+ "\n");
        }
    }

    public static void main(String[] args) {
        CharacterFactory charFac = new CharacterFactory();
        CharacterFactory charFc = new CharacterFactory();
        Character ch1 = charFac.makeChar();
        Character ch2 = charFc.makeChar();
        fight(ch1, ch2);
        System.out.println(ch1.isAlive() + " ch1");
        System.out.println(ch2.isAlive() + " ch2");
    }
}
