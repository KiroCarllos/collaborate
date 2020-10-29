package com.mona.project.fragment;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.mona.project.R;
import com.mona.project.TripDetails;

import static android.content.Context.MODE_PRIVATE;

public class LogInFragment extends Fragment {
    private FirebaseAuth mAuth;
    EditText etLoginEmail, etLoginPassword;
    String loginEmail, loginPassword;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.login_fragment, container, false);
        TextView tvSignUpHere = view.findViewById(R.id.tvSignUpHere);
        Button btnLogin = view.findViewById(R.id.btnLogin);
        etLoginEmail = (EditText) view.findViewById(R.id.etLoginEmail);
        etLoginPassword = (EditText) view.findViewById(R.id.etLoginPassword);

        mAuth = FirebaseAuth.getInstance();

        tvSignUpHere.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SignUpFragment signUpFragment = new SignUpFragment();
                FragmentManager manager = getFragmentManager();
                manager.beginTransaction().replace(R.id.container, signUpFragment).addToBackStack(null).commit();
            }
        });
        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                /*Intent i = new Intent(getActivity(), MainActivity2.class);
                startActivity(i);
                ((Activity) getActivity()).overridePendingTransition(0, 0);*/
                loginEmail = etLoginEmail.getText().toString().trim();
                loginPassword = etLoginPassword.getText().toString().trim();
                if (TextUtils.isEmpty(loginEmail) && !TextUtils.isEmpty(loginPassword)) {
                    Toast.makeText(getContext(), "Email Required", Toast.LENGTH_SHORT).show();
                }else if (!TextUtils.isEmpty(loginEmail) &&TextUtils.isEmpty(loginPassword)) {
                    Toast.makeText(getContext(), "Password Required", Toast.LENGTH_SHORT).show();
                } else if (TextUtils.isEmpty(loginEmail) && TextUtils.isEmpty(loginPassword)) {
                    Toast.makeText(getContext(), "Email & Password Required", Toast.LENGTH_SHORT).show();
                } else {
                    (mAuth.signInWithEmailAndPassword(loginEmail, loginPassword))
                            .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                                @Override
                                public void onComplete(@NonNull Task<AuthResult> task) {
                                    if (task.isSuccessful()) {
                                        Toast.makeText(getContext(), "LogIn Successful", Toast.LENGTH_LONG).show();
                                        UpCommingFragment upCommingFragment = new UpCommingFragment();
                                        FragmentManager manager = getFragmentManager();
                                        manager.beginTransaction().replace(R.id.container, upCommingFragment).addToBackStack(null).commit();
                                        //mAuth.getCurrentUser().getEmail();
                                    } else {
                                        Toast.makeText(getContext(), "LogIn Failed", Toast.LENGTH_LONG).show();
                                    }
                                }
                            });
                    isLogged();
                }
            }
        });
        return view;
    }

    public void isLogged() {
        SharedPreferences.Editor editor = getContext().getSharedPreferences("login", MODE_PRIVATE).edit();
        editor.putBoolean("isLoggedIn", true);
        editor.commit();
    }
}
