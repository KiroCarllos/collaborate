package com.example.delllaptop.projone;


import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.SupportActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.TimePicker;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;


public class roundFragment extends Fragment{

    Button btnTimePicker2, btnDatePicker2;
    TextView txtDate2, txtTime2;
    int mYear2,mMonth2,mDay2,mHour2,mMin2;
    int hourday=-1,minday=-1;
    String myDate,myTime="";
    // Intent intent;


    public roundFragment() {
        // Required empty public constructor
    }


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_round, container, false);
        btnDatePicker2 = v.findViewById(R.id.btn_date2);
        btnTimePicker2 = v.findViewById(R.id.btn_time2);
        txtDate2 = v.findViewById(R.id.in_date2);
        txtTime2 = v.findViewById(R.id.in_time2);
        return v;
    }

    @Override
    public void onStart() {
        super.onStart();
        btnDatePicker2.setOnClickListener(new View.OnClickListener()

        {
            @Override
            public void onClick(View view) {
                final Calendar c = Calendar.getInstance();
                mYear2 = c.get(Calendar.YEAR);
                mMonth2 = c.get(Calendar.MONTH);
                mDay2 = c.get(Calendar.DAY_OF_MONTH);
                DatePickerDialog datePickerDialog2 = new DatePickerDialog(view.getContext(),
                        new DatePickerDialog.OnDateSetListener() {

                            @Override
                            public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                                txtDate2.setText(dayOfMonth + "-" + (monthOfYear + 1) + "-" + year);
                                String timeStamp = new SimpleDateFormat("dd-MM-yyyy").format(Calendar.getInstance().getTime());
                                myDate=txtDate2.getText().toString();
                                if(myDate.equals(null)) {
                                    myDate=timeStamp;
                                }
                                if(minday!=-1)
                                ((roundTripInt) getActivity()).send(myDate,myTime,hourday,minday);
//                                 intent = new Intent(getActivity(), AddTripActivity.class);
//                                intent.putExtra("my_Date",myDate);

                            }
                        }, mYear2, mMonth2, mDay2);
                datePickerDialog2.show();
            }
        });

        btnTimePicker2.setOnClickListener(new View.OnClickListener()

        {
            @Override
            public void onClick(View view) {
                // Get Current Time
                final Calendar c = Calendar.getInstance();
                mHour2 = c.get(Calendar.HOUR_OF_DAY);
                mMin2 = c.get(Calendar.MINUTE);

                // Launch Time Picker Dialog
                TimePickerDialog timePickerDialog2 = new TimePickerDialog(view.getContext(),
                        new TimePickerDialog.OnTimeSetListener() {

                            @Override
                            public void onTimeSet(TimePicker view, int hourOfDay,
                                                  int minute) {
                                if(hourOfDay<10&&minute>=10) {
                                    txtTime2.setText("0" + hourOfDay + ":" + minute);
                                }
                                if(hourOfDay<10&&minute<10)
                                {
                                    txtTime2.setText("0" + hourOfDay + ":"+"0"+ minute);
                                }
                                if(hourOfDay>=10&&minute<10)
                                {
                                    txtTime2.setText(hourOfDay + ":"+"0"+ minute);
                                }
                                if(hourOfDay>=10&&minute>=10)
                                {
                                    txtTime2.setText(hourOfDay + ":"+ minute);
                                }
                                myTime=txtTime2.getText().toString();
//                                intent.putExtra("my_Time",myTime);
//                                getActivity().startActivityForResult(intent,0);
                                minday=minute;
                                hourday = hourOfDay;
                                ((roundTripInt) getActivity()).send(myDate,myTime,hourOfDay,minute);
                            }
                        }, mHour2, mMin2, false);
                timePickerDialog2.show();

            }
        });

    }


}
