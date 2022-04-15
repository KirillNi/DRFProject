import graphene
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldError
from django.db.models import Q
from graphene_django import DjangoObjectType
from projects.models import Project, ToDo


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


def get_object_by_field(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def camelcase_to_snake_case(word: str) -> str:
    result = ''
    for char in word:
        if char.isupper():
            result += f'_{char.lower()}'
        else:
            result += char
    return result


def get_objects_order_by(model, order):
    if order is None:
        return model.objects.all()

    order = camelcase_to_snake_case(order)
    try:
        return model.objects.all().order_by(order)
    except FieldError:
        return None


class Query(graphene.ObjectType):
    get_projects = graphene.List(ProjectType, order=graphene.String())
    get_todos = graphene.List(ToDoType, order=graphene.String())
    get_users = graphene.List(UserType, order=graphene.String())
    search_project_by_name = graphene.List(ProjectType, name=graphene.String(required=True))
    search_todo_by_project = graphene.List(ToDoType, name=graphene.String(required=True))
    search_user_by_name = graphene.List(UserType, name=graphene.String(required=True))

    def resolve_get_projects(self, info, order=None):
        return get_objects_order_by(model=Project, order=order)

    def resolve_get_todos(self, info, order=None):
        return get_objects_order_by(model=ToDo, order=order)

    def resolve_get_users(self, info, order=None):
        return get_objects_order_by(model=get_user_model(), order=order)

    def resolve_search_project_by_name(self, info, name):
        return Project.objects.filter(name__contains=name)

    def resolve_search_todo_by_project(self, info, name):
        return ToDo.objects.filter(project__name__contains=name)

    def resolve_search_user_by_name(self, info, name):
        return get_user_model().objects.filter(Q(first_name__contains=name))


schema = graphene.Schema(query=Query)
