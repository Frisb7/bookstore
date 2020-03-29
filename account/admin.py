from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

# Register your models here.

class AccountCreateForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'grno', 'garde')

class AccountAdmin(UserAdmin) :
    add_form = AccountCreateForm
    list_display = ('email', 'username', 'first_name', 'last_name', 'grno', 'garde')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'grno', 'garde')
    readonly_fields = ('date_joined', 'last_login')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'grno', 'garde', 'password1', 'password2', ),
        }),
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)