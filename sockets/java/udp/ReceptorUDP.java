package udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

import javax.swing.JOptionPane;

public class ReceptorUDP {
	public static void main(String[] args) {
		
		try {
			// Converte o argumento recebido para inteiro (numero da porta)
			int port = 12345;
			// Cria o DatagramSocket para aguardar mensagens, neste momento o metodo fica
			// bloqueando
			// ate o recebimente de uma mensagem
			DatagramSocket ds = new DatagramSocket(port);
			System.out.println("Ouvindo a porta: " + port);
			// Preparando o buffer de recebimento da mensagem
			byte[] msg = new byte[256];
			// Prepara o pacote de dados
			DatagramPacket pkg = new DatagramPacket(msg, msg.length);
			// Recebimento da mensagem
			ds.receive(pkg);
			JOptionPane.showMessageDialog(null, new String(pkg.getData()).trim(), "Mensagem recebida", 1);
			System.out.println("Mensagem Recebida!");
			ds.close();
		}

		catch (IOException ioe) {
			System.out.println("Erro!!! " + ioe.getMessage());
		}
	}

}
