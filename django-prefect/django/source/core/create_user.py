from django.contrib.auth.models import User
from prefect import flow, task
from prefect.task_worker import serve

mock_user_data = [
    {
        "username": "testuser1",
        "email": "testuser@email.com"
        "first_name": "Test",
        "last_name": "User",
    },
    {
        "username": "testuser2",
        "email": "testuser2@email.com",
        "first_name": "Test2",
        "last_name": "User2",
    }
]


@task(name="create_user", retries=3)
def create_user(user_data):
    user = User.objects.create_user(username=user_data["username"])
    return update_profile(user)


@task(name="update_profile", retries=3)
def update_profile(user):
    for key, value in user.items():
        if key == "username":
            continue
        if hasattr(user, key):
            setattr(user, key, value)

    user.save()

    return user


@flow(name="create_users_flow")
def create_users_flow(user):
    for user_data in mock_user_data:
        if user.get('username') and user.get('username') == user_data['username']:
            create_user(user_data)


if __name__ == "__main__":
    serve(create_users_flow)
