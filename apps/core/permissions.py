from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

PERMISSIONS_ROLE = (
    ('archer', 'Archer'),
    ('leader', 'Leader'),
    ('archery-range-pic', 'Archery Range PIC'),
    ('division-pic', 'Division PIC'),
    ('dpc', 'DPC'),
)


class IsArcher(IsAuthenticated):
    def has_permission(self, request, view):
        has_perm = super(IsArcher, self).has_permission(request, view)
        if request.user.groups.filter(name=PERMISSIONS_ROLE[0][0]).count() > 0:
            return has_perm
        return False


class IsLeader(IsAuthenticated):
    def has_permission(self, request, view):
        has_perm = super(IsLeader, self).has_permission(request, view)
        try:
            request.user.member.leading_club
            return has_perm
        except ObjectDoesNotExist:
            return False


class IsDivisionPIC(IsAuthenticated):
    def has_permission(self, request, view):
        has_perm = super(IsDivisionPIC, self).has_permission(request, view)
        try:
            request.user.member.division_pic
            return has_perm
        except ObjectDoesNotExist:
            return False


class IsArcheryRangePIC(IsAuthenticated):
    def has_permission(self, request, view):
        has_perm = super(IsDivisionPIC, self).has_permission(request, view)

        member = request.user.member
        if hasattr(member, 'archery_range') and member.archery_range:
            return has_perm
        elif hasattr(member.club, 'archery_range') and member.club.archery_range and member.club.lead == member:
            return has_perm
        return False
