from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

authorized_users = {
    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash('wonderland'),
    },
    "bob" : {
        "username" :  "bob",
        "hashed_password" : pwd_context.hash('builder'),
    },
    "clementine" : {
        "username" :  "clementine",
        "hashed_password" : pwd_context.hash('mandarine'),
    },
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash('4dm1N '),
    }
}
