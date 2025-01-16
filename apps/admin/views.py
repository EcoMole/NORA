from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def test_error_email_reporting(request):
    raise Exception(
        "This is a testing API endpoint to test whether Django's email error reporting works."
    )
