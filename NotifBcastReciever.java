package com.example.delllaptop.projone;

import android.app.AlarmManager;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;

import com.example.delllaptop.projone.DTO.DownloadImage;
import com.example.delllaptop.projone.DTO.Trip;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;

/**
 * Created by Dell Laptop on 3/17/2018.
 */

public class NotifBcastReciever extends BroadcastReceiver {

    public NotifBcastReciever() {
        super();
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getStringExtra("action");
        Trip trip = (Trip) intent.getSerializableExtra("trip");
        Log.i("bacst",1+"");
        NotificationManager nm = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
        nm.cancel(trip.getId()+1000);
        if (action.contains("Cancel")){
            Log.i("bacst",1+"");
            SQLAdapter adapter = new SQLAdapter(context);
            trip.setStatus("Done");
            long i2 = adapter.updateTrip(trip.getId(),trip.getName(),trip.getSp(),trip.getSlong(),trip.getSlat(),trip.getEp(),trip.getElong(),trip.getElat(), "Cancelled",trip.getSd(),trip.getSd(),trip.getSt(),trip.getSt(),trip.getRep(),trip.getUser(),null);
            String uri = "http://maps.google.com/maps?" + "&daddr=" + trip.getElat()
                    + "," + trip.getElong();
            String webLink = "https://maps.googleapis.com/maps/api/directions/json?origin=" + trip.getSlat() +
                    "," + trip.getSlong() + "&destination=" + trip.getElat()
                    + "," + trip.getElong();
            DownloadImage dImg = new DownloadImage(webLink,context,trip);
            dImg.execute();
            if(trip.getRep()!=0) {
                DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                Calendar c = Calendar.getInstance();
                try {
                    c.setTime(format.parse(trip.getSd()));
                } catch (ParseException e) {
                    e.printStackTrace();
                }
                c.add(Calendar.DATE, trip.getRep());
                String tripdate = (format.format(c.getTime()));
                long i = adapter.insertTrip(trip.getName(), trip.getSp(), trip.getSlong(), trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), "upcoming", tripdate, null, trip.getSt(), trip.getSt(), trip.getRep(), trip.getUser(), null);
                ArrayList<Trip> trips = adapter.retrieveTrips(trip.getUser());
                int newid = trips.get(trips.size()-1).getId();
                DateFormat formate2 = new SimpleDateFormat("hh:mm");
                Calendar myCal = Calendar.getInstance();
                try {
                    Date myTime = formate2.parse(trips.get(trips.size()-1).getSt());
                    Date date2=format.parse(trips.get(trips.size()-1).getSd());
                    Log.i("aya", String.valueOf(myCal.getTime()));
                    myCal.setTime(date2);
                    myCal.set(Calendar.HOUR_OF_DAY,myTime.getHours());
                    myCal.set(Calendar.MINUTE,myTime.getMinutes());
                    HashMap<Integer,Date> myData = new HashMap<Integer, Date>();
                    AlarmManager myAlarm =(AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                    Intent newInt = new Intent(context, AlertReciever.class);
                    newInt.putExtra("trip",trips.get(trips.size()-1));
                    Bundle bundle2 = new Bundle();
                    bundle2.putSerializable("trip",trips.get(trips.size()-1));
                    newInt.putExtra("bundle",bundle2);
                    PendingIntent pi = PendingIntent.getBroadcast(context, trips.get(trips.size()-1).getId(), newInt, 0);
                    myAlarm.set(AlarmManager.RTC_WAKEUP,myCal.getTimeInMillis(),pi);
                } catch (ParseException e) {
                    e.printStackTrace();
                }
            }

        }
        else if(action.contains("start")){
            Log.i("bacst",1+"");
            SQLAdapter adapter = new SQLAdapter(context);
            long i2 = adapter.updateTrip(trip.getId(),trip.getName(),trip.getSp(),trip.getSlong(),trip.getSlat(),trip.getEp(),trip.getElong(),trip.getElat(), "Done",trip.getSd(),trip.getSd(),trip.getSt(),trip.getSt(),trip.getRep(),trip.getUser(),null);
            String uri = "http://maps.google.com/maps?" + "&daddr=" + trip.getElat()
                    + "," + trip.getElong();
            Intent intent2 = new Intent(Intent.ACTION_VIEW, Uri.parse(uri));
            intent2.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            trip.setStatus("Done");
            String webLink = "https://maps.googleapis.com/maps/api/directions/json?origin=" + trip.getSlat() +
                    "," + trip.getSlong() + "&destination=" + trip.getElat()
                    + "," + trip.getElong();
            DownloadImage dImg = new DownloadImage(webLink,context,trip);
            dImg.execute();
            if(trip.getRep()!=0) {
                DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                Calendar c = Calendar.getInstance();
                try {
                    c.setTime(format.parse(trip.getSd()));
                } catch (ParseException e) {
                    e.printStackTrace();
                }
                c.add(Calendar.DATE, trip.getRep());
                String tripdate = (format.format(c.getTime()));
                long i = adapter.insertTrip(trip.getName(), trip.getSp(), trip.getSlong(), trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), "upcoming", tripdate, null, trip.getSt(), trip.getSt(), trip.getRep(), trip.getUser(), null);
                ArrayList<Trip> trips = adapter.retrieveTrips(trip.getUser());
                int newid = trips.get(trips.size()-1).getId();
                DateFormat formate2 = new SimpleDateFormat("hh:mm");
                Calendar myCal = Calendar.getInstance();
                try {
                    Date myTime = formate2.parse(trips.get(trips.size()-1).getSt());
                    Date date2=format.parse(trips.get(trips.size()-1).getSd());
                    Log.i("aya", String.valueOf(myCal.getTime()));
                    myCal.setTime(date2);
                    myCal.set(Calendar.HOUR_OF_DAY,myTime.getHours());
                    myCal.set(Calendar.MINUTE,myTime.getMinutes());
                    HashMap<Integer,Date> myData = new HashMap<Integer, Date>();
                    AlarmManager myAlarm =(AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                    Intent newInt = new Intent(context, AlertReciever.class);
                    newInt.putExtra("trip",trips.get(trips.size()-1));
                    Bundle bundle2 = new Bundle();
                    bundle2.putSerializable("trip",trips.get(trips.size()-1));
                    newInt.putExtra("bundle",bundle2);
                    PendingIntent pi = PendingIntent.getBroadcast(context, trips.get(trips.size()-1).getId(), newInt, 0);
                    myAlarm.set(AlarmManager.RTC_WAKEUP,myCal.getTimeInMillis(),pi);
                } catch (ParseException e) {
                    e.printStackTrace();
                }
            }
            Intent floatingSer = new Intent(context, FloatingService.class);
            Bundle bundle2 = new Bundle();
            bundle2.putSerializable("trip",trip);
//                        //////////////////
//                        bundle.putParcelable("notes",notesParce);
//                        Log.i("parcebundle",notesParce.getNotes()+"");
//                        ///////////////////
            floatingSer.putExtra("bundle",bundle2);
            context.startService(floatingSer);
            context.startActivity(intent2);

        }
    }

    @Override
    public IBinder peekService(Context myContext, Intent service) {
        return super.peekService(myContext, service);
    }
}
