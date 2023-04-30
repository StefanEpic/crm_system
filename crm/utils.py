from django.contrib.auth.mixins import UserPassesTestMixin


class TestIsAuthorThisTask(UserPassesTestMixin):
    # Is user task author or in group Management
    def test_func(self):
        user = self.requset.user
        return self.get_object().author_id == user.pk or user.groups.filter(name='Управление').exists()


def do_dict(tasks):
    d = {}
    for i in [_.end for _ in tasks]:
        d[i] = [j for j in tasks if j.end == i]
    return d

