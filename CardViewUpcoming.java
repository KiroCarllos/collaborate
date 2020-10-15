package com.example.delllaptop.projone;

import android.app.Activity;
import android.app.AlarmManager;
import android.app.AlertDialog;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.app.PendingIntent;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.PopupMenu;
import android.widget.TextView;
import android.widget.Toast;

import com.example.delllaptop.projone.DTO.DownloadImage;
import com.example.delllaptop.projone.DTO.LocationObject;
import com.example.delllaptop.projone.DTO.Trip;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Locale;

/**
 * Created by Dell Laptop on 3/9/2018.
 */
public class CardViewUpcoming extends RecyclerView.Adapter<CardViewUpcoming.CardViewHolder>{

    Context context;
    ArrayList<Trip> trips;
    LayoutInflater inflater;
    private ArrayAdapter<String> listAdapter ;
    SharedPreferences saving;
    UpcomingFrag upcomingFrag;
    FragmentManager fM;

    public CardViewUpcoming(Context context, ArrayList<Trip> trips) {
        this.context = context;
        this.trips = trips;
        saving=context.getSharedPreferences("imgurl",0);
        inflater = LayoutInflater.from(context);

    }

    @Override
    public CardViewHolder onCreateViewHolder(ViewGroup parent, int position) {
        View view = inflater.inflate(R.layout.upcoming_item,parent,false);
        CardViewHolder holder = new CardViewHolder(view);

        return holder;
    }

    @Override
    public void onBindViewHolder(CardViewHolder holder, final int position) {

        holder.menuup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopupMenu popup = new PopupMenu(context, v);
                MenuInflater inflater = popup.getMenuInflater();
                inflater.inflate(R.menu.menu_action, popup.getMenu());
                popup.setOnMenuItemClickListener(new PopupMenu.OnMenuItemClickListener() {
                    @Override
                    public boolean onMenuItemClick(MenuItem item) {
                        if(item.getItemId() == R.id.notesAct){
                            if(trips.get(position).getNotes().isEmpty()) {
                                Intent intent2 = new Intent(context, AddNoteActivity.class);
                                intent2.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                                intent2.putExtra("trip_id", trips.get(position).getId());
                                context.startActivity(intent2);
                            }
                            else{
                                Intent intent2 = new Intent(context, UpdateNoteActivity.class);
                                intent2.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                                intent2.putExtra("trip", trips.get(position));
                                context.startActivity(intent2);
                            }
                        }
                        if(item.getItemId() == R.id.editAct){
                            if(new CheckPermissions(context).checkInternet()) {
                                Intent intent2 = new Intent(context, UpdateTripActivity.class);
                                intent2.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                                intent2.putExtra("trip", trips.get(position));
                                context.startActivity(intent2);
                            }
                        }
                        if(item.getItemId() == R.id.cancelAct){
                            trips.get(position).setStatus("Cancelled");
                            SQLAdapter adapter = new SQLAdapter(context);
                            long i2 = adapter.updateTrip(trips.get(position).getId(),trips.get(position).getName(),
                                    trips.get(position).getSp(),trips.get(position).getSlong(),trips.get(position).getSlat(),
                                    trips.get(position).getEp(),trips.get(position).getElong(),trips.get(position).getElat(),
                                    trips.get(position).getStatus(),trips.get(position).getSd(),trips.get(position).getEd(),
                                    trips.get(position).getSt(),trips.get(position).getEd(),trips.get(position).getRep(),
                                    trips.get(position).getUser(),null);
                            AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                            Intent myIntent = new Intent(context, AlertReciever.class);
                            PendingIntent pendingIntent = PendingIntent.getBroadcast(context, trips.get(position).getId(), myIntent,
                                    PendingIntent.FLAG_UPDATE_CURRENT);
                            alarmManager.cancel(pendingIntent);
                            upcomingFrag = new UpcomingFrag();
                            fM = ((Activity)context).getFragmentManager();
                            FragmentTransaction fT = fM.beginTransaction();
                            fT.replace(R.id.mainFrag,upcomingFrag,"upcoming");
                            fT.commit();
                        }
                        if(item.getItemId() == R.id.delAct){
                            AlertDialog.Builder builder = new AlertDialog.Builder(context);
                            builder.setMessage("Are you sure you want to delete.");
                            builder.setCancelable(false);
                            Boolean check = false;
                            builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialog, int id) {
                                    SQLAdapter adapter = new SQLAdapter(context);
                                    long i = adapter.deleteTrip(trips.get(position).getId());
                                    AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                                    Intent myIntent = new Intent(context, AlertReciever.class);
                                    PendingIntent pendingIntent = PendingIntent.getBroadcast(context, trips.get(position).getId(), myIntent,
                                            PendingIntent.FLAG_UPDATE_CURRENT);
                                    alarmManager.cancel(pendingIntent);
                                    UpcomingFrag upcomingFrag = new UpcomingFrag();
                                    fM = ((Activity)context).getFragmentManager();
                                    FragmentTransaction fT = fM.beginTransaction();
                                    fT.replace(R.id.mainFrag,upcomingFrag,"upcoming");
                                    fT.commit();
                                }
                            });
                            builder.setNegativeButton("No", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialog, int which) {
                                    dialog.cancel();
                                }
                            });
                            AlertDialog alert11 = builder.create();
                            if (Build.VERSION.SDK_INT >= 26) {
                                alert11.getWindow().setType(WindowManager.LayoutParams.TYPE_APPLICATION_PANEL);
                            }
                            else {
                                alert11.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
                            }
                            alert11.setCanceledOnTouchOutside(false);
                            alert11.show();
                        }
                        return false;
                    }
                });
                popup.show();
            }
        });

        ////////////////////////
        holder.name.setText(trips.get(position).getName());
        holder.status.setText(trips.get(position).getStatus());
        holder.startdate.setText(trips.get(position).getSd()+"       "+trips.get(position).getSt());
        holder.startpoint.setText(trips.get(position).getSp());
        holder.endpoint.setText(trips.get(position).getEp());
        if(trips.get(position).getRep()==0) {
            holder.reps.setText("");
        }
        else if(trips.get(position).getRep()==1) {
            holder.reps.setText("Daily");
        }
        else if(trips.get(position).getRep()==7) {
            holder.reps.setText("Weekly");
        }
        else if(trips.get(position).getRep()==30) {
            holder.reps.setText("Monthly");
        }
        holder.startbut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                DateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                DateFormat timeFormat = new SimpleDateFormat("hh:mm");
                Calendar myCal = Calendar.getInstance();
                String stime = timeFormat.format(myCal.getTime());
                String sdate = dateFormat.format(myCal.getTime());
                Toast.makeText(context,"Trip Started",Toast.LENGTH_SHORT).show();
                SQLAdapter adapter = new SQLAdapter(context);
                long i2 = adapter.updateTrip(trips.get(position).getId(),trips.get(position).getName(),
                        trips.get(position).getSp(),trips.get(position).getSlong(),trips.get(position).getSlat()
                        ,trips.get(position).getEp(),trips.get(position).getElong(),trips.get(position).getElat(),
                        "Done",sdate,trips.get(position).getEd(),stime,stime,trips.get(position).getRep(),
                        trips.get(position).getUser(),null);
                String uri = "http://maps.google.com/maps?" + "&daddr=" + trips.get(position).getElat()
                        + "," + trips.get(position).getElong();
                Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(uri));
                trips.get(position).setStatus("Done");
                String webLink = "https://maps.googleapis.com/maps/api/directions/json?origin=" + trips.get(position).getSlat() +
                        "," + trips.get(position).getSlong() + "&destination=" + trips.get(position).getElat()
                        + "," + trips.get(position).getElong();
                DownloadImage dImg = new DownloadImage(webLink,context,trips.get(position));
                if(new CheckPermissions(context).checkInternet()) {
                    dImg.execute();
                }
                ///////////////////////////cancel alarm adeem ///////////////////////////////
                AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
                Intent myIntent = new Intent(context, AlertReciever.class);
                PendingIntent pendingIntent = PendingIntent.getBroadcast(context, trips.get(position).getId(), myIntent,
                        PendingIntent.FLAG_UPDATE_CURRENT);
                alarmManager.cancel(pendingIntent);
                ///////////////////////////////////////////////////////
                if(trips.get(position).getRep()!=0) {
                    DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                    Calendar c = Calendar.getInstance();
                    try {
                        c.setTime(format.parse(trips.get(position).getSd()));
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    c.add(Calendar.DATE, trips.get(position).getRep());
                    String tripdate = (format.format(c.getTime()));
                    long i = adapter.insertTrip(trips.get(position).getName(), trips.get(position).getSp(),
                            trips.get(position).getSlong(), trips.get(position).getSlat(), trips.get(position).getEp(),
                            trips.get(position).getElong(), trips.get(position).getElat(), "upcoming", tripdate,
                            "null", trips.get(position).getSt(), trips.get(position).getSt(), trips.get(position).getRep(),
                            trips.get(position).getUser(), null);


                    ///////////////////////////////////////// awel el alarm/////////////////////////////////
                    trips = adapter.retrieveTrips(trips.get(position).getUser());
                    int newid = trips.get(trips.size()-1).getId();
                    DateFormat formate2 = new SimpleDateFormat("hh:mm");
                    myCal = Calendar.getInstance();
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
                        PendingIntent pi = PendingIntent.getBroadcast(context, trips.get(trips.size()-1).getId(), newInt, PendingIntent.FLAG_UPDATE_CURRENT);
                        myAlarm.set(AlarmManager.RTC_WAKEUP,myCal.getTimeInMillis(),pi);
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    //////////////////////////a5er el alarm/////////////////////////////////////////////////////////
                }
                Intent floatingSer = new Intent(v.getContext(), FloatingService.class);
                Bundle bundle = new Bundle();
                bundle.putSerializable("trip",trips.get(position));
                floatingSer.putExtra("bundle",bundle);
                context.startActivity(intent);
                v.getContext().startService(floatingSer);

            }
        });

//        holder.delBut.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                AlertDialog.Builder builder = new AlertDialog.Builder(context);
//                builder.setMessage("Are you sure you want to delete.");
//                builder.setCancelable(false);
//                Boolean check = false;
//                builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
//                    @Override
//                    public void onClick(DialogInterface dialog, int id) {
//                        SQLAdapter adapter = new SQLAdapter(context);
//                        long i = adapter.deleteTrip(trips.get(position).getId());
//                        UpcomingFrag upcomingFrag = new UpcomingFrag();
//                        fM = ((Activity)context).getFragmentManager();
//                        FragmentTransaction fT = fM.beginTransaction();
//                        fT.replace(R.id.mainFrag,upcomingFrag,"hist");
//                        fT.commit();
//                    }
//                });
//                builder.setNegativeButton("No", new DialogInterface.OnClickListener() {
//                    @Override
//                    public void onClick(DialogInterface dialog, int which) {
//                        dialog.cancel();
//                    }
//                });
//                AlertDialog alert11 = builder.create();
//                if (Build.VERSION.SDK_INT >= 26) {
//                    alert11.getWindow().setType(WindowManager.LayoutParams.TYPE_APPLICATION_PANEL);
//                }
//                else {
//                    alert11.getWindow().setType(WindowManager.LayoutParams.TYPE_SYSTEM_ALERT);
//                }
//                alert11.setCanceledOnTouchOutside(false);
//                alert11.show();
//            }
//        });

        //   final ArrayList<Notes> mynotes =
//        ArrayList<String> noteList = trips.get(position).getNotes();
//        if(!noteList.isEmpty()) {
//            listAdapter = new ArrayAdapter<String>(context, R.layout.list, R.id.noteX, noteList);
//            holder.notes.setAdapter(listAdapter);
//            holder.notes.setOnTouchListener(new ListView.OnTouchListener() {
//                @Override
//                public boolean onTouch(View v, MotionEvent event) {
//                    int action = event.getAction();
//                    switch (action) {
//                        case MotionEvent.ACTION_DOWN:
//                            // Disallow ScrollView to intercept touch events.
//                            v.getParent().requestDisallowInterceptTouchEvent(true);
//                            break;
//
//                        case MotionEvent.ACTION_UP:
//                            // Allow ScrollView to intercept touch events.
//                            v.getParent().requestDisallowInterceptTouchEvent(false);
//                            break;
//                    }
//
//                    // Handle ListView touch events.
//                    v.onTouchEvent(event);
//                    return true;
//                }
//            });
//        }
        holder.notesbut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builderSingle = new AlertDialog.Builder(context);
                builderSingle.setTitle("Notes");
                listAdapter = new ArrayAdapter<String>(context, R.layout.list, R.id.noteX, trips.get(position).getNotes());
                builderSingle.setAdapter(listAdapter, new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                    }
                });
                builderSingle.show();
            }
        });

    }

    @Override
    public int getItemCount() {
        return trips.size();
    }


    class CardViewHolder extends RecyclerView.ViewHolder{
        TextView name;
        TextView status;
        TextView startdate;
        TextView startpoint;
        TextView endpoint;
        TextView reps;
//        ListView notes;
//        Button addNotes;
//        Button edit;
        Button startbut;
//        Button cancel;
//        Button delBut;
        ///////
        ImageButton menuup;
        ImageButton notesbut;


        public CardViewHolder(View itemView) {
            super(itemView);
            name = (TextView) itemView.findViewById(R.id.name);
            status = (TextView) itemView.findViewById(R.id.statusup);
            startdate = (TextView) itemView.findViewById(R.id.startdate);
            startpoint = (TextView) itemView.findViewById(R.id.startpoint);
            endpoint = (TextView) itemView.findViewById(R.id.endpoint);
            reps = (TextView) itemView.findViewById(R.id.repsup);
            startbut = itemView.findViewById(R.id.startbutUp);
//            notes = itemView.findViewById(R.id.notesup);
//            addNotes = itemView.findViewById(R.id.addnotesbut);
//            edit = itemView.findViewById(R.id.editbut);
//            cancel = itemView.findViewById(R.id.cancelbut);
//            delBut = itemView.findViewById(R.id.delbutup);
            menuup = itemView.findViewById(R.id.menuup);
            notesbut = itemView.findViewById(R.id.notesshow);

        }
    }

}