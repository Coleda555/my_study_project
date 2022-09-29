from requests import Session

def get_response():
    with Session() as session:
        session.headers.update(
            {
                'Accept-Languae': 'ru',
                'Accept-Encoding': 'utf-8'

            }
        )
        responce = session.get()