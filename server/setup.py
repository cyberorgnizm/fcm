import firebase_admin
from firebase_admin import messaging


def init_firebase():
    default_app = firebase_admin.initialize_app()
    
    # send message
    message = messaging.Message(
        data={
            "score": '850',
            "time": '2:45'
        },
        topic='highScores'
    )

    response = messaging.send(message)

    print('Successfully sent message:', response)