from openai import OpenAI

# Cette classe encapsule la logique pour interagir avec le modèle gpt-3.5-turbo d'OpenAI afin d'effectuer trois tâches principales :
# la préparation, l'analyse et l'extraction d'informations à partir de texte
class ExtractIa:

    def __init__(self):
        self.client = OpenAI(api_key="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")

    # prepare_text: Elimination du bruit, la normalisation, traitement initial visant à rendre le texte plus conforme aux besoins de l'analyse
    def prepare_text(self, text_to_prepare: str):
        print(text_to_prepare)
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Vous etes le service d'extraction d'Information (IE) métiers qui reçoit le texte de la demande de prêt soumise par le client."
                               "Ce texte peut contenir des informations variées, telles que le nom du client, l'adresse, le montant du prêt demandé, la description de la propriété."
                               "tu vas faire le prétraitement du Texte : Avant dextraire des informations, le texte de la demande est prétraité pour éliminer tout bruit ou caractère indésirable, le texte peut également être normalisé pour assurer la cohérence des données."
                               "Retourne moi le texte prétraité directement"
                },
                {"role": "user", "content": text_to_prepare}
            ]
        )
        prepared_text = completion.choices[0].message.content
        return prepared_text

    # Analyser le texte en utilisant des techniques de traitement automatique du langage naturel (NLP)
    def analyse_text(self, text_to_analyse: str):
        print(text_to_analyse)
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "vous etes le service d'analyse linguistique, vous utilisez des techniques de traitement automatique du langage naturel (NLP) pour analyser le texte."
                               "vous identifiez les entités dans le texte, telles que les noms, les adresses, les montants, type de bien immobilier ... "
                               "Retournez directement le resultat de l'analyse sans détails"
                },
                {"role": "user", "content": text_to_analyse}
            ]
        )
        analysed_text = completion.choices[0].message.content
        return analysed_text

    # Extraire des informations spécifiques conformément à un schéma défini (simulant un modèle de base de données)
    def extract_info(self, info_to_extract: str):
        print(info_to_extract)
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Les informations extraites sont classées en catégories spécifiques, telles que le nom_client, la description_propriete, adresse_propriete, montant_pret, duree_pret, revenu_mensuel, depenses_mensuelles"
                    "Retournez directement sans commentaire le resultat de l'analyse sans détails, retournez seulement le dictionnaire contenant les informations extraites pour remplir ce model exactement:"
                    "id = Column(Integer, primary_key=True)"
                    "nom_client = Column(String)"
                    "description_propriete = Column(String)"
                    "adresse_propriete = Column(String)"
                    "montant_pret = Column(Integer)"
                    "duree_pret = Column(String)"
                    "revenu_mensuel = Column(String)"
                    "depenses_mensuelles = Column(String)"
                    "vous pouvez donner des valeurs aleatoires a revenu_mensuel et depenses_mensuelles "
                },
                {"role": "user", "content": info_to_extract}
            ]
        )
        extracted_info = completion.choices[0].message.content
        return extracted_info
