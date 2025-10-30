package udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class RemetenteUDP {
	public static void main(String[] args) {

	    try {
	      //Primeiro argumento é o nome do host destino
	      InetAddress addr = InetAddress.getByName("localhost");
	      int port = 12345;
	      byte[] msg = "TESTE".getBytes();
	      //Monta o pacote a ser enviado
	      DatagramPacket pkg = new DatagramPacket(msg,msg.length, addr, port);
	      // Cria o DatagramSocket que será responsável por enviar a mensagem
	      DatagramSocket ds = new DatagramSocket();
	      //Envia a mensagem
	      ds.send(pkg);
	      System.out.println("Mensagem enviada para: " + addr.getHostAddress() + "\n" +
		      "Porta: " + port + "\n" + "Mensagem: " );

	      //Fecha o DatagramSocket
	      ds.close();     
	    }

	    catch(IOException ioe) {
	    	System.out.println("Erro de emissão!" + ioe.getMessage());
	    }
	  }
}
