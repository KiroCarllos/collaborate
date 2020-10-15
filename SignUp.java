package com.example.delllaptop.projone;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class SignUp extends AppCompatActivity {

    private FirebaseAuth mAuth;
    private Button signupbut;
    private Button loginbut;
    private EditText email;
    private EditText password;
    String TAG = "sign";
    SharedPreferences saving;
    SharedPreferences.Editor edit;
    public static final String saveData="NewData";
    public static final String newLogin="NewLogin";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        mAuth = FirebaseAuth.getInstance();
        signupbut = findViewById(R.id.signupreg);
        loginbut = findViewById(R.id.signuplog);
        email = findViewById(R.id.signupmail);
        password = findViewById(R.id.signuppass);
        signupbut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String mail = email.getText().toString();
                String pass = password.getText().toString();
                if(!mail.isEmpty() && !pass.isEmpty()){
                    mAuth.createUserWithEmailAndPassword(mail, pass)
                            .addOnCompleteListener(SignUp.this, new OnCompleteListener<AuthResult>() {
                                @Override
                                public void onComplete(@NonNull Task<AuthResult> task) {
                                    if (task.isSuccessful()) {
                                        // Sign in success, update UI with the signed-in user's information
                                        Log.d(TAG, "createUserWithEmail:success");
                                        FirebaseUser user = mAuth.getCurrentUser();
                                        Intent intent = new Intent(SignUp.this,Welcome.class);
                                        saving = getApplicationContext().getSharedPreferences(saveData, 0);
                                        edit = saving.edit();
                                        edit.putBoolean(newLogin,true);
                                        edit.putString("user",user.getEmail());
                                        edit.putString("userid",user.getUid());
                                        Log.i("user",user.getUid());
                                        edit.commit();
                                        startActivity(intent);
                                        finish();

                                    } else {
                                        // If sign in fails, display a message to the user.
                                        Log.w(TAG, "createUserWithEmail:failure", task.getException());
                                        Toast.makeText(SignUp.this, "Authentication failed.",
                                                Toast.LENGTH_SHORT).show();
                                    }
                                }
                            });
                }
                else {
                    Toast.makeText(SignUp.this,"Please enter valid username and password",Toast.LENGTH_SHORT).show();
                }
            }
        });
        loginbut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(SignUp.this, Login.class);
                startActivity(intent);
                finish();
            }
        });
    }
}
