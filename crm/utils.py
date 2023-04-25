from django.contrib.auth.mixins import UserPassesTestMixin


class TestIsAuthorThisTask(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().author_id == self.request.user.pk


def do_dict(tasks):
    d = {}
    for i in [_.end for _ in tasks]:
        d[i] = [j for j in tasks if j.end == i]
    return d

