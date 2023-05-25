import java.util.Scanner;
import java.net.URL;
import java.net.MalformedURLException;
class MetaURL {
    private static Scanner scan = new Scanner(System.in);
    public static void main(String args[]) throws MalformedURLException{
        System.out.print("Enter URL: ");
        String urlString = scan.nextLine();
        System.out.println("Source URL: "+urlString);
        
        URL url = new URL(urlString);
        System.out.println("Applet: "+url.getHost());
        System.out.println("Port: "+url.getPort());
        System.out.println("Protocol: "+url.getProtocol());
        System.out.println("URL: "+url.getFile());
        scan.close();
    }
}
