# Django Import:
from django.db import models

# Django user model Import:
from django.contrib.auth.models import User

# Constants declaration:
ACTION = (
    (0, '---'),
    (1, 'Create'),
    (2, 'Update'),
    (3, 'Delete')
)


# Device model:
class ChangeLog(models.Model):
    """ Xxx. """

    class Meta:
        # Model name values:
        verbose_name = 'Change log'
        verbose_name_plural = 'Change logs'

    # Model data time information:
    changed = models.DateTimeField(
        verbose_name='Created',
        help_text='Change create date.',
        auto_now_add=True
    )

    # Correlation witch user model:
    administrator = models.ForeignKey(
        User,
        verbose_name='Administrator',
        help_text='Administrator responsible for change.',
        on_delete=models.SET_NULL,
        null=True
    )

    # Action:
    action = models.IntegerField(
        verbose_name='Change log action',
        help_text='The action that was performed on a given model.',
        choices=ACTION,
        default=0
    )

    # Change object details:
    object_name = models.CharField(
        verbose_name='Command name',
        help_text='CLI command name.',
        max_length=64
    )
    item_id = models.IntegerField(
        verbose_name='Command name',
        help_text='CLI command name.'
    )

    # Change details:
    after = models.JSONField(
        verbose_name='JSON object representation',
        help_text='JSON object representation after changes was made, and saved to database.',
        null=True,
        blank=True
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.object_name}: {self.item_id}'

    def __str__(self) -> str:
        return f'{self.object_name}: {self.item_id}'
