from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class  AccountVlidationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
           text_type(user.pk) + text_type(timestamp) +text_type(user.is_active)
        )

        
Account_Vlidation_Token=AccountVlidationTokenGenerator()

