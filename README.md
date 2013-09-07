django-20522
============

Code used to validate the bug in Django project ticket #20522

Please note that the root url is not enabled -- please skip directly to the
admin for validation. A test database is already configured using sqlite and
included in the commit.

This same code can be used to verify the bug fix.

### Verifying the Add View Bug in Unpatched Django ###

1. Log into the admin with the username 'admin' and password '1234'
2. Click 'Add' under 'Parents with dependent children'
3. Set 'contingent_field' to 2, and 'dependent_field' to 'Guerilla Knitting'
4. Hit 'Save' and verify that you only see 'This field is required.' in the
    upper portion of the form (this is the bug).
5. Set 'some_required_info' to 'Perhaps' and hit 'Save'; verify that you now
    see "You're doing it wrong" in the lower formset (this would have been the
    correct behavior from the previous step)
6. Change 'contingent_field' to 1 and save.


### Disconfirming the Change View Bug ###
1. Edit the 'Perhaps? +1!' ParentWithDependentChildren you created during
    the verification of the add view
2. Change 'some_required_info' to 'Maybe' and 'contingent_field' to 2.
3. Hit 'Save' and note that you see errors in both the top and bottom portions
    of the form (there does not seem to be a bug here, contrary to the ticket)
