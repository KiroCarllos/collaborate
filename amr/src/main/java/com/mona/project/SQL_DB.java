package com.mona.project;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

import java.util.ArrayList;

public class SQL_DB extends SQLiteOpenHelper {
    public static final String dbName = "data.db";

    public SQL_DB(@Nullable Context context) {
        super(context, dbName, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("create table myTable ( tripName TEXT, startPoint TEXT, endPoint TEXT, date TEXT, time TEXT, tripType TEXT, tripRepeat TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int i, int i1) {
        db.execSQL("DROP TABLE IF EXISTS myTable");
        onCreate(db);
    }

    public boolean insert_data(String tripName, String startPoint,String endPoint,String date,String time,String tripType,String tripRepeat) {
        SQLiteDatabase database = getWritableDatabase();
        ContentValues values = new ContentValues();

        values.put("tripName", tripName);
        values.put("startPoint", startPoint);
        values.put("endPoint", endPoint);
        values.put("date", date);
        values.put("time", time);
        values.put("tripType", tripType);
        values.put("tripRepeat", tripRepeat);

        long result = database.insert("myTable", null, values);
        if (result == -1) {
            return false;
        } else {
            return true;
        }
    }

    public ArrayList getAllRecords() {
        ArrayList arrayList = new ArrayList();
        SQLiteDatabase db = getReadableDatabase();
        Cursor cursor = db.rawQuery("select tripName, startPoint, endPoint, date, time, tripType, tripRepeat from myTable", null);
        cursor.moveToFirst();
        while (cursor.isAfterLast() == false) {
            String s1 = cursor.getString(cursor.getColumnIndex("tripName"));
            String s2 = cursor.getString(cursor.getColumnIndex("startPoint"));
            String s3 = cursor.getString(cursor.getColumnIndex("endPoint"));
            String s4 = cursor.getString(cursor.getColumnIndex("date"));
            String s5 = cursor.getString(cursor.getColumnIndex("time"));
            String s6 = cursor.getString(cursor.getColumnIndex("tripType"));
            String s7 = cursor.getString(cursor.getColumnIndex("tripRepeat"));
            arrayList.add(s1);
            arrayList.add(s2);
            arrayList.add(s3);
            arrayList.add(s4);
            arrayList.add(s5);
            arrayList.add(s6);
            arrayList.add(s7);
            cursor.moveToNext();
        }
        return arrayList;
    }

    public boolean updateData(String tripName, String startPoint,String endPoint,String date,String time,String tripType,String tripRepeat){
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("tripName", tripName);
        values.put("startPoint", startPoint);
        values.put("endPoint", endPoint);
        values.put("date", date);
        values.put("time", time);
        values.put("tripType", tripType);
        values.put("tripRepeat", tripRepeat);
        db.update("myTable",values,"tripName= ?",new String[]{tripName});
        return true;
    }

    public Integer deletData(String tripName){
        SQLiteDatabase db = getWritableDatabase();
        return db.delete("myTable","tripName= ?",new String[]{tripName});
    }
}
