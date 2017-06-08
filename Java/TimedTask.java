package com.griffiths.devicemanager;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.Random;
import java.util.TimerTask;


public class TimedTask extends TimerTask{

	private Random rand = new Random();
	private int write = 1;	
	private int battLevel = rand.nextInt(85)+15;
	private int deviceTemp = rand.nextInt(25)+20;
	private int ambientTemp = rand.nextInt(25)+20;
	private int internalTemp = rand.nextInt(40)+40;
	private int decibels = rand.nextInt(100)+1;
	private int lumens = rand.nextInt(100)+1;	
	private int id = 15;
	private Connection con;
	
	public TimedTask(Connection con)
	{
		this.con = con;
	}
	
	@Override
	public final void run() {
		try 
		{ 
			String query = "insert into tbl_readings (device_id, device_temp, ambient_temp, internal_temp, lumens, decibels, battery) values ("+id+", "+
					deviceTemp+","+ambientTemp+","+internalTemp+","+lumens+","+decibels+","+battLevel+");";
			PreparedStatement preparedStmt = con.prepareStatement(query);
			preparedStmt.execute();
			
			String query1 = "update tbl_device set device_temp='"+deviceTemp+"', ambient_temp='"+ambientTemp+"', internal_temp='"+internalTemp+"', decibels='"+decibels+"', battery='"+battLevel+"', lumens='"+lumens+"' where id="+id+";"; 			
			PreparedStatement preparedStmt1 = con.prepareStatement(query1);
			preparedStmt1.execute();
			
			System.out.println("Wrote " + write);
			if (write%5==0)
			{
				deviceTemp++;
				if (deviceTemp>100)
				{
					deviceTemp=25;
				}
			}
			if (write%9==0)
			{
				battLevel--;
				if (battLevel==0)
				{
					battLevel=95;
				}
			}
			if (write%10==0)
			{
				ambientTemp++;
				if (ambientTemp>100)
				{
					ambientTemp=25;
				}
			}
			if (write%8==0)
			{
				internalTemp++;
				if (internalTemp>100)
				{
					internalTemp=40;
				}
			}
			
			//not needed, auto-commit automatically set
			//con.commit();
			write++;
		}
		catch (Exception ex)
		{
			System.out.println("Error is: " + ex);
		}
	}

}

