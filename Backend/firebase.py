import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./Credentials/todolist-90121-firebase-adminsdk-rjj3a-3be5ccf854.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# def agregar_datos():
#     # Referencia a la colección y documento
#     doc_ref = db.collection('ToDo').document('Tarea')
    
#     # Datos que deseas agregar
#     doc_ref.set({
#         'Nombre': 'Juan Perez',
#         'Frecuencia': 'Alta',
#         'Id': "3",
#         "Estado": "Completada",
#         "Observacion" : "putos todos",
#         "Prioridad": "Alta",
#         "Recordatorio": False
#     })

def agregar_nuevo_documento_con_id_automatico():
    # Referencia a la colección
    collection_ref = db.collection('ToDo').document("tarea062924")
    
    # Datos que deseas agregar
    collection_ref.set({
        'Nombre': 'Juan Perez',
        'Frecuencia': 'Alta',
        'Id': "4",
        "Estado": "Completada",
        "Observacion" : "putos todos",
        "Prioridad": "Alta",
        "Recordatorio": False
    })

    # Agrega el documento con un ID generado automáticamente
    # collection_ref.add(nuevo_documento)

agregar_nuevo_documento_con_id_automatico()
# agregar_datos()

# // const onSignClick = () => {

# //     firebase.auth().signInWithPopup(provider).then(function (result) {
# //         // This gives you a Google Access Token. You can use it to access the Google API.
# //         var token = result.credential.accessToken;
# //         console.log(token)
# //         // The signed-in user info.
# //         var user = result.user;
# //         console.log(user)
# //         // Save user to Firestore
# //         db.collection('Users').doc(user.uid).set({
# //             name: user.displayName,
# //             email: user.email,
# //             photoURL: user.photoURL,  // Add this line
# //         })
# //             .then(() => {
# //                 console.log("Document successfully written!");
# //             })
# //             .catch((error) => {
# //                 console.error("Error writing document: ", error);
# //             });
# //         // ...
# //     }).catch(function (error) {
# //         // Handle Errors here.
# //         var errorCode = error.code;
# //         var errorMessage = error.message;
# //         // The email of the user's account used.
# //         var email = error.email;
# //         // The firebase.auth.AuthCredential type that was used.
# //         var credential = error.credential;
# //         // ...
# //     });
# // }

# // firebase.auth().onAuthStateChanged(function (user) {
# //     if (user) {
# //         console.log('User is signed in');
# //         document.getElementById("googleSignInButton").style.display = "none"
# //         // user is signed in, you can get user information like this
# //         console.log(user.email, user.displayName);
# //         userUid = user.uid;
# //     } else {
# //         console.log('No user is signed in');
# //     }
# // });

# // document.getElementById("googleSignInButton").addEventListener("click", onSignClick)