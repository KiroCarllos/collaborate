package com.mona.project;

import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import static android.support.v4.media.session.MediaControllerCompatApi21.getPackageName;

public class TripDetails extends Fragment {
    EditText etDetailsTripName, etDetailsStartPoint, etDetailsEndPoint, etDetailsNotes, etDetailsDate, etDetailsTime, etDetailsTripStatues;
    CheckBox cbDetailsRound, cbDetailsDone;
    Button btnDetailsStartTrip, btnDetailsEdit;
    String tripName, startPoint, endPoint, date, time, statues, type, id, typeChanged,statuesChanged;
    DatabaseReference reference;

    private static final int DRAW_OVER_OTHER_APP_PERMISSION = 123;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.trip_details, container, false);
        etDetailsTripName = view.findViewById(R.id.etDetailsTripName);
        etDetailsStartPoint = view.findViewById(R.id.etDetailsStartPoint);
        etDetailsEndPoint = view.findViewById(R.id.etDetailsEndPoint);
        etDetailsNotes = view.findViewById(R.id.etDetailsNotes);
        etDetailsDate = view.findViewById(R.id.etDetailsDate);
        etDetailsTime = view.findViewById(R.id.etDetailsTime);
        etDetailsTripStatues = view.findViewById(R.id.etDetailsTripStatues);
        cbDetailsRound = view.findViewById(R.id.cbDetailsRound);
        cbDetailsDone = view.findViewById(R.id.cbDetailsDone);
        btnDetailsStartTrip = view.findViewById(R.id.btnDetailsStartTrip);
        btnDetailsEdit = view.findViewById(R.id.btnDetailsEdit);

        askForSystemOverlayPermission();

        Bundle bundle = getArguments();
        tripName = bundle.getString("name");
        startPoint = bundle.getString("start");
        endPoint = bundle.getString("end");
        date = bundle.getString("date");
        time = bundle.getString("time");
        statues = bundle.getString("statues");
        type = bundle.getString("type");
        id = bundle.getString("id");
        etDetailsTripName.setText(tripName);
        etDetailsStartPoint.setText(startPoint);
        etDetailsEndPoint.setText(endPoint);
        etDetailsDate.setText(date);
        etDetailsTime.setText(time);
        //etDetailsNotes.setText(bundle.getString("notes"));
        etDetailsTripStatues.setText(statues);

        btnDetailsStartTrip.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startTrip(startPoint,endPoint);
            }
        });

        reference = FirebaseDatabase.getInstance().getReference(FirebaseAuth.getInstance().getCurrentUser().getUid())
                .child("MyTrips").child(id);

        if (type.equals("Round")) {
            cbDetailsRound.setChecked(true);
        }

        if (statues.equals("Done")){
            cbDetailsDone.setChecked(true);
        }


        cbDetailsRound.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (cbDetailsRound.isChecked()) {
                    typeChanged = "Round";
                } else if (!cbDetailsRound.isChecked()) {
                    typeChanged = "One Way";
                }
            }
        });

        cbDetailsDone.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (cbDetailsDone.isChecked()){
                    statuesChanged="Done";
                    cbDetailsDone.setEnabled(false);
                }else{
                    cbDetailsDone.setEnabled(true);
                }
            }
        });

        btnDetailsEdit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                /*if (isNameChanged() || isStartPointChanged() || isEndPointChanged()
                        || isDateChanged() || isTimeChanged() || isStatuesChanged() || isTypeChanged()) {
                    Toast.makeText(getContext(), "Data Updated", Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(getContext(), "Update Failed", Toast.LENGTH_LONG).show();
                }*/


            }
        });

        return view;
    }

    /*private boolean isNameChanged() {
        if (!tripName.equals(etDetailsTripName.getText().toString().trim())) {
            reference.child(id).child("tripName").setValue(etDetailsTripName.getText().toString().trim());
            tripName = etDetailsTripName.getText().toString().trim();
            return true;
        } else {
            return false;
        }
    }

    private boolean isStartPointChanged() {
        if (!startPoint.equals(etDetailsStartPoint.getText().toString().trim())) {
            reference.child(id).child("startPoint").setValue(etDetailsStartPoint.getText().toString().trim());
            startPoint = etDetailsStartPoint.getText().toString().trim();
            return true;
        } else {
            return false;
        }
    }

    private boolean isEndPointChanged() {
        if (!endPoint.equals(etDetailsEndPoint.getText().toString().trim())) {
            reference.child(id).child("endPoint").setValue(etDetailsEndPoint.getText().toString().trim());
            endPoint = etDetailsEndPoint.getText().toString().trim();
            return true;
        } else {
            return false;
        }
    }

    private boolean isDateChanged() {
        if (!date.equals(etDetailsDate.getText().toString().trim())) {
            reference.child(id).child("date").setValue(etDetailsDate.getText().toString().trim());
            date = etDetailsDate.getText().toString().trim();
            return true;
        } else {
            return false;
        }
    }

    private boolean isTimeChanged() {
        if (!time.equals(etDetailsTime.getText().toString().trim())) {
            reference.child(id).child("time").setValue(etDetailsTime.getText().toString().trim());
            time = etDetailsTime.getText().toString().trim();
            return true;
        } else {
            return false;
        }
    }

    private boolean isStatuesChanged() {
        if (!statues.equals(statuesChanged)) {
            reference.child(id).child("tripStatues").setValue(statuesChanged);
            statues = statuesChanged;
            return true;
        } else {
            return false;
        }
    }

    private boolean isTypeChanged() {
        if (!type.equals(typeChanged)) {
            reference.child(id).child("tripType").setValue(typeChanged);
            type = typeChanged;
            return true;
        } else {
            return false;
        }
    }*/

    public void startTrip(String s,String d){
        Uri gmIntentUri=Uri.parse("https://www.google.co.in/maps/dir/"+s+"/"+d);
        Intent mapIntent=new Intent(Intent.ACTION_VIEW,gmIntentUri);
        mapIntent.setPackage("com.google.android.apps.maps");
        mapIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(mapIntent);

        requireActivity().startService(new Intent(requireActivity(), FloatingIconService.class));
    }
    private void askForSystemOverlayPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && !Settings.canDrawOverlays(requireActivity().getApplicationContext())) {
            //If the draw over permission is not available to open the settings screen
            //to grant permission.
            Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                    Uri.parse("package:" + requireActivity().getPackageName()));
            startActivityForResult(intent, DRAW_OVER_OTHER_APP_PERMISSION);
        }
    }
        @Override
    public void onPause() {
        super.onPause();
        // To prevent starting the service if the required permission is NOT granted.
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M || Settings.canDrawOverlays(requireActivity().getApplicationContext())) {
           requireActivity().startService(new Intent(requireActivity(), FloatingIconService.class).putExtra("activity_background", true));
           requireActivity().finish();
        } else {

        }
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == DRAW_OVER_OTHER_APP_PERMISSION) {

            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                if (!Settings.canDrawOverlays(requireActivity().getApplicationContext())) {
                    //Permission is not available. Display error text.
                    Toast.makeText(requireActivity(), "Premission not granted", Toast.LENGTH_SHORT).show();
                    requireActivity().finish();
                }
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }
}