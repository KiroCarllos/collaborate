package com.mona.project.fragment;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.mona.project.R;

import java.util.ArrayList;

public class NotesFragment extends Fragment {
    //region intialization
    LinearLayout Layout1, Layout2, Layout3, Layout4, Layout5, Layout6, Layout7, Layout8, Layout9, Layout10;
    Button buSaveNotes;
    Button add1, add2, add3, add4, add5, add6, add7, add8, add9, add10;
    Button cancel1, cancel2, cancel3, cancel4, cancel5, cancel6, cancel7, cancel8, cancel9, cancel10;
    EditText edit1, edit2, edit3, edit4, edit5, edit6, edit7, edit8, edit9, edit10;
    /*String note1, note2, note3, note4, note5, note6, note7, note8, note9, note10;
    ArrayList<String> list = new ArrayList<>();*/

    //endregion
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.notes_fragment, container, false);

        Layout1 = view.findViewById(R.id.addnoteItem1);
        Layout2 = view.findViewById(R.id.addnoteItem2);
        Layout3 = view.findViewById(R.id.addnoteItem3);
        Layout4 = view.findViewById(R.id.addnoteItem4);
        Layout5 = view.findViewById(R.id.addnoteItem5);
        Layout6 = view.findViewById(R.id.addnoteItem6);
        Layout7 = view.findViewById(R.id.addnoteItem7);
        Layout8 = view.findViewById(R.id.addnoteItem8);
        Layout9 = view.findViewById(R.id.addnoteItem9);
        Layout10 = view.findViewById(R.id.addnoteItem10);
        buSaveNotes = view.findViewById(R.id.buSaveNotes);
        add1 = view.findViewById(R.id.ItemAddNoteBtn1);
        add2 = view.findViewById(R.id.ItemAddNoteBtn2);
        add3 = view.findViewById(R.id.ItemAddNoteBtn3);
        add4 = view.findViewById(R.id.ItemAddNoteBtn4);
        add5 = view.findViewById(R.id.ItemAddNoteBtn5);
        add6 = view.findViewById(R.id.ItemAddNoteBtn6);
        add7 = view.findViewById(R.id.ItemAddNoteBtn7);
        add8 = view.findViewById(R.id.ItemAddNoteBtn8);
        add9 = view.findViewById(R.id.ItemAddNoteBtn9);
        add10 = view.findViewById(R.id.ItemAddNoteBtn10);
        cancel1 = view.findViewById(R.id.ItemDelNoteBtn1);
        cancel2 = view.findViewById(R.id.ItemDelNoteBtn2);
        cancel3 = view.findViewById(R.id.ItemDelNoteBtn3);
        cancel4 = view.findViewById(R.id.ItemDelNoteBtn4);
        cancel5 = view.findViewById(R.id.ItemDelNoteBtn5);
        cancel6 = view.findViewById(R.id.ItemDelNoteBtn6);
        cancel7 = view.findViewById(R.id.ItemDelNoteBtn7);
        cancel8 = view.findViewById(R.id.ItemDelNoteBtn8);
        cancel9 = view.findViewById(R.id.ItemDelNoteBtn9);
        cancel10 = view.findViewById(R.id.ItemDelNoteBtn10);
        edit1 = view.findViewById(R.id.addNoteText1);
        edit2 = view.findViewById(R.id.addNoteText2);
        edit3 = view.findViewById(R.id.addNoteText3);
        edit4 = view.findViewById(R.id.addNoteText4);
        edit5 = view.findViewById(R.id.addNoteText5);
        edit6 = view.findViewById(R.id.addNoteText6);
        edit7 = view.findViewById(R.id.addNoteText7);
        edit8 = view.findViewById(R.id.addNoteText8);
        edit9 = view.findViewById(R.id.addNoteText9);
        edit10 = view.findViewById(R.id.addNoteText10);
        //endregion

        //region CancelButtons
        cancel1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit1.setText("");
            }
        });
        cancel2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit2.setText("");
            }
        });
        cancel3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit3.setText("");
            }
        });
        cancel4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit4.setText("");
            }
        });
        cancel5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit5.setText("");
            }
        });
        cancel6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit6.setText("");
            }
        });
        cancel7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit7.setText("");
            }
        });
        cancel8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit8.setText("");
            }
        });
        cancel9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit9.setText("");
            }
        });
        cancel10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                edit10.setText("");
            }
        });
        //endregion

        //region addButtons
        add1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout2.setVisibility(View.VISIBLE);
            }
        });
        add2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout3.setVisibility(View.VISIBLE);
            }
        });
        add3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout4.setVisibility(View.VISIBLE);
            }
        });

        add4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout5.setVisibility(View.VISIBLE);
            }
        });

        add5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout6.setVisibility(View.VISIBLE);
            }
        });

        add6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout7.setVisibility(View.VISIBLE);
            }
        });

        add7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout8.setVisibility(View.VISIBLE);
            }
        });

        add8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout9.setVisibility(View.VISIBLE);
            }
        });

        add9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Layout10.setVisibility(View.VISIBLE);
            }
        });

        add10.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
        //endregion

        /*note1 = edit1.getText().toString().trim();
        note2 = edit2.getText().toString().trim();
        note3 = edit3.getText().toString().trim();
        note4 = edit4.getText().toString().trim();
        note5 = edit5.getText().toString().trim();
        note6 = edit6.getText().toString().trim();
        note7 = edit7.getText().toString().trim();
        note8 = edit8.getText().toString().trim();
        note9 = edit9.getText().toString().trim();
        note10 = edit10.getText().toString().trim();*/

        /*if (!TextUtils.isEmpty(note1)) {
            list.add(note1);
        }
        if (!TextUtils.isEmpty(note2)) {
            list.add(note2);
        }
        if (!TextUtils.isEmpty(note3)) {
            list.add(note3);
        }
        if (!TextUtils.isEmpty(note4)) {
            list.add(note4);
        }
        if (!TextUtils.isEmpty(note5)) {
            list.add(note5);
        }
        if (!TextUtils.isEmpty(note6)) {
            list.add(note6);
        }
        if (!TextUtils.isEmpty(note7)) {
            list.add(note7);
        }
        if (!TextUtils.isEmpty(note8)) {
            list.add(note8);
        }
        if (!TextUtils.isEmpty(note9)) {
            list.add(note9);
        }
        if (!TextUtils.isEmpty(note10)) {
            list.add(note10);
        }*/

        //region saveNotes
        /*buSaveNotes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Bundle bundle=new Bundle();
                bundle.putString("note1",note1);
                bundle.putString("note2",note2);
                bundle.putString("note3",note3);
                bundle.putString("note4",note4);
                bundle.putString("note5",note5);
                bundle.putString("note6",note6);
                bundle.putString("note7",note7);
                bundle.putString("note8",note8);
                bundle.putString("note9",note9);
                bundle.putString("note10",note10);

                TripFragment tripFragment=new TripFragment();
                tripFragment.setArguments(bundle);
            }
        });*/
        //endregion

        return view;
    }
}
