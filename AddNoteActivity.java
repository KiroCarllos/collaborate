package com.example.delllaptop.projone;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.example.delllaptop.projone.DTO.Trip;

import java.io.DataInputStream;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

public class AddNoteActivity extends AppCompatActivity{

    LinearLayout Layout1,Layout2,Layout3,Layout4,Layout5,Layout6,Layout7,Layout8,Layout9,Layout10;
    Button addNote;
    Button add1,add2,add3,add4,add5,add6,add7,add8,add9,add10;
    Button cancel1,cancel2,cancel3,cancel4,cancel5,cancel6,cancel7,cancel8,cancel9,cancel10;
    EditText edit1,edit2,edit3,edit4,edit5,edit6,edit7,edit8,edit9,edit10;
    int i;
    SharedPreferences saving;
    public static final String saveData="NewData";
    public static final String newLogin="NewLogin";
    String user;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_note);
        Layout1=findViewById(R.id.addnoteItem1);
        Layout2=findViewById(R.id.addnoteItem2);
        Layout3=findViewById(R.id.addnoteItem3);
        Layout4=findViewById(R.id.addnoteItem4);
        Layout5=findViewById(R.id.addnoteItem5);
        Layout6=findViewById(R.id.addnoteItem6);
        Layout7=findViewById(R.id.addnoteItem7);
        Layout8=findViewById(R.id.addnoteItem8);
        Layout9=findViewById(R.id.addnoteItem9);
        Layout10=findViewById(R.id.addnoteItem10);
        addNote=findViewById(R.id.AddNotebut);
        add1=findViewById(R.id.ItemAddNoteBtn1);
        add2=findViewById(R.id.ItemAddNoteBtn2);
        add3=findViewById(R.id.ItemAddNoteBtn3);
        add4=findViewById(R.id.ItemAddNoteBtn4);
        add5=findViewById(R.id.ItemAddNoteBtn5);
        add6=findViewById(R.id.ItemAddNoteBtn6);
        add7=findViewById(R.id.ItemAddNoteBtn7);
        add8=findViewById(R.id.ItemAddNoteBtn8);
        add9=findViewById(R.id.ItemAddNoteBtn9);
        add10=findViewById(R.id.ItemAddNoteBtn10);
        cancel1=findViewById(R.id.ItemDelNoteBtn1);
        cancel2=findViewById(R.id.ItemDelNoteBtn2);
        cancel3=findViewById(R.id.ItemDelNoteBtn3);
        cancel4=findViewById(R.id.ItemDelNoteBtn4);
        cancel5=findViewById(R.id.ItemDelNoteBtn5);
        cancel6=findViewById(R.id.ItemDelNoteBtn6);
        cancel7=findViewById(R.id.ItemDelNoteBtn7);
        cancel8=findViewById(R.id.ItemDelNoteBtn8);
        cancel9=findViewById(R.id.ItemDelNoteBtn9);
        cancel10=findViewById(R.id.ItemDelNoteBtn10);
        edit1=findViewById(R.id.addNoteText1);
        edit2=findViewById(R.id.addNoteText2);
        edit3=findViewById(R.id.addNoteText3);
        edit4=findViewById(R.id.addNoteText4);
        edit5=findViewById(R.id.addNoteText5);
        edit6=findViewById(R.id.addNoteText6);
        edit7=findViewById(R.id.addNoteText7);
        edit8=findViewById(R.id.addNoteText8);
        edit9=findViewById(R.id.addNoteText9);
        edit10=findViewById(R.id.addNoteText10);
        saving=getSharedPreferences(saveData,0);
        user = saving.getString("user", "null");
        Log.i("user",user);

        final ArrayList<String>myNotes=new ArrayList();

        cancel1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit1.setText("empty");
            }
        });
        cancel2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit2.setText("empty");
            }
        });
        cancel3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit3.setText("empty");
            }
        });
        cancel4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit4.setText("empty");
            }
        });
        cancel5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit5.setText("empty");
            }
        });
        cancel6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit6.setText("empty");
            }
        });
        cancel7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit7.setText("empty");
            }
        });
        cancel8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit8.setText("empty");
            }
        });
        cancel9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit9.setText("empty");
            }
        });
        cancel10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit10.setText("empty");
            }
        });

        add1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout2.setVisibility(View.VISIBLE);
            }
        });

        add2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout3.setVisibility(View.VISIBLE);
            }
        });

        add3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout4.setVisibility(View.VISIBLE);

            }
        });

        add4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout5.setVisibility(View.VISIBLE);
            }
        });

        add5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout6.setVisibility(View.VISIBLE);
            }
        });

        add6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout7.setVisibility(View.VISIBLE);
            }
        });

        add7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout8.setVisibility(View.VISIBLE);
            }
        });

        add8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout9.setVisibility(View.VISIBLE);
            }
        });

        add9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout10.setVisibility(View.VISIBLE);
            }
        });

        add10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });

        addNote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myNotes.clear();
                if(!edit1.getText().toString().equals("empty") &&!edit1.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit1.getText().toString()))
                    {
                        myNotes.add(edit1.getText().toString());
                    }

                }
                if(!edit2.getText().toString().equals("empty") &&!edit2.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit2.getText().toString()))
                    {
                        myNotes.add(edit2.getText().toString());
                    }
                }
                if(!edit3.getText().toString().equals("empty") &&!edit3.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit3.getText().toString()))
                    {
                        myNotes.add(edit3.getText().toString());
                    }
                }
                if(!edit4.getText().toString().equals("empty") &&!edit4.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit4.getText().toString()))
                    {
                        myNotes.add(edit4.getText().toString());
                    }
                }
                if(!edit5.getText().toString().equals("empty") &&!edit5.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit5.getText().toString()))
                    {
                        myNotes.add(edit5.getText().toString());
                    }
                }
                if(!edit6.getText().toString().equals("empty") &&!edit6.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit6.getText().toString()))
                    {
                        myNotes.add(edit6.getText().toString());
                    }
                }
                if(!edit7.getText().toString().equals("empty") &&!edit7.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit7.getText().toString()))
                    {
                        myNotes.add(edit7.getText().toString());
                    }
                }
                if(!edit8.getText().toString().equals("empty") &&!edit8.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit8.getText().toString()))
                    {
                        myNotes.add(edit8.getText().toString());
                    }

                }
                if(!edit9.getText().toString().equals("empty") &&!edit9.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit9.getText().toString()))
                    {
                        myNotes.add(edit9.getText().toString());
                    }
                }
                if(!edit10.getText().toString().equals("empty") &&!edit10.getText().toString().isEmpty())
                {
                    if(!myNotes.contains(edit10.getText().toString()))
                    {
                        myNotes.add(edit10.getText().toString());
                    }
                }
//                for(String k:myNotes)
//                {
//                    Log.i("res",k);
//                }
                Intent intent = getIntent();
                int trip_id = intent.getIntExtra("trip_id",0);

                SQLAdapter adapteeer = new SQLAdapter(view.getContext());
                if(!myNotes.isEmpty() && trip_id!=0) {
                    for (int j = 0; j < myNotes.size(); j++) {
                        adapteeer.insertNote(myNotes.get(j), trip_id);
                    }
                }
                ArrayList<Trip> trips = adapteeer.retrieveTrips(user);
                for (Trip trip : trips) {
                if(trip.getId()==trip_id){
                    DateFormat format = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                    DateFormat formate2 = new SimpleDateFormat("hh:mm");
                    Calendar myCal = Calendar.getInstance();

                    Date date2= null;
                    try {
                        Date myTime = formate2.parse(trip.getSt());
                        date2 = format.parse(trip.getSd());
                        Log.i("aya", String.valueOf(myCal.getTime()));
                        myCal.setTime(date2);
                        myCal.set(Calendar.HOUR_OF_DAY,myTime.getHours());
                        myCal.set(Calendar.MINUTE,myTime.getMinutes());
                        AlarmManager myAlarm =(AlarmManager) AddNoteActivity.this.getSystemService(Context.ALARM_SERVICE);
                        Intent i = new Intent(AddNoteActivity.this, AlertReciever.class);
                        Bundle bundle = new Bundle();
                        Log.i("myTripnotes",trip.getNotes()+"");
                        bundle.putSerializable("trip",trip);
                        i.putExtra("bundle",bundle);
                        PendingIntent pi = PendingIntent.getBroadcast(AddNoteActivity.this, trip.getId(), i, PendingIntent.FLAG_UPDATE_CURRENT);
                        myAlarm.set(AlarmManager.RTC_WAKEUP,myCal.getTimeInMillis(),pi);
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }

                }
            }
                finish();
            }
        });
    }
}