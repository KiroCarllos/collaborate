package com.example.delllaptop.projone;

import android.*;
import android.Manifest;
import android.app.AlarmManager;
import android.app.DatePickerDialog;
import android.app.PendingIntent;
import android.app.TimePickerDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.provider.Settings;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;


import com.example.delllaptop.projone.DTO.Trip;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.places.Place;
import com.google.android.gms.location.places.ui.PlaceAutocompleteFragment;
import com.google.android.gms.location.places.ui.PlaceSelectionListener;
import com.google.android.gms.maps.model.LatLng;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Locale;
import java.util.Map;

public class AddTripActivity extends AppCompatActivity implements View.OnClickListener,roundTripInt{

    private static final String TAG = "dah error !";
    Button btnTimePicker, btnDatePicker, Next,btnTimePicker2, btnDatePicker2;
    TextView txtDate,txtTime,txtDate2,txtTime2;
    EditText Name;
    FragmentManager mgr;
    private int mYear,mMonth,mDay,mHour,mMin;
    String name, spoint="", sLat="", sLong="", epoint="", eLat="", eLong="", status, sdate,totaltime,rdate,rtime;
    double mysLat, mysLong, myeLat, myeLong;
    int rep, position,position2;
    Spinner spinner1,spinner2;
    roundFragment myFrag;
    roundFragment r;
    SharedPreferences saving;
    public static final String saveData="NewData";
    String user;
    HashMap<Integer,Date> myData = new HashMap<Integer, Date>();
    ArrayList<PendingIntent> allPendingIntent;
    int hours,min;
    int num;
    Date date;
    Date date2;
    Date myTime;
    Date myDateCheck;
    int returnhour;
    int returnmin;
    Boolean inserted2 = true;
    boolean flagfrag = true;
    private FirebaseAuth mAuth;
    private DatabaseReference db;
    private FirebaseUser fuser;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        if(!(new CheckPermissions(this).checkInternet())){
//            finish();
//        }
        if(savedInstanceState!=null)
        flagfrag = savedInstanceState.getBoolean("flagfrag");
        setContentView(R.layout.activity_add_trip);
        btnDatePicker = findViewById(R.id.btn_date_add);
        btnTimePicker = findViewById(R.id.btn_time_add);
        txtDate = findViewById(R.id.in_date_add);
        txtTime = findViewById(R.id.in_time_add);
        btnDatePicker.setOnClickListener(this);
        btnTimePicker.setOnClickListener(this);
        Name = findViewById(R.id.Name_add);
        Next = findViewById(R.id.Next_add);
        Next.setOnClickListener(this);
        spinner1 = findViewById(R.id.spinner1_add);
        saving=getSharedPreferences(saveData,0);
        user = saving.getString("user", "null");
//        ///////
//        saving = getApplicationContext().getSharedPreferences(saveData, 0);
//        SharedPreferences.Editor edit = saving.edit();
//        edit.putBoolean("refresh",true);
//        Log.i("user",user);
//        ////////
        spinner1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                position = i;
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinner2 = findViewById(R.id.spinner2_add);
        spinner2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                position2 = i;
                if (position2 == 1 && flagfrag) {
                    myFrag = new roundFragment();
                    mgr = getSupportFragmentManager();
                    FragmentTransaction trans = mgr.beginTransaction();
                    trans.add(R.id.myScrollView_add, myFrag, "myNewFrag");
                    trans.commit();
                    flagfrag = false;
                }
                if (position2 == 0) {
                    if (getSupportFragmentManager().findFragmentByTag("myNewFrag") != null) {
                        getSupportFragmentManager().beginTransaction().remove(getSupportFragmentManager().findFragmentByTag("myNewFrag")).commit();
                        flagfrag=true;
                    }
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });
        if (Build.VERSION.SDK_INT >= 23) {
            if (!Settings.canDrawOverlays(this)) {
                Toast.makeText(this,"Please grant overlay permisssion",Toast.LENGTH_LONG).show();
                Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:" + getPackageName()));
                startActivityForResult(intent, 0);
            }
        }


    }




    @Override
    protected void onStart() {
        super.onStart();
        PlaceAutocompleteFragment autocompleteFragment1 = (PlaceAutocompleteFragment) getFragmentManager().findFragmentById(R.id.place_autocomplete_fragment_add);
        if (autocompleteFragment1 != null)
            autocompleteFragment1.setOnPlaceSelectedListener(new PlaceSelectionListener() {
                @Override
                public void onPlaceSelected(Place place) {
                    // TODO: Get info about the selected place.
                    Log.i(TAG, "Place: " + place.getName());
                    spoint = place.getName().toString();
                    LatLng myLatLong = place.getLatLng();
                    mysLat = myLatLong.latitude;
                    mysLong = myLatLong.longitude;
                    sLat = mysLat + "";
                    sLong = mysLong + "";


                }

                @Override
                public void onError(Status status) {
                    // TODO: Handle the error.
                    Log.i(TAG, "An error occurred: " + status);
                }
            });
        else Toast.makeText(this, "Problem with loading page", Toast.LENGTH_LONG).show();


        PlaceAutocompleteFragment autocompleteFragment2 = (PlaceAutocompleteFragment) getFragmentManager().findFragmentById(R.id.place_autocomplete_fragment2_add);
        if (autocompleteFragment2 != null )
            autocompleteFragment2.setOnPlaceSelectedListener(new PlaceSelectionListener() {
                @Override
                public void onPlaceSelected(Place place) {
                    // TODO: Get info about the selected place./
                    Log.i(TAG, "Place: " + place.getName());
                    //String placeName = place.getName().toString();
                    //  Toast.makeText(MainActivity.this, "the place is "+ placeName ,Toast.LENGTH_SHORT).show();
                    epoint = place.getName().toString();
                    LatLng myLatLong = place.getLatLng();
                    myeLat = myLatLong.latitude;
                    myeLong = myLatLong.longitude;
                    eLat = myeLat + "";
                    eLong = myeLong + "";
                }

                @Override
                public void onError(Status status) {
                    // TODO: Handle the error.
                    Log.i(TAG, "An error occurred: " + status);
                }
            });
        else Toast.makeText(this, "Problem with loading page", Toast.LENGTH_LONG).show();
    }


    @Override
    public void onClick(View view) {
        if (view == btnDatePicker) {
            final Calendar c = Calendar.getInstance();
            mYear = c.get(Calendar.YEAR);
            mMonth = c.get(Calendar.MONTH);
            mDay = c.get(Calendar.DAY_OF_MONTH);

            DatePickerDialog datePickerDialog = new DatePickerDialog(view.getContext(),
                    new DatePickerDialog.OnDateSetListener() {

                        @Override
                        public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                            String myDate = dayOfMonth + "-" + (monthOfYear + 1) + "-" + year;
                            String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                            DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                            try {
                                date = format.parse(timeStamp);
                                myDateCheck = format.parse(myDate);
                            } catch (ParseException e) {
                                e.printStackTrace();
                            }
                            if(myDateCheck.equals(null)) {
                                try {
                                    myDateCheck = format.parse(timeStamp);
                                } catch (ParseException e) {
                                    e.printStackTrace();
                                }
                            }
                            else {
                            if (myDateCheck.before(date)) {
                                Toast.makeText(view.getContext(), "Enter Valid Date", Toast.LENGTH_SHORT).show();
                            } else {
                                txtDate.setText(dayOfMonth + "-" + (monthOfYear + 1) + "-" + year);
                            }
                            }
                        }
                    }, mYear, mMonth, mDay);
            datePickerDialog.show();
        }
        if (view == btnTimePicker) {

            // Get Current Time
            final Calendar c = Calendar.getInstance();
            mHour = c.get(Calendar.HOUR_OF_DAY);
            mMin = c.get(Calendar.MINUTE);

            // Launch Time Picker Dialog
            TimePickerDialog timePickerDialog = new TimePickerDialog(view.getContext(),
                    new TimePickerDialog.OnTimeSetListener() {

                        @Override
                        public void onTimeSet(TimePicker view, int hourOfDay,
                                              int minute) {
                            Calendar myCalInstance = Calendar.getInstance();
                            Calendar myRealCalender = Calendar.getInstance();
                            if(myDateCheck==null){
                                String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                                DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                                try {
                                    myDateCheck = format.parse(timeStamp);
                                } catch (ParseException e) {
                                    e.printStackTrace();
                                }
                            }
                            myRealCalender.setTime(myDateCheck);
                            myRealCalender.set(Calendar.HOUR_OF_DAY,hourOfDay);
                            myRealCalender.set(Calendar.MINUTE,minute);
                            Log.i("time", String.valueOf(myCalInstance.getTime()));
                            Log.i("time", String.valueOf(myRealCalender.getTime()));
                            if((myRealCalender.getTime()).before(myCalInstance.getTime()))
                            {
                                Toast.makeText(view.getContext(),"Enter Valid Time",Toast.LENGTH_SHORT).show();
                            }
                            else {
                                hours = hourOfDay;
                                min = minute;
                                if(hourOfDay<10&&min>=10) {
                                    txtTime.setText("0" + hourOfDay + ":" + minute);
                                }
                                if(hourOfDay<10&&min<10)
                                {
                                    txtTime.setText("0" + hourOfDay + ":"+"0"+ minute);
                                }
                                if(hourOfDay>=10&&min<10)
                                {
                                    txtTime.setText(hourOfDay + ":"+"0"+ minute);
                                }
                                if(hourOfDay>=10&&min>=10)
                                {
                                    txtTime.setText(hourOfDay + ":"+ minute);
                                }

                            }
                        }
                    }, mHour, mMin, false);
            timePickerDialog.show();
        }
        if (view == Next &&  new CheckPermissions(this).checkInternet()){
            if(!Name.getText().toString().isEmpty() && !txtTime.getText().toString().isEmpty() &&
                !sLat.isEmpty() && !eLat.isEmpty()) {

                SQLAdapter adapter = new SQLAdapter(view.getContext());
//            ArrayList<Trip> tripsa = adapter.retrieveTrips();
//            for (Trip trip : tripsa) {
//                long i3 = adapter.deleteTrip(trip.getId());
//                Log.i("count", i3 + "");
//            }


                status = "upcoming";
                name = Name.getText().toString();
                sdate = txtDate.getText().toString();
                totaltime = txtTime.getText().toString();

                if (position == 0)
                    rep = 0;
                if (position == 1)
                    rep = 1;
                if (position == 2)
                    rep = 7;
                if (position == 3)
                    rep = 30;

                if (position2 == 0) {
                    Log.i("insertsql", "done");
                    long i = adapter.insertTrip(name, spoint, sLong, sLat, epoint, eLong, eLat, status, sdate, "null", totaltime, null, rep, user, null);
                    //db.child(auth.getCurrentUser().getUid()).child()

                } else if (position2 == 1) {
                    /////////////////////////
                    DateFormat format = new SimpleDateFormat("dd-MM-yyyy HH:mm", Locale.ENGLISH);
                    Calendar myCalOne = Calendar.getInstance();
                    Calendar myCalTwo = Calendar.getInstance();
                    try {
                        Date dateOne = format.parse(sdate + " " + hours + ":" + min);
                        myCalOne.setTime(dateOne);
//                    myCalOne.set(Calendar.HOUR_OF_DAY,hours);
//                    myCalOne.set(Calendar.MINUTE,min);
                        Date dateTwo = format.parse(rdate + " " + returnhour + ":" + returnmin);
                        myCalTwo.setTime(dateTwo);
//                    myCalTwo.set(Calendar.HOUR_OF_DAY,returnhour);
//                    myCalTwo.set(Calendar.MINUTE,returnmin);
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }

                    if (myCalTwo.before(myCalOne)) {
                        Toast.makeText(this, "Your must insert return date after start date", Toast.LENGTH_SHORT).show();
                        inserted2 = false;
                    } else {
                        Log.i("insertsql", "done");
                        long i = adapter.insertTrip(name, spoint, sLong, sLat, epoint, eLong, eLat, status, sdate, "null", totaltime, null, rep, user, null);
                        long i2 = adapter.insertTrip(name, epoint, eLong, eLat, spoint, sLong, sLat, status, rdate, "null", rtime, null, rep, user, null);
                        inserted2 = true;
                    }
                    ////////////////////////
                }
                ArrayList<Trip> trips = adapter.retrieveTrips(user);
                if (position2 == 0) {
                    int id = trips.get(trips.size() - 1).getId();
                    String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                    DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                    DateFormat formate2 = new SimpleDateFormat("hh:mm");
                    Calendar myCal = Calendar.getInstance();
                    try {
                        myTime = formate2.parse(trips.get(trips.size() - 1).getSt());
                        date = format.parse(timeStamp);
                        date2 = format.parse(trips.get(trips.size() - 1).getSd());
                        Log.i("aya", String.valueOf(myCal.getTime()));
                        myCal.setTime(date2);
                        myCal.set(Calendar.HOUR_OF_DAY, hours);
                        myCal.set(Calendar.MINUTE, min);
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    myData.put(id, date2);
                    ////////////////////////////////////
                    db = FirebaseDatabase.getInstance().getReference();
                    mAuth = FirebaseAuth.getInstance();
                    fuser = FirebaseAuth.getInstance().getCurrentUser();
                    SyncUpload su = new SyncUpload(this,mAuth,db,fuser,trips.get(trips.size() - 1));
                    su.execute();
                    /////////////////////////////////////////
                    //hna h7ot el id bta3 el trip fe el hashmap w el pendding intent
                    AlarmManager myAlarm = (AlarmManager) this.getSystemService(Context.ALARM_SERVICE);
                    Intent i = new Intent(this, AlertReciever.class);
                    Bundle bundle = new Bundle();
                    bundle.putSerializable("trip", trips.get(trips.size() - 1));
                    i.putExtra("bundle", bundle);
                    Log.i("tripalert", trips.get(trips.size() - 1) + "");
                    PendingIntent pi = PendingIntent.getBroadcast(this, id, i, PendingIntent.FLAG_UPDATE_CURRENT);
                    myAlarm.set(AlarmManager.RTC_WAKEUP, myCal.getTimeInMillis(), pi);
                    finish();

                }

                ////////////////////////////////////////////// position 2 /////////////////////////////////////////////////////

                if (position2 == 1 && inserted2) {
                    String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                    DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                    DateFormat formate2 = new SimpleDateFormat("hh:mm");
                    Calendar myCal = Calendar.getInstance();
                    int id = trips.get(trips.size() - 2).getId();

                    try {
                        myTime = formate2.parse(trips.get(trips.size() - 2).getSt());
                        date = format.parse(timeStamp);
                        date2 = format.parse(trips.get(trips.size() - 2).getSd());
                        Log.i("aya", String.valueOf(myCal.getTime()));
                        myCal.setTime(date2);
                        myCal.set(Calendar.HOUR_OF_DAY, hours);
                        myCal.set(Calendar.MINUTE, min);
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    myData.put(id, date2);
                    ////////////////////////////////////
                    db = FirebaseDatabase.getInstance().getReference();
                    mAuth = FirebaseAuth.getInstance();
                    fuser = FirebaseAuth.getInstance().getCurrentUser();
                    SyncUpload su = new SyncUpload(this,mAuth,db,fuser,trips.get(trips.size() - 2));
                    su.execute();
                    /////////////////////////////////////////
                    //hna h7ot el id bta3 el trip fe el hashmap w el pendding intent
                    AlarmManager myAlarm = (AlarmManager) this.getSystemService(Context.ALARM_SERVICE);
                    Intent i = new Intent(this, AlertReciever.class);
                    Bundle bundle = new Bundle();
                    bundle.putSerializable("trip", trips.get(trips.size() - 2));
                    i.putExtra("bundle", bundle);
                    Log.i("tripalert", trips.get(trips.size() - 2) + "");
                    PendingIntent pi = PendingIntent.getBroadcast(this, id, i, PendingIntent.FLAG_UPDATE_CURRENT);
                    myAlarm.set(AlarmManager.RTC_WAKEUP, myCal.getTimeInMillis(), pi);

                    ///////////////////// trip 2 poition 2 ////////////////
                    id = trips.get(trips.size() - 1).getId();

                    try {
                        myTime = formate2.parse(trips.get(trips.size() - 1).getSt());
                        date = format.parse(timeStamp);
                        date2 = format.parse(trips.get(trips.size() - 1).getSd());
                        Log.i("aya", String.valueOf(myCal.getTime()));
                        myCal.setTime(date2);
                        myCal.set(Calendar.HOUR_OF_DAY, myTime.getHours());
                        myCal.set(Calendar.MINUTE, myTime.getMinutes());
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                    myData.put(id, date2);
                    ////////////////////////////////////
                    db = FirebaseDatabase.getInstance().getReference();
                    mAuth = FirebaseAuth.getInstance();
                    fuser = FirebaseAuth.getInstance().getCurrentUser();
                    SyncUpload syncUpload = new SyncUpload(this,mAuth,db,fuser,trips.get(trips.size() - 1));
                    syncUpload.execute();
                    /////////////////////////////////////////
                    //hna h7ot el id bta3 el trip fe el hashmap w el pendding intent
                    AlarmManager myAlarm2 = (AlarmManager) this.getSystemService(Context.ALARM_SERVICE);
                    Intent i2 = new Intent(this, AlertReciever.class);
                    Bundle bundle2 = new Bundle();
                    bundle2.putSerializable("trip", trips.get(trips.size() - 1));
                    i2.putExtra("bundle", bundle2);
                    Log.i("tripalert", trips.get(trips.size() - 1) + "");
                    PendingIntent pi2 = PendingIntent.getBroadcast(this, id, i2, PendingIntent.FLAG_UPDATE_CURRENT);
                    myAlarm2.set(AlarmManager.RTC_WAKEUP, myCal.getTimeInMillis(), pi2);
                    finish();
                }
            }
            else {
                Toast.makeText(this, "Please enter valid information", Toast.LENGTH_SHORT).show();
            }

        }

    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putBoolean("flagfrag",flagfrag);
    }

    @Override
    public void send(String Date, String Time,int hours, int mins) {
        rdate=Date;
        rtime=Time;
        returnhour = hours;
        returnmin = mins;
    }
}
