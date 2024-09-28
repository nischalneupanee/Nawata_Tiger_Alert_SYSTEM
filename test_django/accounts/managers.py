from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.hashers import check_password, make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, Contact_no, password=None, **extra_fields):
        if not Contact_no:
         raise ValueError('Contact number must be set')
        user = self.model(Contact_no=Contact_no, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, Contact_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        return self.create_user(Contact_no, password,
                                **extra_fields)

