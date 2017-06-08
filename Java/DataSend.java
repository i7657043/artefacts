package com.griffiths.devicemanager;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Timer;
import java.util.TimerTask;

public class DataSend {
	
	private static String URL = "jdbc:mysql://*?useSSL=false";
	private static String P = "*";
	private static String U = "*";
	
	public static void main(String[] args) throws SQLException
	{
		
		
		Connection con = DriverManager.getConnection(URL,U,P);
		System.out.println("Connected...");
		
		TimerTask task = new TimedTask(con);
		Timer timer = new Timer();

		//every second
		timer.schedule(task, 0, 1000);
		

	}
}