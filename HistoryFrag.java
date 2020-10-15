package com.example.delllaptop.projone;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.app.Fragment;
import android.provider.Settings;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.example.delllaptop.projone.DTO.Trip;

import java.util.ArrayList;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link HistoryFrag.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link HistoryFrag#newInstance} factory method to
 * create an instance of this fragment.
 */
public class HistoryFrag extends Fragment {


    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    RecyclerView rv;
    CardViewHist cvh;
    ArrayList<Trip> trips;
    ArrayList<Trip> historyTrips;
    View view;
    SharedPreferences saving;
    public static final String saveData="NewData";
    public static final String newLogin="NewLogin";
    String user;

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    private OnFragmentInteractionListener mListener;

    public HistoryFrag() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment HistoryFrag.
     */
    // TODO: Rename and change types and number of parameters
    public static HistoryFrag newInstance(String param1, String param2) {
        HistoryFrag fragment = new HistoryFrag();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
            Log.i("user",user);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.fragment_history, container, false);
        trips=new ArrayList<Trip>();
        historyTrips=new ArrayList<Trip>();
        saving=getActivity().getSharedPreferences(saveData,0);
        user = saving.getString("user", "null");
        if (Build.VERSION.SDK_INT >= 23) {
            if (!Settings.canDrawOverlays(view.getContext())) {
                Toast.makeText(view.getContext(),"Please grant overlay permisssion",Toast.LENGTH_LONG).show();
                Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION, Uri.parse("package:" + view.getContext().getPackageName()));
                startActivityForResult(intent, 0);
            }
        }
        ///set eltrips
//        ArrayList<String> notes = new ArrayList<>();
//        Trip t1 = new Trip("name","spoint","slong","slat","epoint",
//                "elong","elat","Done","sdate","edate","stime","etime",7,notes,user);
//        t1.setId(1);
//        trips.add(t1);
//        Trip t2 = new Trip("name","spoint","slong","slat","epoint",
//                "elong","elat","Cancelled","sdate","edate","stime","etime",7,notes,user);
//        t2.setId(2);
//        trips.add(t2);
//
//        Trip t3 = new Trip("name","spoint","slong","slat","epoint",
//                "elong","elat","Cancelled","sdate","edate","stime","etime",7,notes,user);
//        t3.setId(3);
//        trips.add(t3);
//
//        Trip t4 = new Trip("namghjghjgjhgjhe","spoint","slong","slat","epoint",
//                "elong","elat","Done","sdate","edate","stime","etime",7,notes,user);
//        t4.setId(4);
//        trips.add(t4);
        SQLAdapter adapter = new SQLAdapter(getActivity());
        trips=adapter.retrieveTrips(user);
        for(Trip temp:trips){
            Trip t;
            if (!temp.getStatus().toString().equals("upcoming")){
                t = temp;
                historyTrips.add(t);
            }
        }
        if(historyTrips.size()<=0){
            view.findViewById(R.id.notripshist).setVisibility(View.VISIBLE);
        }
        rv = (RecyclerView) view.findViewById(R.id.recyclerHistory);  /// shoof bnull leeh
        cvh = new CardViewHist(getActivity(),historyTrips);
        Log.i("yarab",rv+"");
        Log.i("yarab",historyTrips+"");
        Log.i("yarab",cvh+"");
        rv.setAdapter(cvh);
        rv.setLayoutManager(new LinearLayoutManager(getActivity()));

        return view;
    }

    // TODO: Rename method, update argument and hook method into UI event
    public void onButtonPressed(Uri uri) {
        if (mListener != null) {
            mListener.onFragmentInteraction(uri);
        }
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        if (context instanceof OnFragmentInteractionListener) {
            mListener = (OnFragmentInteractionListener) context;
        } else {
            throw new RuntimeException(context.toString()
                    + " must implement OnFragmentInteractionListener");
        }

    }

    @Override
    public void onDetach() {
        super.onDetach();
        mListener = null;
    }

    /**
     * This interface must be implemented by activities that contain this
     * fragment to allow an interaction in this fragment to be communicated
     * to the activity and potentially other fragments contained in that
     * activity.
     * <p>
     * See the Android Training lesson <a href=
     * "http://developer.android.com/training/basics/fragments/communicating.html"
     * >Communicating with Other Fragments</a> for more information.
     */
    public interface OnFragmentInteractionListener {
        // TODO: Update argument type and name
        void onFragmentInteraction(Uri uri);
    }
}
