package game;


import org.junit.Test;

import static junit.framework.TestCase.assertTrue;


public class CharacterFactoryTest {
    @Test
    public void factoryMakeCharacter_IsAlive() {
        // Arrange
        CharacterFactory factory = new CharacterFactory();

        // Act
        Character ch = factory.makeChar();

        // Assert
        assertTrue(ch.isAlive());
    }
}
