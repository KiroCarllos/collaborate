package com.example.delllaptop.projone;

import android.Manifest;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Window;

import java.util.Timer;
import java.util.TimerTask;

public class Splash extends AppCompatActivity {

    long loadTime = 4000;
    SharedPreferences saving;
    public static final String saveData="NewData";
    public static final String newLogin="NewLogin";
    String user;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        final Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {

                saving=getSharedPreferences(saveData,0);
                boolean firstTime = saving.getBoolean(newLogin,false);
                user = saving.getString("user", "null");
                Log.i("user",user);
                if(!firstTime) {
                    Intent login = new Intent(Splash.this, Login.class);
                    startActivity(login);
                    finish();
                }
                else {
                    Intent Home = new Intent(Splash.this, Welcome.class);
                    startActivity(Home);
                    finish();
                }
                finish();

            }
        }, 1);
    }

}
