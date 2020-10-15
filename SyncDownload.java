package com.example.delllaptop.projone;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;

import com.example.delllaptop.projone.DTO.DownloadImage;
import com.example.delllaptop.projone.DTO.Trip;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.ValueEventListener;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;

/**
 * Created by Dell Laptop on 3/13/2018.
 */

public class SyncDownload extends AsyncTask<ArrayList<Trip>,Void,Integer> {


    ArrayList<Trip> trips;
    ArrayList<Trip> tripsnew;
    private FirebaseAuth mAuth;
    private DatabaseReference db;
    private FirebaseUser fuser;
    SQLAdapter adapter;
    Context context;

    public SyncDownload(Context context, FirebaseAuth mAuth, DatabaseReference db, FirebaseUser fuser) {
        this.mAuth = mAuth;
        this.db = db;
        this.fuser = fuser;
        this.context = context;
    }

    @Override
    protected Integer doInBackground(ArrayList<Trip>[] arrayLists) {
        Log.i("elidfire",fuser.getEmail());
        adapter = new SQLAdapter(context);
        tripsnew = new ArrayList<Trip>();
        trips=adapter.retrieveTrips(fuser.getEmail());
        db.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Log.i("firebase", dataSnapshot.getChildren().toString());
                for (DataSnapshot templateSnapshot : dataSnapshot.getChildren()) {
                    Log.i("7aslaxxxx",templateSnapshot.getKey());
                    for (DataSnapshot dss : templateSnapshot.getChildren()) {
                        Log.i("7asla33333",dss.getKey());
                        Trip trip = dss.getValue(Trip.class);
                        if(trip.getUser().contains(fuser.getEmail())) {
                            Log.i("7aslatrip77878", trip.getName());
                            tripsnew.add(trip);
                            Log.i("7aslatripsize", tripsnew.size()+"");
                        }

                    }
                }
                Log.i("7aslatripwsl", tripsnew.size()+"");
                for(Trip trip: tripsnew){
                    Log.i("yaallaaaaah000000000",trip.getEd());
                    int flag = 0;
                    for(Trip temp: trips) {
                        Log.i("yaallaaaaah000000000",temp.getEd());
                        if (trip.getEd().contains(temp.getEd())) {
                            Log.i("yaallaaaaah12345","7asal");
                            flag = 1;
                            Log.i("yaallaaaaah111111",flag+"7asalflag1");
                        }
                    }
                    Log.i("yaallaaaaah111111",flag+"7asalflag2");
                    if (flag==0){
                        Log.i("ya allah ya rab","7asal 1");
                        DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                        DateFormat formate2 = new SimpleDateFormat("hh:mm");
                        Calendar c = Calendar.getInstance();
                        Calendar c2 = Calendar.getInstance();
                        try {
                            c2.setTime(format.parse(trip.getSd()));
                            int hournew = Integer.parseInt(trip.getSt().split(":")[0]),
                                    minnew = Integer.parseInt(trip.getSt().split(":")[1]);
                            Log.i("jdsfhsfusioeruwoiruw",minnew+ " "+hournew);
                            c2.set(Calendar.HOUR_OF_DAY,hournew);
                            c2.set(Calendar.MINUTE,minnew);
                            Log.i("jdsfhsfusioeruwoiru111w",c2.get(Calendar.HOUR_OF_DAY)+"");
                        } catch (ParseException e) {
                            e.printStackTrace();
                        }
                        Log.i("thedate",c+" "+c2);

                        if(c.after(c2)  && trip.getStatus().contains("upcoming")) {

                            Log.i("ya allah ya rab","7asal4");
                            adapter.insertTrip(trip.getName(), trip.getSp(), trip.getSlong(), trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), "cancelled", trip.getSd(), trip.getEd(), trip.getSt(), trip.getSt(), trip.getRep(), trip.getUser(), "new");
                        }else{

                            adapter.insertTrip(trip.getName(),trip.getSp(),trip.getSlong(),trip.getSlat(),trip.getEp(),trip.getElong(),trip.getElat(), trip.getStatus(),trip.getSd(),trip.getEd(),trip.getSt(),trip.getSt(),trip.getRep(),trip.getUser(),"new");
                        }
                    }

                }
                trips = adapter.retrieveTrips(fuser.getEmail());
                Log.i("thedate777",trips.size()+"");
                for(Trip trip: trips) {
                    Log.i("thedate778", trip.getUrl()+"");
                    if(trip.getUrl()!=null) {
                        Log.i("thedate779", "new");
                        if (!trip.getStatus().contains("upcoming")) {
                            Log.i("thedate780", "da5al hna");
                            String webLink = "https://maps.googleapis.com/maps/api/directions/json?origin=" + trip.getSlat() +
                                    "," + trip.getSlong() + "&destination=" + trip.getElat()
                                    + "," + trip.getElong();
                            DownloadImage dImg = new DownloadImage(webLink, context, trip);
                            dImg.execute();
                        }
                        else{
                            //hna el alarm set
                            Log.i("thedate781", "da5al hna");
                            String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                            DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                            DateFormat formate2 = new SimpleDateFormat("hh:mm");
                            Calendar myCal = Calendar.getInstance();
                            try {
                                Date myTime = formate2.parse(trip.getSt());
                                Date date2=format.parse(trip.getSd());
                                Log.i("aya", String.valueOf(myCal.getTime()));
                                myCal.setTime(date2);
                                myCal.set(Calendar.HOUR_OF_DAY,myTime.getHours());
                                myCal.set(Calendar.MINUTE,myTime.getMinutes());
                                HashMap<Integer,Date> myData = new HashMap<Integer, Date>();
                                AlarmManager myAlarm =(AlarmManager)context.getSystemService(Context.ALARM_SERVICE);
                                Intent i = new Intent(context, AlertReciever.class);
                                Bundle bundle = new Bundle();
                                bundle.putSerializable("trip", trip);
                                i.putExtra("bundle", bundle);
                                PendingIntent pi = PendingIntent.getBroadcast(context, trip.getId(), i, 0);
                                myAlarm.set(AlarmManager.RTC_WAKEUP,myCal.getTimeInMillis(),pi);
                            } catch (ParseException e) {
                                e.printStackTrace();
                            }

//                            a5er el alarm
                        }
                        for (Trip temp : tripsnew) {
                            Log.i("notessync", "ahoh ahoh ahoh");
                            if (trip.getUrl()!=null && trip.getEd().contains(temp.getEd())) {
                                Log.i("notessync2",temp.getNotes()+"");
                                if(temp.getNotes()!=null)
                                    for (String note : temp.getNotes()) {
                                        long i= adapter.insertNote(note, trip.getId());
                                        Log.i("notessync","ahoh ahoh ahoh" + i);
                                        trip.getNotes().add(note);
                                    }
                            }
                        }
                        trip.setUrl(null);
                        long i = adapter.updateTrip(trip.getId(), trip.getName(), trip.getSp(), trip.getSlong(),
                                trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), trip.getStatus(),
                                trip.getSd(), trip.getEd(), trip.getSt(), trip.getSt(), trip.getRep(), trip.getUser(), null);
                        Log.i("elxxxxi",i+"");
                    }
                    if(trip.getEd().contains("null")) {
                        String key = db.child(fuser.getUid()).push().getKey();
                        trip.setEd(key);
                        long i = adapter.updateTrip(trip.getId(), trip.getName(), trip.getSp(), trip.getSlong(),
                                trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), trip.getStatus(),
                                trip.getSd(), trip.getEd(), trip.getSt(), trip.getSt(), trip.getRep(), trip.getUser(), null);
                        db.child(fuser.getUid()).child(key).setValue(trip);
                        Log.i("a5eryom","awel mara " + i+trip.getEd());

                    }
                    else {
                        Log.i("a5eryom","else");
                        db.child(fuser.getUid()).child(trip.getEd()).setValue(trip);
                    }

                }
                db.removeEventListener(this);

            }
            @Override
            public void onCancelled(DatabaseError databaseError) {
                Log.i("7aslatriperror", tripsnew.size()+"");
            }

        });


        return null;
    }
}
