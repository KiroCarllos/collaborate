package com.mona.project.model;

import java.util.ArrayList;
import java.util.List;

public class Trip {
    String tripName, startPoint, endPoint, date, time, tripStatues, tripType, tripRepeat, tripId,userId;
    List<String> notes;

    public Trip() {
    }

    public Trip(String tripName, String tripStatues) {
        this.tripName = tripName;
        this.tripStatues = tripStatues;
    }

    public Trip(String tripName, String startPoint, String endPoint,
                String date, String time, String tripStatues, String tripType, String tripRepeat, String tripId,String userId, List<String> notes) {
        this.tripName = tripName;
        this.startPoint = startPoint;
        this.endPoint = endPoint;
        this.date = date;
        this.time = time;
        this.tripStatues = tripStatues;
        this.tripType = tripType;
        this.tripRepeat = tripRepeat;
        this.tripId = tripId;
        this.userId=userId;
        this.notes = notes;
    }

    public String getTripName() {
        return tripName;
    }

    public void setTripName(String tripName) {
        this.tripName = tripName;
    }

    public String getStartPoint() {
        return startPoint;
    }

    public void setStartPoint(String startPoint) {
        this.startPoint = startPoint;
    }

    public String getEndPoint() {
        return endPoint;
    }

    public void setEndPoint(String endPoint) {
        this.endPoint = endPoint;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getTripType() {
        return tripType;
    }

    public void setTripType(String roundTrip) {
        this.tripType = roundTrip;
    }

    public String getTripRepeat() {
        return tripRepeat;
    }

    public void setTripRepeat(String tripRepeat) {
        this.tripRepeat = tripRepeat;
    }

    public String getTripStatues() {
        return tripStatues;
    }

    public void setTripStatues(String tripStatues) {
        this.tripStatues = tripStatues;
    }

    public String getTripId() {
        return tripId;
    }

    public void setTripId(String tripId) {
        this.tripId = tripId;
    }

    public List<String> getNotes() {
        return notes;
    }

    public void setNotes(List<String> notes) {
        this.notes = notes;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
