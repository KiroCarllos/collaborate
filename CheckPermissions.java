package com.example.delllaptop.projone;

import android.app.Activity;
import android.content.Context;
import android.content.pm.PackageManager;
import android.net.ConnectivityManager;
import android.support.v4.app.ActivityCompat;
import android.widget.Toast;

/**
 * Created by Dell Laptop on 3/15/2018.
 */
public class CheckPermissions {

    private static final int INTERNET_PERMISSION  =1;
    private static final int LOCATION_PERMISSION =2 ;
    private static final int EXTERNAL_STORAGE_PERMISSION  =3;
    Context context ;
    private int locationPermission;

    public CheckPermissions(Context context) {
        this.context = context;
    }

    public Boolean checkExernalStorage() {
        if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {
            return true;
        } else {
            ActivityCompat.requestPermissions((Activity) context, new String[]{android.Manifest.permission.WRITE_EXTERNAL_STORAGE}, EXTERNAL_STORAGE_PERMISSION);
            if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {
                return true;
            } else {
                return false;
            }
        }
    }
    public Boolean checkLocation() {

        int result = ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_FINE_LOCATION) ;
        if (result == PackageManager.PERMISSION_GRANTED){
            return true;
        } else {
            ActivityCompat.requestPermissions((Activity) context,
                    new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, LOCATION_PERMISSION);

            if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {
                return true;
            } else {
                return false;
            }
        }
    }



    public Boolean checkInternet() {
        final ConnectivityManager connectivityManager = ((ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE));
        if (connectivityManager.getActiveNetworkInfo() != null && connectivityManager.getActiveNetworkInfo().isConnected())
        {
            return true;
        }else {
            Toast.makeText(context, "Please check your Internet Connection", Toast.LENGTH_LONG).show();
        }
        return false ;
    }



}