package com.mona.project;

import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.PopupMenu;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.recyclerview.widget.RecyclerView;

import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;
import com.mona.project.model.Trip;

import java.util.List;

public class MyAdapter extends FirebaseRecyclerAdapter<Trip, MyAdapter.ViewHolder> {
    List<Trip> notes;
    Context context;

    public MyAdapter(@NonNull FirebaseRecyclerOptions<Trip> options) {
        super(options);
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.row_layout, parent, false);
        ViewHolder holder = new ViewHolder(view);
        return holder;
    }

    @Override
    protected void onBindViewHolder(@NonNull final ViewHolder viewHolder, int i, @NonNull final Trip trip) {
        viewHolder.tvTripName.setText(trip.getTripName());
        viewHolder.tvStartPoint.setText(trip.getStartPoint());
        viewHolder.tvEndPoint.setText(trip.getEndPoint());
        viewHolder.tvDate.setText(trip.getDate());
        viewHolder.tvTime.setText(trip.getTime());
        viewHolder.tvStatues.setText(trip.getTripStatues());
        viewHolder.tvType.setText(trip.getTripType());
        viewHolder.tvTripId.setText(trip.getTripId());
        notes.add();
        context=(AppCompatActivity) viewHolder.btnStartTrip.getContext();
        viewHolder.btnStartTrip.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Uri gmIntentUri=Uri.parse("https://www.google.co.in/maps/dir/"+viewHolder.tvStartPoint.getText().toString()
                        +"/"+viewHolder.tvEndPoint.getText().toString());
                Intent mapIntent=new Intent(Intent.ACTION_VIEW,gmIntentUri);
                mapIntent.setPackage("com.google.android.apps.maps");
                mapIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(mapIntent);
            }
        });
        viewHolder.ivOptions.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(final View view) {
                PopupMenu popupMenu = new PopupMenu(view.getContext(), viewHolder.ivOptions);
                popupMenu.inflate(R.menu.menu);
                popupMenu.setOnMenuItemClickListener(new PopupMenu.OnMenuItemClickListener() {
                    @Override
                    public boolean onMenuItemClick(MenuItem menuItem) {
                        switch (menuItem.getItemId()) {
                            case R.id.edit:
                                TripDetails tripDetails = new TripDetails();
                                Bundle bundle = new Bundle();
                                bundle.putString("name", viewHolder.tvTripName.getText().toString());
                                bundle.putString("start", viewHolder.tvStartPoint.getText().toString());
                                bundle.putString("end", viewHolder.tvEndPoint.getText().toString());
                                bundle.putString("date", viewHolder.tvDate.getText().toString());
                                bundle.putString("time", viewHolder.tvTime.getText().toString());
                                bundle.putString("statues", viewHolder.tvStatues.getText().toString());
                                bundle.putString("type", viewHolder.tvType.getText().toString());
                                bundle.putString("id", viewHolder.tvTripId.getText().toString());
                                tripDetails.setArguments(bundle);
                                AppCompatActivity activity = (AppCompatActivity) view.getContext();
                                activity.getSupportFragmentManager().beginTransaction()
                                        .add(R.id.container, tripDetails).addToBackStack(null).commit();
                                break;
                            case R.id.delete:
                                AlertDialog.Builder alert = new AlertDialog.Builder((AppCompatActivity) view.getContext());
                                alert.setTitle("Delete Trip")
                                        .setMessage("Want to delete this Trip")
                                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                                            @Override
                                            public void onClick(DialogInterface dialogInterface, int i) {
                                                FirebaseDatabase.getInstance()
                                                        .getReference(FirebaseAuth.getInstance().getCurrentUser().getUid()).child("MyTrips")
                                                        .child(viewHolder.tvTripId.getText().toString()).removeValue();
                                            }
                                        })
                                        .setNegativeButton("No", new DialogInterface.OnClickListener() {
                                            @Override
                                            public void onClick(DialogInterface dialogInterface, int i) {

                                            }
                                        }).create().show();
                                break;
                        }
                        return false;
                    }
                });
                popupMenu.show();
            }
        });
    }

//    @Override
//    public int getItemCount() {
//        return trips.size();
//    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView tvTripName, tvStartPoint, tvEndPoint, tvDate, tvTime, tvStatues, tvType, tvTripId;
        ConstraintLayout expand;
        ImageView ivOptions;
        Button btnStartTrip;

        public ViewHolder(View view) {
            super(view);
            tvTripName = (TextView) view.findViewById(R.id.tvPastTripName);
            tvStartPoint = (TextView) view.findViewById(R.id.tvStartPoint);
            tvEndPoint = (TextView) view.findViewById(R.id.tvEndPoint);
            tvDate = (TextView) view.findViewById(R.id.tvDate);
            tvTime = (TextView) view.findViewById(R.id.tvTime);
            tvStatues = (TextView) view.findViewById(R.id.tvStatues);
            tvType = (TextView) view.findViewById(R.id.tvType);
            tvTripId = (TextView) view.findViewById(R.id.tvTripId);
            btnStartTrip = (Button) view.findViewById(R.id.btnStartTrip);
            ivOptions = (ImageView) view.findViewById(R.id.ivDelete);
            expand = (ConstraintLayout) view.findViewById(R.id.expandLayout);
            tvTripName.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (expand.getVisibility() == View.GONE) {
                        expand.setVisibility(View.VISIBLE);
                    } else {
                        expand.setVisibility(View.GONE);
                    }
                }
            });
        }
    }
}
