package lv.vogella.emf.webpage.usingmodel;

import lv.vogella.webpage.model.webpage.Web;
import lv.vogella.webpage.model.webpage.WebPage;
import lv.vogella.webpage.model.webpage.WebpageFactory;
import lv.vogella.webpage.model.webpage.WebpagePackage;

public class UsingEMFNodel {
	public static void main(String[] args) {
		WebpagePackage webpackage = WebpagePackage.eINSTANCE;		
		
		WebpageFactory factory = WebpageFactory.eINSTANCE;
		
		Web web = factory.createWeb();
		web.setName("Hallo");
		web.setDescription("This is descriprion");
		
		WebPage webpage = factory.createWebPage();
		webpage.setTitle("This is title");
	}
}