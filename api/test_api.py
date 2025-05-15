import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.models import Category, Item

@pytest.mark.django_db
def test_create_category():
    user = User.objects.create_user(username="testuser", password="testpassword")
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post("/api/v1/categories/", {"name": "Test Category"})
    assert response.status_code == 201
    assert Category.objects.count() == 1
    assert Category.objects.get(name="Test Category").name == "Test Category"
