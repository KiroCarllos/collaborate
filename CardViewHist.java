package com.example.delllaptop.projone;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.Dialog;
import android.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.app.DialogFragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.content.Context;
import android.content.DialogInterface;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.view.animation.TranslateAnimation;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

import com.example.delllaptop.projone.DTO.Trip;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by Dell Laptop on 3/9/2018.
 */

public class CardViewHist extends RecyclerView.Adapter<CardViewHist.CardViewHolder> {
    Context context;
    ArrayList<Trip> trips;
    LayoutInflater inflater;
    private ArrayAdapter<String> listAdapter ;
    HistoryFrag historyFrag;
    FragmentManager fM;
    int flag[];


    public CardViewHist(Context context, ArrayList<Trip> trips) {
        this.context = context;
        this.trips = trips;
        flag = new int[trips.size()];
        inflater = LayoutInflater.from(context);

    }

    @Override
    public CardViewHolder onCreateViewHolder(ViewGroup parent, int position) {
        View view = inflater.inflate(R.layout.history_item,parent,false);
        CardViewHolder holder = new CardViewHolder(view);
        Log.i("trips",trips.get(position).getUrl()+"");
        return holder;
    }

    @Override
    public void onBindViewHolder(final CardViewHolder holder, final int position) {
        FileInputStream is = null;
        try {
            is = new FileInputStream(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES)+"/imgetr"+trips.get(position).getId());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        Log.i("try1", "2");
        Bitmap b = BitmapFactory.decodeStream(is);
        Log.i("try1", "3");
        holder.img.setImageBitmap(b);
        holder.name.setText(trips.get(position).getName());
        holder.status.setText(trips.get(position).getStatus());
        holder.startdate.setText(trips.get(position).getSd()+"       "+trips.get(position).getSt());
//        holder.enddate.setText(trips.get(position).getEd());
//        holder.starttime.setText(trips.get(position).getSt());
//        holder.endtime.setText(trips.get(position).getEt());
//        Log.i("yarab1",holder.name.getText()+"");
//        Log.i("yarab1",trips.get(position).getSt()+"asdasdasd");
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

        /////
//        listAdapter = new ArrayAdapter<String>(context,R.layout.list,R.id.noteX, trips.get(position).getNotes());
//        holder.notes.setAdapter(listAdapter);
//        holder.notes.setOnTouchListener(new ListView.OnTouchListener() {
//            @Override
//            public boolean onTouch(View v, MotionEvent event) {
//                int action = event.getAction();
//                switch (action) {
//                    case MotionEvent.ACTION_DOWN:
//                        // Disallow ScrollView to intercept touch events.
//                        v.getParent().requestDisallowInterceptTouchEvent(true);
//                        break;
//
//                    case MotionEvent.ACTION_UP:
//                        // Allow ScrollView to intercept touch events.
//                        v.getParent().requestDisallowInterceptTouchEvent(false);
//                        break;
//                }
//
//                // Handle ListView touch events.
//                v.onTouchEvent(event);
//                return true;
//            }
//        });
        holder.delbut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder = new AlertDialog.Builder(context);
                builder.setMessage("Are you sure you want to delete.");
                builder.setCancelable(false);
                Boolean check = false;
                builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int id) {
                        SQLAdapter adapter = new SQLAdapter(context);
                        long i = adapter.deleteTrip(trips.get(position).getId());
                        historyFrag = new HistoryFrag();
                        fM = ((Activity) context).getFragmentManager();
                        FragmentTransaction fT = fM.beginTransaction();
                        fT.replace(R.id.mainFrag, historyFrag, "hist");
                        fT.commit();
                        dialog.cancel();
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
        });

        holder.histCard.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                if(flag[position]==0){
                    flag[position]=1;
                    /////////////////////////////////////////
                    holder.histextra.setVisibility(View.VISIBLE);
                    Animation animation   = AnimationUtils.loadAnimation(v.getContext(), R.anim.animationhistory);
                    animation.setDuration(500);
                    holder.histextra.setAnimation(animation);
                    holder.histextra.animate();
                    animation.start();
                    animation.setDuration(500);
                    holder.delbut.setAnimation(animation);
                    holder.delbut.animate();
                    animation.start();
                    /////////////////////////////////////////////
                }
                else {
                    flag[position]=0;
                    Animation animation   = AnimationUtils.loadAnimation(v.getContext(), R.anim.animationhistoryout);
                    animation.setDuration(1);
                    holder.histextra.setAnimation(animation);
                    holder.histextra.animate();
                    animation.start();
                    holder.histextra.setVisibility(View.GONE);
                }
            }
        });
        holder.histextra.setVisibility(View.GONE);

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
        ////////////////////////////////////////////////////////////////////
        String distvel;
        SQLAdapter adapter = new SQLAdapter(context);
        distvel = adapter.retrivedist(trips.get(position).getId());
        if(distvel==null)
            distvel="No available speed and distance info";
        holder.cfdistvel.setText(distvel);
        /////////////////////////////////////////////////////////////////////

    }

    @Override
    public int getItemCount() {
        return trips.size();
    }

    class CardViewHolder extends RecyclerView.ViewHolder{
        ImageView img;
        TextView name;
        TextView status;
        TextView startdate;
        TextView startpoint;
        TextView endpoint;
        TextView reps;
//        ListView notes;
        Button delbut;
        LinearLayout histCard;
        LinearLayout histextra;
        TextView cfdistvel;
        Button notesbut;


        public CardViewHolder(View itemView) {
            super(itemView);
            delbut = (Button) itemView.findViewById(R.id.delbut);
            notesbut = (Button) itemView.findViewById(R.id.shownoteshist);
            img = (ImageView) itemView.findViewById(R.id.tripimg);
            name = (TextView) itemView.findViewById(R.id.tripname);
            status = (TextView) itemView.findViewById(R.id.status);
            startdate = (TextView) itemView.findViewById(R.id.tripstarttime);
//            enddate = (TextView) itemView.findViewById(R.id.tripenddate);
//            starttime = (TextView) itemView.findViewById(R.id.tripstarttime);
//            endtime = (TextView) itemView.findViewById(R.id.tripendtime);
            startpoint = (TextView) itemView.findViewById(R.id.cftripstartpoint);
            endpoint = (TextView) itemView.findViewById(R.id.cftripendpoint);
            reps = (TextView) itemView.findViewById(R.id.cfreps);
//            notes = (ListView)itemView.findViewById(R.id.noteshist);
            histCard = (LinearLayout)itemView.findViewById(R.id.histCard);
            histextra = (LinearLayout)itemView.findViewById(R.id.extrahist);
            cfdistvel = (TextView) itemView.findViewById(R.id.cfdistvel);
        }
    }

}
