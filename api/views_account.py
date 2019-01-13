from api.enseignant.serializers import EnseignantSerializer
from .models import Enseignant
def jwt_response_payload_handler(token, user=None, request=None):
    groups = []
    for g in user.groups.all():
        groups.append(g.name)
    myuser = None
    if 'enseignant' in groups:
        enseignant = Enseignant.objects.filter(user=user).first()
        myuser = EnseignantSerializer(enseignant).data
    return {
        'token': token,
        'user': myuser
    }



