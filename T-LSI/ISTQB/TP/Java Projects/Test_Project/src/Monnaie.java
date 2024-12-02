
// Custom exception for Test
class DeviseInvalideException extends Exception {
    public DeviseInvalideException(String message) {
        super(message);
    }
}

public class Monnaie {
    private int valeur;
    private String devise ;

    Monnaie(int valeur, String devise) {
        this.valeur = valeur;
        this.devise = devise ;
    }

    void setValue(int value) {
        this.valeur = value ;
    }
    int getValue() {
        return this.valeur;

    }

    String getDevise() {
        return this.devise ;
    }

    public boolean Verif(Monnaie m1, Monnaie m2) {
        return m1.getDevise().equals(m2.getDevise()) ;
    }
        public void Ajouter(Monnaie m) throws DeviseInvalideException {
            if (!Verif(this, m)) {
                throw new DeviseInvalideException("Les devises ne correspondent pas : " + this.getDevise() + " | " + m.getDevise());
            }
            this.setValue(this.getValue() + m.getValue());
        }
    
        public void Retranche(Monnaie m) throws DeviseInvalideException {
            if (!Verif(this, m)) {
                throw new DeviseInvalideException("Les devises ne correspondent pas : " + this.getDevise() + " | " + m.getDevise());
            }
            this.setValue(this.getValue() - m.getValue());
        }
}
