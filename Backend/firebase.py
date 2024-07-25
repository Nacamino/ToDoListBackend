import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./Credentials/todolist-90121-firebase-adminsdk-rjj3a-3be5ccf854.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def agregar_nuevo_documento_con_id_automatico():
    
    collection_ref = db.collection('ToDo').document("01072024")
    
    collection_ref.set({
        'Nombre': 'Ema Perez',
        'Frecuencia': 'Alta',
        'Id': "4",
        "Estado": "Completada",
        "Observacion" : "Test",
        "Prioridad": "Alta",
        "Recordatorio": False
    })

agregar_nuevo_documento_con_id_automatico()


def EliminarRegistro(id):
    try:
      
        collection_ref = db.collection('ToDo').document(id)
        collection_ref.delete()
        
        print(f"Documento con ID {id} eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el registro: {e}")

EliminarRegistro("34234sdfsd")


def LeerRegistros():
    try:
        collection_ref = db.collection('ToDo')
        registros = collection_ref.stream()
        
        for regi in registros:
            print(f"{regi.to_dict()}")
            
    except Exception as e:
        print(f"Error al leer los registros: {e}")

LeerRegistros()

