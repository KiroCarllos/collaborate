package com.mona.project.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.android.libraries.places.api.Places;
import com.google.android.libraries.places.api.net.PlacesClient;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.mona.project.MyAdapter;
import com.mona.project.R;
import com.mona.project.model.Trip;

import java.util.ArrayList;
import java.util.List;

public class UpCommingFragment extends Fragment {
    RecyclerView recyclerUpComming;
    MyAdapter adapter;
    RecyclerView.LayoutManager manager;
    DatabaseReference reference;
    List<Trip> tripsList = new ArrayList<>();






    @Override
    public void onStart() {
        super.onStart();
        adapter.startListening();
    }

    @Override
    public void onStop() {
        super.onStop();
        adapter.startListening();
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.upcomming_fragment, container, false);
        FloatingActionButton fab = view.findViewById(R.id.fabAdd);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TripFragment fragment = new TripFragment();
                FragmentManager fm = getFragmentManager();
                fm.beginTransaction().add(R.id.container, fragment).addToBackStack(null).commit();
            }
        });

        recyclerUpComming = view.findViewById(R.id.recyclerUpComming);
        recyclerUpComming.setHasFixedSize(true);
        manager = new LinearLayoutManager(getContext());
        recyclerUpComming.setLayoutManager(manager);
//        adapter = new MyAdapter(tripsList);
//        recyclerUpComming.setAdapter(adapter);

        /*reference = FirebaseDatabase.getInstance().getReference(FirebaseAuth.getInstance().getCurrentUser().getUid());
        reference.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                for (DataSnapshot ds : snapshot.getChildren()) {
                    Trip trips = ds.getValue(Trip.class);
                    tripsList.add(trips);
                }
                adapter = new MyAdapter(tripsList);
                recyclerUpComming.setAdapter(adapter);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });*/

        FirebaseRecyclerOptions<Trip> options=new FirebaseRecyclerOptions.Builder<Trip>()
                .setQuery(FirebaseDatabase.getInstance().getReference(FirebaseAuth.getInstance().getCurrentUser().getUid())
                        .child("MyTrips"),Trip.class)
                .build();
        adapter=new MyAdapter(options);
        recyclerUpComming.setAdapter(adapter);

        /*tripsList.add(new Trip("work", "upcomming"));
        tripsList.add(new Trip("school", "upcomming"));
        tripsList.add(new Trip("college", "upcomming"));
        tripsList.add(new Trip("vacation", "upcomming"));
        tripsList.add(new Trip("nana", "upcomming"));
        tripsList.add(new Trip("go home", "upcomming"));
        tripsList.add(new Trip("work", "upcomming"));
        tripsList.add(new Trip("school", "upcomming"));
        tripsList.add(new Trip("college", "upcomming"));
        tripsList.add(new Trip("vacation", "upcomming"));
        tripsList.add(new Trip("nana", "upcomming"));
        tripsList.add(new Trip("go home", "upcomming"));
        tripsList.add(new Trip("work", "upcomming"));
        tripsList.add(new Trip("school", "upcomming"));
        tripsList.add(new Trip("college", "upcomming"));
        tripsList.add(new Trip("vacation", "upcomming"));
        tripsList.add(new Trip("nana", "upcomming"));
        tripsList.add(new Trip("go home", "upcomming"));
        tripsList.add(new Trip("work", "upcomming"));
        tripsList.add(new Trip("school", "upcomming"));
        tripsList.add(new Trip("college", "upcomming"));
        tripsList.add(new Trip("vacation", "upcomming"));
        tripsList.add(new Trip("nana", "upcomming"));
        tripsList.add(new Trip("go home", "upcomming"));*/

        return view;
    }
}
