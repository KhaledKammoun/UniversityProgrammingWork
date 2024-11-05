public class App {
        // Test 1
public void TestMonnaie1(Monnaie m1, Monnaie m2) {
    try {
      

        // Valid case
        m1.Ajouter(m2);
        System.out.println("Nouvelle valeur après addition: " + m1.getValue() + " " + m1.getDevise());

    } catch (DeviseInvalideException e) {
        System.err.println("Erreur: " + e.getMessage());
    }
}
// Test 2
public void TestMonnaie2(Monnaie m1, Monnaie m2) {
    try {
        // Valid case
        m1.Retranche(m2);
        System.out.println("Nouvelle valeur après addition: " + m1.getValue() + " " + m1.getDevise());
    } catch (DeviseInvalideException e) {
        System.err.println("Erreur: " + e.getMessage());
    }
}
public static void main(String[] args) {
        try {
            Monnaie m4 = new Monnaie(200, "EUR");
            Monnaie m5 = new Monnaie(100, "EUR");       
            // Valid case
            m4.Retranche(m5);
            System.out.println("Nouvelle valeur après soustraction: " + m4.getValue() + " " + m4.getDevise());      
            // Invalid case: different currency
            Monnaie m6 = new Monnaie(100, "USD");
            m4.Ajouter(m6);
        } catch (DeviseInvalideException e) {
            System.err.println("Erreur: " + e.getMessage());
        }
    }
}
    