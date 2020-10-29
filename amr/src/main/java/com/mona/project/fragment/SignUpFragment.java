package com.mona.project.fragment;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import com.google.android.gms.auth.api.Auth;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.auth.api.signin.GoogleSignInResult;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;
import com.mona.project.R;
import com.mona.project.TripDetails;
import com.mona.project.model.User;

import static android.content.Context.MODE_PRIVATE;

public class SignUpFragment extends Fragment implements GoogleApiClient.OnConnectionFailedListener, View.OnClickListener {
    EditText etSignupEmail, etSignupPassword, etUserName;
    Button btnSignup, btnSignUpWithGoogle;
    String name, email, password, googleName, googleEmail;
    private static final String TAG = "EmailPassword";
    GoogleApiClient googleApiClient;
    private static final int GOOGLE_SIGNUP = 8007;
    private FirebaseAuth mAuth;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.signup_fragment, container, false);
        btnSignup = view.findViewById(R.id.btnSignup);
        btnSignUpWithGoogle = view.findViewById(R.id.btnSignUpWithGoogle);
        etUserName = (EditText) view.findViewById(R.id.etUserName);
        etSignupEmail = (EditText) view.findViewById(R.id.etSignupEmail);
        etSignupPassword = (EditText) view.findViewById(R.id.etSignupPassword);

        mAuth = FirebaseAuth.getInstance();

        btnSignup.setOnClickListener(this);
        btnSignUpWithGoogle.setOnClickListener(this);

        GoogleSignInOptions signInOptions = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN).requestEmail().build();
        googleApiClient = new GoogleApiClient.Builder(getActivity()).enableAutoManage(getActivity(), this)
                .addApi(Auth.GOOGLE_SIGN_IN_API, signInOptions).build();

        return view;
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.btnSignUpWithGoogle:
                signupWithGoogle();
                break;
            case R.id.btnSignup:
                signup();
                break;
        }
    }

    private void signup() {
        name = etUserName.getText().toString().trim();
        email = etSignupEmail.getText().toString().trim();
        password = etSignupPassword.getText().toString().trim();
        if (TextUtils.isEmpty(name) && !TextUtils.isEmpty(email) && !TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "User Name Required", Toast.LENGTH_SHORT).show();
        } else if (!TextUtils.isEmpty(name) && TextUtils.isEmpty(email) && !TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "Email Required", Toast.LENGTH_SHORT).show();
        } else if (!TextUtils.isEmpty(name) && !TextUtils.isEmpty(email) && TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "Password Required", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(name) && TextUtils.isEmpty(email) && !TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "User Name & Email Required", Toast.LENGTH_SHORT).show();
        } else if (!TextUtils.isEmpty(name) &&TextUtils.isEmpty(email) && TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "Email & Password Required", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(name)&& !TextUtils.isEmpty(email) && TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "User Name & Password Required", Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(name) && TextUtils.isEmpty(email) && TextUtils.isEmpty(password)) {
            Toast.makeText(getContext(), "User Name, Email & Password Required", Toast.LENGTH_SHORT).show();
        } else if (!TextUtils.isEmpty(name) && !TextUtils.isEmpty(email) && !TextUtils.isEmpty(password)) {
            (mAuth.createUserWithEmailAndPassword(etSignupEmail.getText().toString().trim(), etSignupPassword.getText().toString().trim()))
                    .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if (task.isSuccessful()) {
                                Toast.makeText(getContext(), "SignUp Successful", Toast.LENGTH_SHORT).show();
                                User user = new User();
                                user.setName(name);
                                user.setEmail(email);
                                insertIntoFirebase(user);
                                isLogged();
                            } else {
                                // If sign in fails, display a message to the user.
                                Log.i(TAG, "createUserWithEmail:failure", task.getException());
                                Toast.makeText(getContext(), "Authentication failed.", Toast.LENGTH_LONG).show();
                            }
                        }
                    });
        }

    }

    private void signupWithGoogle() {
        Intent google = Auth.GoogleSignInApi.getSignInIntent(googleApiClient);
        startActivityForResult(google, GOOGLE_SIGNUP);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == GOOGLE_SIGNUP) {
            GoogleSignInResult result = Auth.GoogleSignInApi.getSignInResultFromIntent(data);
            handleSignInResult(result);
        }
    }

    private void handleSignInResult(GoogleSignInResult result) {
        if (result.isSuccess()) {
            GoogleSignInAccount signInAccount = result.getSignInAccount();
            googleName = signInAccount.getDisplayName();
            googleEmail = signInAccount.getEmail();
            User user = new User();
            if (!TextUtils.isEmpty(googleName) && !TextUtils.isEmpty(googleEmail)) {
                user.setName(googleName);
                user.setEmail(googleEmail);
                insertIntoFirebase(user);
                isLogged();
            }

        }
    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {
    }

    public void insertIntoFirebase(User user) {
        FirebaseDatabase.getInstance().getReference("Users")
                .child(FirebaseAuth.getInstance().getCurrentUser().getUid()).push()
                .setValue(user).addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Toast.makeText(getContext(), "SignUp Successful", Toast.LENGTH_SHORT).show();
                    Log.i(TAG, "createUserWithEmail:success");
                    /*TripDetails tripDetails = new TripDetails();
                    FragmentManager manager = getFragmentManager();
                    manager.beginTransaction().replace(R.id.container, tripDetails).commit();*/
                    UpCommingFragment upCommingFragment = new UpCommingFragment();
                    FragmentManager manager = getFragmentManager();
                    manager.beginTransaction().replace(R.id.container, upCommingFragment).commit();
                } else {
                    Log.i(TAG, "createUserWithEmail:failure", task.getException());
                    Toast.makeText(getContext(), "SignUp failed.", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    public void isLogged() {
        SharedPreferences.Editor editor = getContext().getSharedPreferences("login", MODE_PRIVATE).edit();
        editor.putBoolean("isLoggedIn", true);
        editor.commit();
    }
}
