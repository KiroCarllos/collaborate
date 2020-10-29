package com.mona.project;

import android.annotation.SuppressLint;
import android.app.Notification;
import android.app.Service;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.os.Build;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.core.app.NotificationCompat;

import java.util.ArrayList;

public class FloatingIconService extends Service {
    private WindowManager mWindowManager;
    private View mFloatingNoteView;
    ArrayList<String> tripNotes =new ArrayList<>();
    LinearLayout myLayout;
    TextView txtNote;
    Boolean expanded;
    View collapsedView;
    View expandedView;
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @SuppressLint("ClickableViewAccessibility")
    @Override
    public void onCreate() {
        super.onCreate();
        mFloatingNoteView = LayoutInflater.from(this).inflate(R.layout.floating_icon, null);
        //Add the view to the window.
        final WindowManager.LayoutParams params = new WindowManager.LayoutParams(
                WindowManager.LayoutParams.WRAP_CONTENT,
                WindowManager.LayoutParams.WRAP_CONTENT,
                WindowManager.LayoutParams.TYPE_PHONE,
                WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
                PixelFormat.TRANSLUCENT);
        //Initial position
        params.gravity = Gravity.TOP | Gravity.LEFT;
        params.x = 0;
        params.y = 100;
        //Add the view to the window
        mWindowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
        mWindowManager.addView(mFloatingNoteView, params);
        //Collapse view layout
        collapsedView = mFloatingNoteView.findViewById(R.id.collapseView);
        //Expanded view layout
        expandedView = mFloatingNoteView.findViewById(R.id.expanded_container);
        //Set the close button.
        ImageView closeButton = (ImageView) mFloatingNoteView.findViewById(R.id.close_floating_icon);
        closeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stopSelf();
            }
        });
        ImageView closeButtonCollapsed2 = (ImageView) mFloatingNoteView.findViewById(R.id.close_notes);
        closeButtonCollapsed2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                stopSelf();
            }
        });

        //Drag and move chat head using user's touch action.
        mFloatingNoteView.findViewById(R.id.root_container).setOnTouchListener(new View.OnTouchListener() {
            private int lastAction;
            private int initialX;
            private int initialY;
            private float initialTouchX;
            private float initialTouchY;
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                switch (motionEvent.getAction()) {
                    case MotionEvent.ACTION_DOWN:
                        //remember the initial position.
                        initialX = params.x;
                        initialY = params.y;
                        //get the touch location
                        initialTouchX = motionEvent.getRawX();
                        initialTouchY = motionEvent.getRawY();

                        lastAction = motionEvent.getAction();
                        return true;
                    case MotionEvent.ACTION_UP:
                        if (lastAction == MotionEvent.ACTION_DOWN) {
                            if (isViewCollapsed()) {
                                collapsedView.setVisibility(View.GONE);
                                expandedView.setVisibility(View.VISIBLE);
                                expanded=true;
                            }
                        }
                        lastAction = motionEvent.getAction();
                        return true;
                    case MotionEvent.ACTION_MOVE:
                        //Calculate the X and Y coordinates of the view.
                        params.x = initialX + (int) (motionEvent.getRawX() - initialTouchX);
                        params.y = initialY + (int) (motionEvent.getRawY() - initialTouchY);
                        //Update the layout with new X & Y coordinate
                        mWindowManager.updateViewLayout(mFloatingNoteView, params);
                        lastAction = motionEvent.getAction();
                        return true;
                }
                return false;
            }
        });
    }
    //ToDO fill current trip Notes
//    @Override
//    public int onStartCommand(Intent intent, int flags, int startId) {
//        NotificationCompat.Builder mBuilder;
//        Bundle bundle = intent.getBundleExtra("bundle");
//        Trip trip = (Trip) bundle.getSerializable("trip");
//        Log.i("floatser", trip + "");
//        mBuilder = new NotificationCompat.Builder(this,"default");
//        mBuilder.setContentText("My Trip")
//                .setContentTitle("You are currently on trip "+trip.getName())
//                .setSmallIcon(R.drawable.roundnitif);
//        //NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
//        Notification notif = mBuilder.build();
//        startForeground(5,notif);
//        //nm.notify(trip.getId()+1000,mBuilder.build());
//        tripNotes = trip.getNotes();
//        for (int i = 0; i < tripNotes.size(); i++) {
//            int j = i + 1;
//            String LayoutID = "Note" + j;
//            int layoutId = getResources().getIdentifier(LayoutID, "id", getPackageName());
//            myLayout = mFloatingNoteView.findViewById(layoutId);
//            myLayout.setVisibility(View.VISIBLE);
//            String TextID = "NoteText" + j;
//            int resID = getResources().getIdentifier(TextID, "id", getPackageName());
//            txtNote = mFloatingNoteView.findViewById(resID);
//            txtNote.setText(tripNotes.get(i));
//        }
//        return Service.START_REDELIVER_INTENT;
//    }

    private boolean isViewCollapsed() {
        return mFloatingNoteView == null || mFloatingNoteView.findViewById(R.id.collapseView).getVisibility() == View.VISIBLE;
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            stopForeground(STOP_FOREGROUND_REMOVE);
        }
        if (mFloatingNoteView != null) mWindowManager.removeView(mFloatingNoteView);
    }
}
