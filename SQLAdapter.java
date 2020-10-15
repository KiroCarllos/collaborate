package com.example.delllaptop.projone;

/**
 * Created by Dell Laptop on 3/10/2018.
 */
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;


import com.example.delllaptop.projone.DTO.Trip;

import java.util.ArrayList;


public class SQLAdapter {
    private Context context;
    static MySQLHelper dbHelper;

    public SQLAdapter(Context _context){
        dbHelper = new MySQLHelper(_context);
        context = _context;
    }

    public long insertNote(String note, int id){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put("_id",id);
        contentValues.put(MySQLHelper.note,note);
        long i = db.insert(MySQLHelper.notes_table,null,contentValues);
        return i;
    }

    public long updateNote(String note,String oldNote, int id){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(MySQLHelper.note,note);
        long i = db.update(MySQLHelper.notes_table,contentValues,"_id = "+id+" and "+ MySQLHelper.note+" like '"+oldNote+"'",null);
        return i;
    }

    public long deleteNote(String oldNote, int id){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        long i = db.delete(MySQLHelper.notes_table,"_id = "+id+" and "+ MySQLHelper.note+" like '"+oldNote+"'",null);
        return i;
    }

    public ArrayList<String> retrieveNotes(int id){
        ArrayList<String> notes = new ArrayList<String>();

        Cursor c;
        String[] columns = {MySQLHelper.note};
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        c = db.query(dbHelper.notes_table,columns,"_id = "+id,null,null,null,null);
        while ( c.moveToNext()) {
            String note = new String();
            note = (c.getString(0));
            notes.add(note);
        }
        return notes;
    }

    public long insertTrip(String name, String sp, String slong, String slat, String ep, String elong,
                           String elat, String status, String sd, String ed, String st, String et, int rep, String user, String url){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(MySQLHelper.name,name);
        contentValues.put(MySQLHelper.sp,sp);
        contentValues.put(MySQLHelper.slong,slong);
        contentValues.put(MySQLHelper.slat,slat);
        contentValues.put(MySQLHelper.ep,ep);
        contentValues.put(MySQLHelper.elong,elong);
        contentValues.put(MySQLHelper.elat,elat);
        contentValues.put(MySQLHelper.status,status);
        contentValues.put(MySQLHelper.sd,sd);
        contentValues.put(MySQLHelper.ed,ed);
        contentValues.put(MySQLHelper.st,st);
        contentValues.put(MySQLHelper.et,et);
        contentValues.put(MySQLHelper.rep,rep);
        contentValues.put(MySQLHelper.user,user);
        if(url!=null)
        contentValues.put(MySQLHelper.url,url);
        long i = db.insert(MySQLHelper.trip_table,null,contentValues);
        Log.i("log",i+"");
        return i;
    }
    public long updateTrip(int id, String name, String sp, String slong, String slat, String ep, String elong,
                           String elat, String status, String sd, String ed, String st,String et,int rep, String user,String url){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(MySQLHelper.name,name);
        contentValues.put(MySQLHelper.sp,sp);
        contentValues.put(MySQLHelper.slong,slong);
        contentValues.put(MySQLHelper.slat,slat);
        contentValues.put(MySQLHelper.ep,ep);
        contentValues.put(MySQLHelper.elong,elong);
        contentValues.put(MySQLHelper.elat,elat);
        contentValues.put(MySQLHelper.status,status);
        contentValues.put(MySQLHelper.sd,sd);
        contentValues.put(MySQLHelper.ed,ed);
        contentValues.put(MySQLHelper.st,st);
        contentValues.put(MySQLHelper.et,et);
        contentValues.put(MySQLHelper.rep,rep);
        contentValues.put(MySQLHelper.user,user);
        long i = db.update(MySQLHelper.trip_table,contentValues,"_id = "+id,null);
        Log.i("sqlupdate",i+"");
        return i;
    }
    public long deleteTrip(int id){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        long i = db.delete(MySQLHelper.trip_table,"_id = "+id,null);

        return i;
    }

    public ArrayList<Trip> retrieveTrips(String user){
        ArrayList<Trip> trips = new ArrayList<Trip>();
        Cursor c;
        String[] columns = {MySQLHelper.id,dbHelper.name, MySQLHelper.sp, MySQLHelper.ep, MySQLHelper.slat, MySQLHelper.slong,
                MySQLHelper.elat, MySQLHelper.elong, MySQLHelper.status, MySQLHelper.rep, MySQLHelper.sd,
                MySQLHelper.ed, MySQLHelper.st, MySQLHelper.et, MySQLHelper.user, MySQLHelper.url};
        String[] args = {user};
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        Log.i("insertsql",user +" done");
        c = db.query(dbHelper.trip_table,columns,MySQLHelper.user + " = ?",args,null,null,null);
        Log.i("ic",c.getCount()+"");
        if(c.getCount()>0){
            while ( c.moveToNext()) {
                Trip trip = new Trip();
                trip.setId(c.getInt(0));
                trip.setName(c.getString(1));
                trip.setSp(c.getString(2));
                trip.setEp(c.getString(3));
                trip.setSlat(c.getString(4));
                trip.setSlong(c.getString(5));
                trip.setElat(c.getString(6));
                trip.setElong(c.getString(7));
                trip.setStatus(c.getString(8));
                trip.setRep(c.getInt(9));
                trip.setSd(c.getString(10));
                trip.setEd(c.getString(11));//////
                trip.setSt(c.getString(12));
                trip.setEt(c.getString(13));
                trip.setUser(c.getString(14));
                trip.setUrl(c.getString(15));
                trip.setNotes(retrieveNotes(trip.getId()));
                trips.add(trip);
            }
        }
        return trips;
    }
    /////////////////////////////////////////////////
    public String retrivedist(int id){
        String distvel = "";
        Cursor c;
        String[] columns = {MySQLHelper.distvel};
        String[] args = {id+""};
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        Log.i("insertsql",id +" done");
        c = db.query(dbHelper.trip_table,columns,dbHelper.id+"="+id,null,null,null,null);
        Log.i("idasdasdasdasdc",c.getCount()+"");
        if(c.getCount()>0){
            while ( c.moveToNext()) {
                distvel = c.getString(0);
                Log.i("zzzzzzidasdasdasdasdc",distvel+"");
            }
        }
        return distvel;
    }

    public long updateTripdist(int id,String distvel){
        SQLiteDatabase db = dbHelper.getWritableDatabase();
        ContentValues contentValues = new ContentValues();
        contentValues.put(MySQLHelper.distvel,distvel);
        long i = db.update(MySQLHelper.trip_table,contentValues,"_id = "+id,null);
        Log.i("idasdasdasdasdcxxxxxqwe",i+"");
        return i;
    }
    ///////////////////////////////////////////////

    static class MySQLHelper extends SQLiteOpenHelper {
        public static final String trip_table="trips";
        public static final String notes_table="notes";
        public static final String id="_id";
        public static final String name="name";
        public static final String sp="start_point";
        public static final String slong="Start_logintude";
        public static final String slat="Start_latitude";
        public static final String ep="end_point";
        public static final String elong="end_logintude";
        public static final String elat="end_latitude";
        public static final String status="status";
        public static final String sd="start_date";
        public static final String ed="end_date";
        public static final String st="start_time";
        public static final String et="end_time";
        public static final String rep="Repeatition";
        public static final String note="note";
        public static final String user="user";
        public static final String url="url";
        public static final String distvel="distvel";

        private static final String DATABASE_NAME = "acamar.db";
        private static final int version = 1;

        public MySQLHelper(Context context) {
            super(context, DATABASE_NAME, null, version);
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            db.execSQL("create table "+trip_table+" ("+id+" integer primary key autoincrement," +
                    " "+name+" varchar(255),"+sp+" varchar(255), "+ep+" varchar(255),"+slat+" varchar(255)," +
                    " "+slong+" varchar(255),"+elat+" varchar(255),"+elong+" varchar(255)," +
                    " "+status+" varchar(255),"+rep+" int,"+sd+" varchar(255),"+ed+" varchar(255),"+st+" varchar(255),"+et+" varchar(255),"+user+" varchar(255),"+url+" text,"+distvel+" varchar(255));");
            db.execSQL("create table "+notes_table+" (idtrip integer primary key autoincrement, _id integer," +
                    ""+note+" varchar(255));");
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {

        }
    }
}