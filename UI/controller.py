import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        """Carica musei ed epoche nel menu a tendina."""
        # --- Musei ---
        musei = self._model.get_musei()
        self._view.dropdown_museo.options.clear()
        self._view.dropdown_museo.options.append(ft.dropdown.Option("Nessun filtro"))
        for m in musei:
            self._view.dropdown_museo.options.append(ft.dropdown.Option(m.nome))

        # --- Epoche ---
        epoche = self._model.get_epoche()
        self._view.dropdown_epoca.options.clear()
        self._view.dropdown_epoca.options.append(ft.dropdown.Option("Nessun filtro"))
        for e in epoche:
            self._view.dropdown_epoca.options.append(ft.dropdown.Option(e))

        self._view.update()

    # TODO

    # CALLBACKS DROPDOWN
    def museo_changed(self, e):
        self.museo_selezionato = e.control.value

    def epoca_changed(self, e):
        self.epoca_selezionata = e.control.value

    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        """Recupera gli artefatti filtrati e aggiorna la lista nella view."""
        artefatti = self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)

        self._view.list_view.controls.clear()

        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato per i filtri selezionati.")
        else:
            for a in artefatti:
                self._view.list_view.controls.append(
                    ft.Text(f"{a.nome} | Epoca: {a.epoca} | Museo: {a.id_museo}")
                )

        self._view.update()
    # TODO
