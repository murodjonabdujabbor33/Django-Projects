from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqatgina ko'rish uchun ruxsat beriladi
        if request.method in permissions.SAFE_METHODS: \
            # foydalanuvchi so'rovi SAFE_METHODS (GET, READ ...) lar
            # bo'lsa, ruxsat beriladi.
            return True
        # o'zgartirish uchun ruxsatnoma faqatgina post muallifiga beriladi
        return obj.author == request.user