package com.example.delllaptop.projone;

import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.pm.Signature;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.CallbackManager;
import com.facebook.FacebookCallback;
import com.facebook.FacebookException;
import com.facebook.GraphRequest;
import com.facebook.GraphResponse;
import com.facebook.login.LoginResult;
import com.facebook.login.widget.LoginButton;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FacebookAuthProvider;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import org.json.JSONException;
import org.json.JSONObject;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;

public class Login extends AppCompatActivity {

    SharedPreferences saving;
    String TAG = "sign";
    SharedPreferences.Editor edit;
    public static final String saveData="NewData";
    public static final String newLogin="NewLogin";
    private EditText email;
    private EditText password;
    private Button login;
    private Button forgot;
    private Button signup;
    private FirebaseAuth mAuth;
    CallbackManager callbackManager;

    private FirebaseAuth.AuthStateListener mListener;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        email = findViewById(R.id.signinmail);
        password = findViewById(R.id.signinpass);
        login = findViewById(R.id.signin);
        forgot = findViewById(R.id.signinfor);
        signup = findViewById(R.id.signinreg);
        mAuth = FirebaseAuth.getInstance();
        login.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View v) {
                 String mail = email.getText().toString();
                 String pass = password.getText().toString();
                 if (!mail.isEmpty() && !pass.isEmpty()) {
                     mAuth.signInWithEmailAndPassword(mail,pass).addOnCompleteListener(Login.this, new OnCompleteListener<AuthResult>() {
                         @Override
                         public void onComplete(@NonNull Task<AuthResult> task) {
                             if (task.isSuccessful()) {
                                 // Sign in success, update UI with the signed-in user's information
                                 Log.d(TAG, "createUserWithEmail:success");
                                 FirebaseUser user = mAuth.getCurrentUser();
                                 Intent intent = new Intent(Login.this,Welcome.class);
                                 saving = getApplicationContext().getSharedPreferences(saveData, 0);
                                 edit = saving.edit();
                                 edit.putBoolean(newLogin,true);
                                 edit.putString("user",user.getEmail());
                                 edit.putString("userid",user.getUid());
                                 Log.i("user",user.getUid());
                                 Log.i("user",user.getEmail());
                                 edit.commit();
                                 startActivity(intent);
                                 finish();

                             } else {
                                 // If sign in fails, display a message to the user.
                                 Log.w(TAG, task.getException());
                                 Toast.makeText(Login.this, "Authentication failed.",
                                         Toast.LENGTH_SHORT).show();
                             }
                         }
                     });
                 }
                 else{
                     Toast.makeText(Login.this,"Please enter valid username and password",Toast.LENGTH_SHORT).show();
                 }
             }
         });
        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Login.this, SignUp.class);
                startActivity(intent);
                finish();
            }
        });
        forgot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String mail = email.getText().toString();
                if (!mail.isEmpty()){
                    mAuth.sendPasswordResetEmail(mail).addOnCompleteListener(new OnCompleteListener<Void>() {
                        @Override
                        public void onComplete(@NonNull Task<Void> task) {
                            if (task.isSuccessful()) {
                                Toast.makeText(Login.this, "Instructions have been sent to your E-mail.",
                                        Toast.LENGTH_LONG).show();
                            } else {
                                // If sign in fails, display a message to the user.
                                Log.w(TAG, task.getException());
                                Toast.makeText(Login.this, "This E-mail is not registered.",
                                        Toast.LENGTH_SHORT).show();
                            }

                        }
                    });
            }
            }
        });

        callbackManager=CallbackManager.Factory.create();
        final LoginButton loginButton = (LoginButton)findViewById(R.id.login_button);
        loginButton.setReadPermissions(Arrays.asList("public_profile","email","user_birthday"));
        loginButton.registerCallback(callbackManager, new FacebookCallback<LoginResult>() {
            @Override
            public void onSuccess(final LoginResult loginResult) {
                Toast.makeText(Login.this,"Please wait for loading",Toast.LENGTH_LONG).show();
                //  getUserDetails(loginResult);
                Log.i("hi","Hello"+loginResult.getAccessToken().getToken());

                GraphRequest data_request = GraphRequest.newMeRequest(loginResult.getAccessToken(), new GraphRequest.GraphJSONObjectCallback() {      @Override
                public void onCompleted(JSONObject json_object, GraphResponse response) {
                    Intent intent = new Intent(Login.this, Welcome.class);
                    intent.putExtra("userProfile", json_object.toString());
                    intent.putExtra("user",loginResult.getAccessToken().getUserId() );
                    saving = getApplicationContext().getSharedPreferences(saveData, 0);
                    edit = saving.edit();
                    edit.putBoolean(newLogin,true);
                    try {
                        edit.putString("user" , json_object.getString("email"));

                        Log.i("user",json_object.getString("email"));
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    handleFacebookAccessToken(loginResult.getAccessToken(),intent);
                    edit.commit();

                }
                });
                Bundle permission_param = new Bundle();
                permission_param.putString("fields", "id,name,email,picture.width(120).height(120)");
                data_request.setParameters(permission_param);
                data_request.executeAsync();


            }

            @Override
            public void onCancel() {

            }

            @Override
            public void onError(FacebookException error) {

            }
        });
        mListener = new FirebaseAuth.AuthStateListener(){
            @Override
            public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
                FirebaseUser user = firebaseAuth.getCurrentUser();
                if (user!=null){
                    //Toast.makeText(Login.this,"fireBase User"+user.getDisplayName(),Toast.LENGTH_LONG).show();
                }else {
                    Toast.makeText(Login.this,"something went wrong",Toast.LENGTH_LONG).show();
                }
            }
        };
    }

    private void handleFacebookAccessToken(final AccessToken accessToken, final Intent intent) {
        Log.d("hiii", "handleFacebookAccessToken:" + accessToken);
        AuthCredential credential = FacebookAuthProvider.getCredential(accessToken.getToken());
        mAuth.signInWithCredential(credential).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {

                    Log.w("hi", "signInWithCredential", task.getException());
                    edit.putString("userid",mAuth.getCurrentUser().getUid());
                    startActivity(intent);
                    finish();

                    Toast.makeText(Login.this, "Success", Toast.LENGTH_SHORT).show();


                }else{
                    Toast.makeText(Login.this, "Authentication error", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        callbackManager.onActivityResult(requestCode, resultCode, data);

    }

}
