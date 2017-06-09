import json
import unittest
from dico_villes import *


class UnityTestSearch(unittest.TestCase):
    """Test case used for testing the functions on the SearchData module."""
    def testSearchInstallation(self):
        """Test the correct functioning of the methods installation_dictionary()"""
        listInstallations = [{"numInstall": 490050001, "nomInstall": "Terrains de Tennis", "nomCommune": "Andigné", "cdp": 49220, "nomLieuDit": "", "numVoie": "",
                                          "nomVoie": "Rue Chapelle des Vignes", "accessH": "Non", "nbPlacesP": 0, "longitude": -0.77791, "latitude": 47.66453}, {"numInstall": 490050002,
                                          "nomInstall": "Aire de Jeux", "nomCommune": "Andigné", "cdp": 49220, "nomLieuDit": "", "numVoie": "", "nomVoie": "Rue de la Croix Ruau",
                                          "accessH": "Non", "nbPlacesP": 0, "longitude": -0.77923, "latitude": 47.66498}]
        jsonObjects = json.dumps(listInstallations)
        self.assertEqual(installation_dictionary("Andigné"),jsonObjects)

    def testSearchInstallActivity(self):
        """Test the correct functioning of the methods installations_activity_list()"""
        listInstallations = [{"numInstall": 491760002, "nomInstall": "Complexe Sportif Lucien M\u00e9rignac", "nomCommune": "Lion-d'Angers", "cdp": 49220, "nomLieuDit": "", "numVoie": "",
                              "nomVoie": "Rue Henri et Robert de Cholet", "accessH": "Oui", "nbPlacesP": 0, "longitude": -0.71883, "latitude": 47.6253}, {"numInstall": 491760002,
                                "nomInstall": "Complexe Sportif Lucien M\u00e9rignac", "nomCommune": "Lion-d'Angers", "cdp": 49220, "nomLieuDit": "", "numVoie": "",
                                "nomVoie": "Rue Henri et Robert de Cholet", "accessH": "Oui", "nbPlacesP": 0, "longitude": -0.71946, "latitude": 47.62697}, {"numInstall": 491760006,
                                "nomInstall": "Stade des Guenelles", "nomCommune": "Lion-d'Angers", "cdp": 49220, "nomLieuDit": "", "numVoie": "", "nomVoie": "Rue du Courgeon",
                                "accessH": "Non", "nbPlacesP": 75, "longitude": -0.72112, "latitude": 47.62827}]

        jsonObjects = json.dumps(listInstallations)
        self.assertEqual(installations_activity_list("Lion-d'Angers","Tennis"), jsonObjects)

    def testSearchActivityCity(self):
        """Test the correct functioning of the methods city_activities_dictionary()"""
        listActivities= {7901: 'Tennis', 2901: 'Football / Football en salle (Futsal)', 6001: 'Pétanque et jeu provencal'}

        self.assertEqual(city_activities_dictionary("Andigné"), listActivities)

    def testSearchCity(self):
        """Test the correct functioning of the methods cityDictionary()"""
        listCity = ['Andigné', 'Brain-sur-Longuenée', 'Chambellay', 'Champteussé-sur-Baconne', 'Chenillé-Changé', 'Gené', 'Grez-Neuville',
                             'Jaille-Yvon', "Lion-d'Angers", 'Montreuil-sur-Maine', 'Pruillé', "Thorigné-d'Anjou", "Vern-d'Anjou"]

        self.assertEqual(city_dictionary("49220"), listCity)


if __name__ == '__main__':
    unittest.main()