public class Employer {
	private String name, title,manager;
	public Employer(String n, String t,String m) {
		this.name=n;
		this.title=t;
		this.manager=m;
	}
	public static void main(String[] args) {
		
		Employer e= new Employer(args[0],args[1],args[2]);
		System.out.println("name :" +e.name);
		System.out.println("title :" +e.title);
		System.out.println("manager :" +e.manager);
	}
}
