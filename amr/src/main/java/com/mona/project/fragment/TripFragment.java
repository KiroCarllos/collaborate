package com.mona.project.fragment;

import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.places.ui.PlaceAutocompleteFragment;
import com.google.android.gms.location.places.ui.PlaceSelectionListener;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.libraries.places.api.model.Place;
import com.google.android.libraries.places.api.net.PlacesClient;
import com.google.android.libraries.places.widget.Autocomplete;
import com.google.android.libraries.places.widget.AutocompleteActivity;
import com.google.android.libraries.places.widget.model.AutocompleteActivityMode;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.mona.project.R;
import com.google.android.libraries.places.api.Places;
import com.mona.project.SQL_DB;
import com.mona.project.TripDetails;
import com.mona.project.model.Trip;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;
import java.util.zip.Inflater;

import static android.app.Activity.RESULT_OK;

public class TripFragment extends Fragment implements View.OnClickListener {
    EditText edtxtTripName, edtxtStartPoint, edtxtEndPoint,etNewNote;
    TextView txtDate, txtTime, tvAddNotes;
    Button buAdd,btnNewNote;
    ImageView datePicker, timePicker;
    Spinner spinner_repetition, spinner_type;
    String repeatition, type;
    ListView lvNotes;
    List<String> notes;
    ArrayAdapter<String> arrayAdapter;

    DatabaseReference myRef;
    long id;
    SQL_DB sqlDb = new SQL_DB(getContext());

    String apiKey = getString(R.string.api_key);



    // Create a new Places client instance.
    PlacesClient placesClient = Places.createClient(requireContext());

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Places.initialize(requireContext(), "AIzaSyBhU7FNWT3H-T4Jjmx7R-CZx4liUqVKcFY");
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        final View tripView = inflater.inflate(R.layout.fragment_trip, container, false);
        edtxtTripName = tripView.findViewById(R.id.editTextTripName);
        edtxtStartPoint = tripView.findViewById(R.id.editTextStartPoint);
        edtxtEndPoint = tripView.findViewById(R.id.editTextEndPoint);
        txtDate = tripView.findViewById(R.id.textDate);
        txtTime = tripView.findViewById(R.id.textTime);
        tvAddNotes = tripView.findViewById(R.id.tvAddNotes);
        buAdd = tripView.findViewById(R.id.buAdd);
        datePicker = tripView.findViewById(R.id.datePicker);
        timePicker = tripView.findViewById(R.id.timePicker);
        spinner_repetition = tripView.findViewById(R.id.spinner_repetition);
        spinner_type = tripView.findViewById(R.id.spinner_type);
        lvNotes = tripView.findViewById(R.id.lvNotes);

        notes=new ArrayList<>();
        arrayAdapter=new ArrayAdapter<>(getActivity(),R.layout.note_list,notes);
        lvNotes=tripView.findViewById(R.id.lvNotes);
        lvNotes.setAdapter(arrayAdapter);
        etNewNote=tripView.findViewById(R.id.etNewNote);
        btnNewNote=tripView.findViewById(R.id.btnNewNote);
        btnNewNote.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(TextUtils.isEmpty(etNewNote.getText().toString())){
                    Toast.makeText(getActivity(),"This is empty", Toast.LENGTH_SHORT).show();
                }else{
                    notes.add(etNewNote.getText().toString());
                    arrayAdapter.notifyDataSetChanged();
                    etNewNote.setText("");}
            }
        });

        buAdd.setOnClickListener(this);

        id = 0;
        myRef = FirebaseDatabase.getInstance().getReference(FirebaseAuth.getInstance().getCurrentUser().getUid()).child("MyTrips");
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.exists()) {
                    id = (snapshot.getChildrenCount());
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

        ArrayList<String> repeatArray = new ArrayList<>();
        repeatArray.add("No Repeat");
        repeatArray.add("Daily");
        repeatArray.add("Weekly");
        repeatArray.add("Monthly");
        ArrayAdapter<String> repeatAdapter = new ArrayAdapter<String>(tripView.getContext(), android.R.layout.simple_spinner_item, repeatArray);
        repeatAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner_repetition.setAdapter(repeatAdapter);
        spinner_repetition.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                //TODO repeatSelection
                repeatition = parent.getItemAtPosition(position).toString();
                Toast.makeText(parent.getContext(), "Selected: " + repeatition, Toast.LENGTH_LONG).show();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });
        ArrayList<String> typeArray = new ArrayList<>();
        typeArray.add("One Way");
        typeArray.add("Round");
        ArrayAdapter<String> typeAdapter = new ArrayAdapter<String>(tripView.getContext(), android.R.layout.simple_spinner_item, typeArray);
        typeAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner_type.setAdapter(typeAdapter);
        spinner_type.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                //TODO typeSelection
                type = parent.getItemAtPosition(position).toString();
                Toast.makeText(parent.getContext(), "Selected: " + type, Toast.LENGTH_LONG).show();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });
        timePicker.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int mHour, mMinute;
                // Get Current Time
                final Calendar c = Calendar.getInstance();
                mHour = c.get(Calendar.HOUR_OF_DAY);
                mMinute = c.get(Calendar.MINUTE);

                // Launch Time Picker Dialog
                TimePickerDialog timePickerDialog = new TimePickerDialog(tripView.getContext(),
                        new TimePickerDialog.OnTimeSetListener() {
                            @Override
                            public void onTimeSet(TimePicker view, int hourOfDay,
                                                  int minute) {
                                txtTime.setText(hourOfDay + ":" + minute);
                            }
                        }, mHour, mMinute, false);
                timePickerDialog.show();
            }
        });

        datePicker.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int mYear, mMonth, mDay;
                // Get Current Date
                final Calendar c = Calendar.getInstance();
                mYear = c.get(Calendar.YEAR);
                mMonth = c.get(Calendar.MONTH);
                mDay = c.get(Calendar.DAY_OF_MONTH);
                DatePickerDialog datePickerDialog = new DatePickerDialog(tripView.getContext(),
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker datePicker, int year, int monthOfYear, int dayOfMonth) {
                                txtDate.setText(dayOfMonth + "-" + (monthOfYear + 1) + "-" + year);
                            }
                        }, mYear, mMonth, mDay);
                datePickerDialog.show();
            }
        });

        //getApplicationContext()
        edtxtStartPoint.setFocusable(false);
        edtxtStartPoint.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                List<Place.Field> placeFields = Arrays.asList(Place.Field.ID, Place.Field.NAME);
                Intent intent = new Autocomplete.IntentBuilder(
                        AutocompleteActivityMode.OVERLAY, placeFields)
                        .build(requireContext());
                startActivityForResult(intent, 100);
            }
        });
        edtxtEndPoint.setFocusable(false);
        edtxtEndPoint.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                List<Place.Field> placeFields = Arrays.asList(Place.Field.ID, Place.Field.NAME);
                Intent intent = new Autocomplete.IntentBuilder(
                        AutocompleteActivityMode.OVERLAY, placeFields)
                        .build(requireContext());
                startActivityForResult(intent, 101);
            }
        });
        return tripView;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 100 && resultCode == RESULT_OK) {
            Place place = Autocomplete.getPlaceFromIntent(data);
            edtxtStartPoint.setText(place.getAddress());
        } else if (requestCode == 101 && resultCode == RESULT_OK) {
            Place place = Autocomplete.getPlaceFromIntent(data);
            edtxtEndPoint.setText(place.getAddress());
        } else if (resultCode == AutocompleteActivity.RESULT_ERROR) {
            // TODO: Handle the error.
            Status status = Autocomplete.getStatusFromIntent(data);
            //ast.makeText(tripView.getContext(), status.getStatusMessage(), Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.buAdd:
                addTrip();
                break;
        }
    }

    private void addTrip() {
        Trip trip = new Trip();
        trip.setTripName(edtxtTripName.getText().toString().trim());
        trip.setStartPoint(edtxtStartPoint.getText().toString().trim());
        trip.setEndPoint(edtxtEndPoint.getText().toString().trim());
        trip.setDate(txtDate.getText().toString().trim());
        trip.setTime(txtTime.getText().toString().trim());
        trip.setTripType(type);
        trip.setTripStatues("UpComming");
        trip.setTripRepeat(repeatition);
        trip.setNotes(notes);
        trip.setTripId(String.valueOf(id + 1));
        myRef.child(String.valueOf(id + 1)).setValue(trip).addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Toast.makeText(getContext(), "Trip Created", Toast.LENGTH_SHORT).show();
                    Log.i("TripTAG", "createtrip:success");
                } else {
                    Log.i("TripTAG", "createtrip:failure", task.getException());
                    Toast.makeText(getContext(), "Create Trip failed.", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    public void saveIntoDB() {
        String tripName = edtxtTripName.getText().toString();
        String startPoint = edtxtStartPoint.getText().toString();
        String endPoint = edtxtEndPoint.getText().toString();
        String date = txtDate.getText().toString();
        String time = txtTime.getText().toString();
        String tripType = type;
        String tripRepeatition = repeatition;
        Boolean result = sqlDb.insert_data(tripName, startPoint, endPoint, date, time, tripType, tripRepeatition);
        if (result == true) {
            Toast.makeText(getContext(), "Data Inserted", Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(getContext(), "Data Not Inserted", Toast.LENGTH_LONG).show();
        }
    }
}
