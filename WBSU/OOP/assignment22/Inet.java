// Demonstrate Inet address
import java.net.*;

// driving code
class Inet{
    public static void main(String args[]) throws UnknownHostException{
        // obtaining localhost address
        InetAddress inetaddress_localhost = InetAddress.getLocalHost();
        System.out.println(String.format("LocalHost address: %s",inetaddress_localhost));

        // obtaining all address by URL
        InetAddress[] inetAddress = InetAddress.getAllByName("www.google.com");
        for(int i=0; i<inetAddress.length; i++){
            System.out.println(inetAddress[i]);
        }
    }
}