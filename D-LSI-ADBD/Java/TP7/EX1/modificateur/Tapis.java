package modificateur;

public class Tapis {
	float longueur ;
	public float largeur ;
	protected float prixMetreCarre ;
	
	public Tapis(float l, float larg,float prix) {
		this.longueur = l ;
		this.largeur = larg ;
		this.prixMetreCarre = prix ;
	}
	float calculerSurfaceTapis() {
		return largeur * longueur ;
	}
	protected float calculerPrixTapis(float surfaceTapis) {
		return prixMetreCarre * surfaceTapis ;
	}
}
