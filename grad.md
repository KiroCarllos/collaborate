apply plugin: 'com.android.application'

android {
    compileSdkVersion 30
    buildToolsVersion "30.0.1"

    defaultConfig {
        applicationId "com.mona.project"
        minSdkVersion 21
        targetSdkVersion 30
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

apply plugin: 'com.google.gms.google-services'

dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar"])
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.0.1'
    implementation 'androidx.cardview:cardview:1.0.0'
    implementation 'com.google.android.gms:play-services-auth:18.1.0'
    implementation 'com.google.android.libraries.places:places:2.4.0'
    //google - maps
    implementation 'com.google.android.gms:play-services-places:16.0.0'
    implementation 'com.google.android.gms:play-services-location:17.1.0'
    implementation 'com.google.android.gms:play-services-maps:17.0.0'
    implementation 'com.google.android.material:material:1.2.1'
    //implementation 'com.google.firebase:firebase-database:19.2.0'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'androidx.test.ext:junit:1.1.2'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.3.0'
    implementation platform('com.google.firebase:firebase-bom:25.12.0')
    implementation 'com.google.firebase:firebase-analytics'
    implementation 'com.google.android.gms:play-services-auth:9.6.1'
    implementation 'com.google.firebase:firebase-auth'
    implementation 'com.google.firebase:firebase-database:19.5.0'

}