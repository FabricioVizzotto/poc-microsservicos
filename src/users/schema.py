import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from users.models import Profile
from django.contrib.auth.models import User, Group

class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = {
            'user__username':['exact','icontains','istartswith'],
            'user__email':['exact'],
            'groups__name':['exact'],
            'groups':['exact'],
        }
        interfaces = (relay.Node, )


class GroupNode(DjangoObjectType):
    class Meta:
        model = Group
        filter_fields = {
            'name':['exact'],
        }
        interfaces = (relay.Node, )


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username':['exact','icontains','istartswith'],
            'email':['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    profile = relay.Node.Field(ProfileNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)

    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    group = relay.Node.Field(GroupNode)
    all_groups = DjangoFilterConnectionField(GroupNode)

'''
class CreateProfileMutation(relay.ClientIDMutation):
    class Input:
        user_id = graphene.Int()
        group_id = graphene.Int()
        username = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args):
        print(args)


class UserMutation(relay.ClientIDMutation):
    class Input:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args):
        print(args)


class CreateUserMutation(relay.ClientIDMutation):
    class Input:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args):
        print(args)
        '''
