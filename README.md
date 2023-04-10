# Simple Chat

## Installation:

```commndline
pip install django
pip instll djangorestframework
pip instll djangorestframework_simplejwt
```

## How to run

First of all we need to create migrations
```commandline
python manage.py makemigrations
python manage.py migrate
```
Next step we need to create superuser

```commandline
python manage.py createsuperuser
```

And the last one run the server

```commandline
python manage.py runserver
```


## How to use

### In order to add user you need to move to django admin with link: 

[your server address]/admin/

Fill all field with superuser login and password you created earlier

And then, if you want to add new user just press the button Add user

### To create thread just use this link

[your server address]/chat/thread/

and create post request with this data

{
    "user1": "[user1 username]",
    "user2": "[user2 username]"
}

if thread with this users already exists you'll just get this thread back

### To delete thread just use this link
[your server address]/chat/thread/[thread id]/

and make delete request

### To get threads for user just use this link

[your server address]/chat/user/<user id>/thread/

### To create or get messages for thread

[your server address]/thread/[thread id]/message/

And fill with this data

{
"messages":

[

{
    "sender": [user_id who sent the message],
    "text": "test"
},

{
    "sender": [user_id who sent the message],
    "text": "second test"
}, ...[you may add many messages in one request]

]

}


### To Mark messages as read

[your server address]/message/

and fill with messages ids 

{
 "messages_ids": [] in this list you should leave message ids to mark as read
}

### To get number of unread messages

[your server address]/user/[user id]/message/



