# Simple Chat
## Installation:

```
pip install django
pip install djangorestframework
pip install djangorestframework_simplejwt
```

## How to Run

First, we need to create migrations:

```commandline
python manage.py makemigrations
python manage.py migrate
```

Next, we need to create a superuser:

```commandline

python manage.py createsuperuser

```

Finally, run the server:

```commandline

python manage.py runserver

```

## How to Use

### Add User

To add a user, go to the Django admin page by navigating to [your server address]/admin/. Fill in all fields with the superuser login and password you created earlier. Then, if you want to add a new user, click the "Add User" button.
### Create Thread

To create a thread, use the following link: [your server address]/chat/thread/. Create a POST request with the following data:

```json

{
    "user1": "[user1 username]",
    "user2": "[user2 username]"
}
```

If a thread with these users already exists, the existing thread will be returned.
### Delete Thread

To delete a thread, use the following link: [your server address]/chat/thread/[thread id]/. Make a DELETE request.
### Get Threads for User

To get threads for a user, use the following link: [your server address]/chat/user/[user id]/thread/.
### Create or Get Messages for Thread

To create or get messages for a thread, use the following link: [your server address]/thread/[thread id]/message/.

Fill the request with the following data:

```json

{
    "messages": [
        {
            "sender": [user_id who sent the message],
            "text": "test"
        },
        {
            "sender": [user_id who sent the message],
            "text": "second test"
        }
    ]
}

```

You may add multiple messages in one request.
### Mark Messages as Read

To mark messages as read, use the following link: [your server address]/message/. Fill the request with the message IDs to mark as read:

```json

{
    "messages_ids": [1, 2, 3]
}
```

### Get Number of Unread Messages

To get the number of unread messages, use the following link: [your server address]/user/[user id]/message/.
