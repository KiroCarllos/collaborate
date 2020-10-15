package com.example.delllaptop.projone;

import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;

import com.example.delllaptop.projone.DTO.DownloadImage;
import com.example.delllaptop.projone.DTO.LocationObject;
import com.example.delllaptop.projone.DTO.Trip;

import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.List;
import java.util.Locale;

/**
 * Created by Dell Laptop on 3/15/2018.
 */

public class GetCurrentLocation {
    Geocoder geocoder;
    List<Address> allAddress;
    private double longitudes;
    private double latitudes;
    LocationObject myLocation;
    String Message;
    LocationManager loc;
    Boolean locationPerm;
    Boolean internetPerm;

    public Boolean getMyLocation(final Context context, final Trip trip) {
        geocoder = new Geocoder(context, Locale.getDefault());
        loc = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);
        CheckPermissions checkPermissions = new CheckPermissions(context);
        internetPerm = checkPermissions.checkInternet();
        if (ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(context, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            locationPerm = checkPermissions.checkLocation();
            return null;
        }
        if(locationPerm && internetPerm) {
            loc.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, new LocationListener() {
                @Override
                public void onLocationChanged(Location location) {
                    latitudes = location.getLatitude();
                    longitudes = location.getLongitude();
                    // String longitude = "" + longitudes;
                    // String latitude = "" + latitudes;

                    try {
                        allAddress = geocoder.getFromLocation(latitudes, longitudes, 1);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                    if (allAddress != null) {
                        Message = allAddress.get(0).getFeatureName() + " " + allAddress.get(0).getCountryName();
                    }
                    DateFormat dateFormat = new SimpleDateFormat("dd-MM-yyyy", Locale.ENGLISH);
                    DateFormat timeFormat = new SimpleDateFormat("hh:mm");
                    Calendar myCal = Calendar.getInstance();
                    String stime = timeFormat.format(myCal.getTime());
                    String sdate = dateFormat.format(myCal.getTime());
                    myLocation = new LocationObject(longitudes, latitudes, Message);
                    SQLAdapter adapter = new SQLAdapter(context);
                    long i2 = adapter.updateTrip(trip.getId(), trip.getName(), trip.getSp(), trip.getSlong()
                            , trip.getSlat(), trip.getEp(), trip.getElong(), trip.getElat(), "Done", sdate,
                            sdate, stime, stime, trip.getRep(), trip.getUser(), null);
                    String uri = "http://maps.google.com/maps?saddr=" + trip.getSlat() +
                            "," + trip.getSlong() + "&daddr=" + trip.getElat()
                            + "," + trip.getElong();
                    Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(uri));
                    trip.setStatus("Done");
                    String webLink = "https://maps.googleapis.com/maps/api/directions/json?origin=" + trip.getSlat() +
                            "," + trip.getSlong() + "&destination=" + trip.getElat()
                            + "," + trip.getElong();
                    DownloadImage dImg = new DownloadImage(webLink, context, trip);
                    dImg.execute();
                    //Toast.makeText(MainActivity.this, "logitude: " + longitude + "\nLatitude: " + latitude+"\nLocation"+Message, Toast.LENGTH_SHORT).show();
                    loc.removeUpdates(this);
                }


                @Override
                public void onStatusChanged(String s, int i, Bundle bundle) {

                }

                @Override
                public void onProviderEnabled(String s) {

                }

                @Override
                public void onProviderDisabled(String s) {

                }
            });
        }

        return false;
    }

}
