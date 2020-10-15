package com.example.delllaptop.projone;

import android.app.Activity;
import android.app.Notification;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.support.v4.app.NotificationCompat;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewConfiguration;
import android.view.WindowManager;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.delllaptop.projone.DTO.Trip;

import java.util.ArrayList;

public class FloatingService extends Service {
    private WindowManager mWindowManager;
    private View mFloatingView;
    ArrayList<String>myNotes=new ArrayList<>();
    LinearLayout myLayout;
    TextView myText;
    Boolean expanded;
    View collapsedView;
    View expandedView;

    public FloatingService() {
    }

    @Override
    public IBinder onBind(Intent intent) {


        return null;
    }

    @Override
    public void onCreate() {
        super.onCreate();
        mFloatingView = LayoutInflater.from(this).inflate(R.layout.layout_floating_widget, null);
        //Inflate the floating view layout we created


        //Add the view to the window.
        final WindowManager.LayoutParams params = new WindowManager.LayoutParams(
                WindowManager.LayoutParams.WRAP_CONTENT,
                WindowManager.LayoutParams.WRAP_CONTENT,
                WindowManager.LayoutParams.TYPE_PHONE,
                WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
                PixelFormat.TRANSLUCENT);

        //Specify the view position
        params.gravity = Gravity.TOP | Gravity.LEFT;        //Initially view will be added to top-left corner
        params.x = 0;
        params.y = 100;

        //Add the view to the window
        mWindowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
        mWindowManager.addView(mFloatingView, params);

        //The root element of the collapsed view layout
        collapsedView = mFloatingView.findViewById(R.id.collapseView);
//The root element of the expanded view layout
        expandedView = mFloatingView.findViewById(R.id.expanded_container);


//Set the close button
        ImageView closeButtonCollapsed = (ImageView) mFloatingView.findViewById(R.id.close_btn);
        closeButtonCollapsed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //close the service and remove the from from the window
                stopSelf();
            }
        });

        ImageView closeButtonCollapsed2 = (ImageView) mFloatingView.findViewById(R.id.close_btn2);
        closeButtonCollapsed2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //close the service and remove the from from the window
                stopSelf();
            }
        });

//        CheckBox firstCheckBox= (CheckBox)mFloatingView.findViewById(R.id.NoteCheck1);
//        firstCheckBox.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Toast.makeText(view.getContext(),"check box clicked",Toast.LENGTH_LONG).show();
//            }
//        });
//
//        TextView firstText= (TextView) mFloatingView.findViewById(R.id.NoteText1);
//        firstText.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Toast.makeText(view.getContext(),"Text view clicked",Toast.LENGTH_LONG).show();
//            }
//        });


        mFloatingView.findViewById(R.id.root_container).setOnTouchListener(new View.OnTouchListener() {
            private int initialX;
            private int initialY;
            private float initialTouchX;
            private float initialTouchY;


            @Override
            public boolean onTouch(View v, MotionEvent event) {
                switch (event.getAction()) {
                    case MotionEvent.ACTION_DOWN:
                        //remember the initial position.
                        initialX = params.x;
                        initialY = params.y;
                        //get the touch location
                        initialTouchX = event.getRawX();
                        initialTouchY = event.getRawY();
                        return true;

                    case MotionEvent.ACTION_MOVE:
                        //Calculate the X and Y coordinates of the view.
                        params.x = initialX + (int) (event.getRawX() - initialTouchX);
                        params.y = initialY + (int) (event.getRawY() - initialTouchY);
                        //Update the layout with new X & Y coordinate
//                        if (isViewCollapsed()) {
//                                //When user clicks on the image view of the collapsed layout,
//                                //visibility of the collapsed layout will be changed to "View.GONE"
//                                //and expanded view will become visible.
//                                collapsedView.setVisibility(View.GONE);
//                                expandedView.setVisibility(View.VISIBLE);
//
//                        }
                        mWindowManager.updateViewLayout(mFloatingView, params);
                        return true;

                    case MotionEvent.ACTION_UP:
                        int Xdiff = (int) (event.getRawX() - initialTouchX);
                        int Ydiff = (int) (event.getRawY() - initialTouchY);


                        //The check for Xdiff <10 && YDiff< 10 because sometime elements moves a little while clicking.
                        //So that is click event.
                        if (Xdiff < 10 && Ydiff < 10) {
                            if (isViewCollapsed()) {
                                //When user clicks on the image view of the collapsed layout,
                                //visibility of the collapsed layout will be changed to "View.GONE"
                                //and expanded view will become visible.
                                collapsedView.setVisibility(View.GONE);
                                expandedView.setVisibility(View.VISIBLE);
                                expanded=true;

                            }
                        }
                        return true;
                }
                return false;
            }
        });

    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        NotificationCompat.Builder mBuilder;

            Log.i("floatser", intent + "");
            Bundle bundle = intent.getBundleExtra("bundle");
            Log.i("floatser", bundle + "");
            Trip trip = (Trip) bundle.getSerializable("trip");
            Log.i("floatser", trip + "");
        mBuilder = new NotificationCompat.Builder(this,"default");
        mBuilder.setContentText("Tripaway")
                .setContentTitle("You are currently on trip "+trip.getName())
                .setSmallIcon(R.drawable.roundnitif);
        //NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        Notification notif = mBuilder.build();
        startForeground(5,notif);
        //nm.notify(trip.getId()+1000,mBuilder.build());
            myNotes = trip.getNotes();
            for (int i = 0; i < myNotes.size(); i++) {
                int j = i + 1;
                String LayoutID = "Note" + j;
                int layoutId = getResources().getIdentifier(LayoutID, "id", getPackageName());
                myLayout = mFloatingView.findViewById(layoutId);
                myLayout.setVisibility(View.VISIBLE);
                String TextID = "NoteText" + j;
                int resID = getResources().getIdentifier(TextID, "id", getPackageName());
                myText = mFloatingView.findViewById(resID);
                myText.setText(myNotes.get(i));
            }
        return Service.START_REDELIVER_INTENT;
    }

    private boolean isViewCollapsed() {
        return mFloatingView == null || mFloatingView.findViewById(R.id.collapseView).getVisibility() == View.VISIBLE;
    }


    @Override
    public void onDestroy() {
        super.onDestroy();
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            stopForeground(STOP_FOREGROUND_REMOVE);
        }
        if (mFloatingView != null) mWindowManager.removeView(mFloatingView);
    }

}


