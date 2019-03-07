from api.enseignant.serializers import EnseignantSerializer
from api.eleve.serializers import EleveSerializer
from api.classe.serializers import ClasseMobileSerializer
from api.section.serializers import SectionSerializer
from api.devoir.serializers import DevoirMobileSerializer
from api.question.serializers import QuestionMobileSerializer
from .models import Enseignant, Eleve, Classe, Section, Devoir, Question
def jwt_response_payload_handler(token, user=None, request=None):
    groups = []
    mesclasses = []
    chapitres = []
    devoirs = []
    myuser = None
    sections = []
    questions = []
    myQuestions = []
    mobile = request.POST.get("mobile", None)
    for g in user.groups.all():
        groups.append(g.name)
    if 'enseignant' in groups:
        enseignant = Enseignant.objects.filter(user=user).first()
        myuser = EnseignantSerializer(enseignant).data
    else:
        eleve = Eleve.objects.filter(user=user).first()
        myuser = EleveSerializer(eleve).data
        print(myuser)
        if mobile:
            idClassesList = [classe['idClasse'] for classe in myuser['classes']]
            classes = Classe.objects.filter(idClass__in=idClassesList)
            for classe in classes:
                chapitres = chapitres + classe.chapitres
            idChapitreList = [chapitre['id'] for chapitre in chapitres]
            sectionsDB = Section.objects.filter(chapitre_id__in=idChapitreList)
            devoirDB = Devoir.objects.filter(chapitre_id__in=idChapitreList)
            devoirs = DevoirMobileSerializer(devoirDB, many=True).data
            for devoir in devoirs:
                numQuestions = devoir['numeroDesQuestions'].split(";")
                questionsDB = Question.objects.filter(idQuestion__in=numQuestions)
                tmp = QuestionMobileSerializer(questionsDB, many=True).data
                questions = questions + [quest for quest in tmp if quest not in questions]

            sections = SectionSerializer(sectionsDB, many=True).data
            mesclasses = ClasseMobileSerializer(classes, many=True).data
            myQuestions = questionParserForMobile(questions)

    return {
        'token': token,
        'user': myuser,
        'classes': mesclasses,
        'chapitres': chapitres,
        'sections': sections,
        'devoirs': devoirs,
        'questions': myQuestions
    }

def questionParserForMobile(questions):
    myQuestions = []
    for question in questions:
        if question["type"] == "schema":
            propositions = []
            for proposition in question["propositions"]:
                propositions.append({
                    "id": proposition["id"],
                    "enonce": proposition["numero"],
                    "label": proposition["annotation"],
                    "value": proposition["annotation"],
                    "proposition": None,
                    "solution": proposition["annotation"]
                })
            myQuestions.append({
                "id": question["idQuestion"],
                "enonce": question["image"],
                "type": question["type"],
                "propositions": {
                    "type": "croquis",
                    "lists": propositions
                }
            })
        if question["type"] == "qcm":
            propositions = []
            for proposition in question["propositions"]:
                propositions.append({
                    "id": proposition["id"],
                    "checked": False,
                    "enonce": proposition["enonce"],
                    "solution": proposition["solution"]
                })
            myQuestions.append({
                "id": question["idQuestion"],
                "enonce": question["enonce"],
                "type": question["type"],
                "propositions": {
                    "type": "qcm",
                    "lists": propositions
                }
            })
        if question["type"] == "qr":
            propositions = []
            enonce = []
            for proposition in question["propositions"]:
                propositions.append({
                    "id": proposition["id"],
                    "enonce": proposition["enonceA"],
                    "proposition": None,
                    "solution": proposition["enonceB"]
                })
                enonce.append({
                    "label": proposition["enonceB"],
                    "value": proposition["enonceB"]
                })
            myQuestions.append({
                "id": question["idQuestion"],
                "enonce": enonce,
                "type": question["type"],
                "propositions": {
                    "type": "qr",
                    "lists": propositions
                }
            })
    return myQuestions


