package com.mona.project;

import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.mona.project.fragment.LogInFragment;
import com.mona.project.fragment.TripFragment;

public class MainActivity extends AppCompatActivity {
    LogInFragment logInFragment;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //logInFragment=new LogInFragment();
        //getSupportFragmentManager().beginTransaction().add(R.id.container,logInFragment).commit();

        FragmentManager fm = getSupportFragmentManager();
        logInFragment = (LogInFragment) fm.findFragmentById(R.id.container);
        //fragmentB = (FragmentB) fm.findFragmentById(R.id.containerB);
        if (logInFragment == null /*&& fragmentB==null*/) {
            logInFragment=new LogInFragment();
            //fragmentB=new FragmentB();
            fm.beginTransaction()
                    .add(R.id.container,logInFragment).commit();
                    //.add(R.id.containerB,fragmentB).commit();
        }
    }
}