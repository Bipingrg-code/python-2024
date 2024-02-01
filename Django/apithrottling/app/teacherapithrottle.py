from rest_framework.throttling import UserRateThrottle

class TeacherRateThrottle(UserRateThrottle):
    scope = 'teachers'