from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_admin or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_admin
                or request.user.is_moderator)


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        worker = request.user
        document = view.get_object()

        if document.groups.filter(pk__in=worker.groups.all()).exists():
            return True
        worker_grade = worker.workergroup_set.get(group=document.groups.first()).grade
        if worker_grade.priority >= document.min_grade.priority:
            return True

        return False
