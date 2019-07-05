package game;



import org.junit.Test;

import static game.GameManager.fight;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class GameManagerTest {
    @Test
    public void twoElvesFight_AllAlive() {
        // Arrange
        Elf ch1 = new Elf();
        Elf ch2 = new Elf();

        // Act
        fight(ch1, ch2);

        // Assert
        assertTrue(ch1.isAlive());
        assertTrue(ch2.isAlive());
    }

    @Test
    public void TwoHobbitsFight_AllAlive() {
        // Arrange
        Hobbit ch1 = new Hobbit();
        Hobbit ch2 = new Hobbit();

        // Act
        fight(ch1, ch2);

        // Assert
        assertTrue(ch1.isAlive());
        assertTrue(ch2.isAlive());
    }

    @Test
    public void HobbitKingFight_HobbitDead() {
        // Arrange
        Hobbit ch1 = new Hobbit();
        King ch2 = new King();

        // Act
        fight(ch1, ch2);

        // Assert
        assertFalse(ch1.isAlive());
        assertTrue(ch2.isAlive());
    }

    @Test
    public void ElfHobbitFight_HobbitDead() {
        // Arrange
        Elf ch1 = new Elf();
        Hobbit ch2 = new Hobbit();

        // Act
        fight(ch1, ch2);

        // Assert
        assertTrue(ch1.isAlive());
        assertFalse(ch2.isAlive());
    }

    @Test
    public void HobbitElfFight_HobbitDead() {
        // Arrange
        Hobbit ch1 = new Hobbit();
        Elf ch2 = new Elf();

        // Act
        fight(ch1, ch2);

        // Assert
        assertFalse(ch1.isAlive());
        assertTrue(ch2.isAlive());
    }

    @Test
    public void KnightHobbitFight_HobbitDead() {
        // Arrange
        Knight ch1 = new Knight();
        Hobbit ch2 = new Hobbit();

        // Act
        fight(ch1, ch2);

        // Assert
        assertTrue(ch1.isAlive());
        assertFalse(ch2.isAlive());
    }
}
