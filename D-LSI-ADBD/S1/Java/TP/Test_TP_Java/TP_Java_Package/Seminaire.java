package TP_Java_Package;
import java.util.ArrayList ;
import java.util.List ;
public class Seminaire {
	String intitule, periode, lieu ;
	int frai_indust = 100, frai_univ = 200 ;
	public List<Participant> part ;
	public Seminaire(String intitule, String periode, String lieu, int frai_univ, int frai_indust) {
        this.intitule = intitule;
        this.periode = periode;
        this.lieu = lieu;
        this.frai_indust = frai_indust;
        this.frai_univ = frai_univ;
        this.part = new ArrayList<>();
    }
	public void addPart(Participant participant) {
        part.add(participant);
    }
	public int recette() {
		int montant = 0 ;
		for (Participant participant : part) {
            if (participant instanceof industriels) {
            	montant += frai_indust;
            } else if (participant instanceof Universitaire) {
            	montant += frai_univ;
            }
        }
		return montant ;
	}
	
	public String toString() {
		return "Seminaire{ intitule : " + intitule + ", periode : " + periode + ", lieu : " + lieu +  "}" ;		
	}
}
