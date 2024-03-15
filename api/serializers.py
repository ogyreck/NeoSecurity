from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import serializers

from workers.models import Grade, Group, Worker, Document, WorkerGroup

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'name', 'priority']


class DocumentSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = Document
        fields = [
            'id',
            'name',
            'groups',
            'created_at',
            'updated_at',
        ]


class DocumentCreateSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

    class Meta:
        model = Document
        fields = [
            'name',
            'groups',
        ]


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = Worker
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'groups'
        ]

    def get_groups(self, obj):
        groups = WorkerGroup.objects.filter(worker=obj)
        return CustomUserSerializer(groups, many=True).data


class AddGroupWorkerSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())
    grade = serializers.PrimaryKeyRelatedField(many=True, queryset=Grade.objects.all())

    class Meta:
        model = WorkerGroup
        fields = ['group', 'grade']
    class

class CustomUserCreateSerializer(UserCreateSerializer):
    groups = AddGroupWorkerSerializer(many=True)

    class Meta:
        model = Worker
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'groups',
        ]
    @staticmethod
    def create_groups(groups, worker):
        for group in groups:
            RecipeIngredient.objects.create(
                ingredient_id=ingredient['id'],
                recipe=recipe,
                amount=ingredient['amount']
            )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        self.create_ingredients(
            recipe=recipe,
            ingredients=ingredients
        )
        return recipe