REST API for Cats web app

## Installation
1. Clone repo to your local machine <br />
2. Add .env file with these data: <br />

```
SECRET_KEY=your_secret_key
DEBUG=TRUE OR FALSE(Default)
DATABASE_URL=postgres://{dbusername}:{password}@db:5432/{dbname}
```
3. Build docker with command: <br />
`docker-compose up --build`

Then you are ready to go!)

### Swagger Documentation URL: <br />
http://127.0.0.1:8000/swagger/


#### Inital data that project create so you can test it:
\
Admin:
`username='admin'`
`email='admin@example.com'`
`password='adminpass'` <br />
User1:
`username='ordinary_user1'`
`email='user1@example.com'`
`password='password1'` <br />
User2:
`username='ordinary_user2'`
`email='user2@example.com'`
`password='password2'`

Breeds: `Siamese`, `Persian` <br />
Cats: `Whiskers`, `Fluffy`
